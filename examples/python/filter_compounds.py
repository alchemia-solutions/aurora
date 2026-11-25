#!/usr/bin/env python3
"""Filter a list of AURORA compounds by computed properties and by predicted ADMET values.

    pip install requests
    export AURORA_TOKEN=aurk_...
    python examples/python/filter_compounds.py --ids-file my_ids.txt --max-mw 500 --max-logp 5 \\
        --admet "hERG<=0.5" --admet "AMES<=0.5" > kept.tsv

Input: alchemia_id values (ALC<n>), from --ids-file (one per line, # comments allowed) and/or --ids.
Step 1, one call per 50 ids: GET /v1/compounds/batch gives molecular_weight, logp, tpsa and qed. Compounds
outside the property bounds are dropped here, so the ADMET step reads fewer records.
Step 2, only when --admet is given: GET /v1/compounds/{alchemia_id}/features for each remaining compound,
and its admet_profile is compared with each condition. A condition names an ADMET-AI task (hERG, AMES,
Solubility_AqSolDB, ...; the list is the ADMET group of docs/DATA_DICTIONARY.md). The program accepts the
task name with or without the admet_ prefix. A compound whose profile has no value for a task fails that
condition and the reason is printed.

ADMET values are model predictions, never measurements: use them for triage. Classifiers give a
probability between 0 and 1, regressors a value in the units of their training set.

Output: a TSV on stdout with alchemia_id, package, licence SPDX, the four properties and the ADMET values
asked for. Keep the package and licence columns with the data: each compound carries the licence of its
package, and AURORA-NC compounds are for non-commercial use only.

To filter a whole collection instead of a list, the API filters on the server: GET /v1/compounds or
GET /v1/collections/{slug}/compounds with min_mw, max_mw, min_logp, ... (docs/API.md).
Licensed under Apache-2.0 (LICENSE-CODE).
"""
from __future__ import annotations

import argparse
import operator
import re
import sys

from aurora_client import AuroraClient, AuroraError, read_ids

CONDITION = re.compile(r"^\s*([A-Za-z0-9_]+)\s*(<=|>=|<|>)\s*(-?[0-9]+(?:\.[0-9]+)?)\s*$")
OPERATORS = {"<=": operator.le, ">=": operator.ge, "<": operator.lt, ">": operator.gt}
PROPERTIES = ("molecular_weight", "logp", "tpsa", "qed")
FLAG = {"molecular_weight": "mw", "logp": "logp", "tpsa": "tpsa", "qed": "qed"}  # --min-mw, --max-logp, ...


def parse_condition(text: str) -> tuple[str, str, float]:
    match = CONDITION.match(text)
    if not match:
        raise argparse.ArgumentTypeError(f"not a condition: {text!r} (expected TASK<=VALUE, TASK>=VALUE, TASK<VALUE or TASK>VALUE)")
    task, op, value = match.groups()
    if task.startswith("admet_"):
        task = task[len("admet_"):]
    return task, op, float(value)


def admet_value(profile: dict, task: str) -> float | None:
    for key in (task, f"admet_{task}"):
        value = profile.get(key)
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            return float(value)
    return None


def within(value: float | None, low: float | None, high: float | None) -> bool:
    if low is None and high is None:
        return True
    if value is None:
        return False
    return (low is None or value >= low) and (high is None or value <= high)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--ids-file", help="file with one alchemia_id per line")
    parser.add_argument("--ids", nargs="*", help="alchemia_id values on the command line")
    for name in PROPERTIES:
        parser.add_argument(f"--min-{FLAG[name]}", type=float, dest=f"min_{name}", help=f"lower bound of {name}")
        parser.add_argument(f"--max-{FLAG[name]}", type=float, dest=f"max_{name}", help=f"upper bound of {name}")
    parser.add_argument("--admet", action="append", type=parse_condition, default=[], help='e.g. "hERG<=0.5"; repeat for more')
    args = parser.parse_args()

    ids = read_ids(args.ids_file, args.ids)
    if not ids:
        parser.error("give at least one alchemia_id with --ids or --ids-file")

    try:
        client = AuroraClient()
        found, missing = client.batch(ids)
    except (ValueError, AuroraError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    for alchemia_id in missing:
        print(f"skip {alchemia_id}: not served to this account", file=sys.stderr)

    kept = [c for c in found if all(within(c.get(p), getattr(args, f"min_{p}"), getattr(args, f"max_{p}")) for p in PROPERTIES)]
    print(f"{len(kept)} of {len(found)} compounds within the property bounds", file=sys.stderr)

    tasks = [task for task, _, _ in args.admet]
    header = ["alchemia_id", "package", "license_spdx", *PROPERTIES, *[f"admet_{t}" for t in tasks]]
    print("\t".join(header))
    written = 0
    for compound in kept:
        alchemia_id = compound["alchemia_id"]
        values: dict[str, float | None] = {}
        if args.admet:
            try:
                profile = client.get(f"/v1/compounds/{alchemia_id}/features").get("admet_profile") or {}
            except AuroraError as exc:
                print(f"skip {alchemia_id}: {exc}", file=sys.stderr)
                continue
            failed = None
            for task, op, bound in args.admet:
                values[task] = admet_value(profile, task)
                if values[task] is None:
                    failed = f"no {task} value in its ADMET profile"
                elif not OPERATORS[op](values[task], bound):
                    failed = f"{task} = {values[task]:g}, condition {op} {bound:g}"
                if failed:
                    break
            if failed:
                print(f"drop {alchemia_id}: {failed}", file=sys.stderr)
                continue
        licence = compound.get("license") or {}
        row = [alchemia_id, licence.get("package", ""), licence.get("spdx", "")]
        row += ["" if compound.get(p) is None else f"{compound[p]:g}" for p in PROPERTIES]
        row += ["" if values.get(t) is None else f"{values[t]:g}" for t in tasks]
        print("\t".join(row))
        written += 1
    print(f"{written} compounds written", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
