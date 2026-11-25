#!/usr/bin/env python3
"""Build a ligand set for docking from a list of AURORA compounds, one 3D SDF per compound.

    pip install requests
    export AURORA_TOKEN=aurk_...
    python examples/python/docking_set.py --ids-file kept_ids.txt --out my_ligands

Input: alchemia_id values (ALC<n>), from --ids-file (one per line, # comments allowed) and/or --ids.
For each compound:
  1. GET /v1/compounds/batch says whether it has an SDF (sdf_available) and gives its licence;
  2. GET /v1/compounds/{alchemia_id}/structure.sdf returns the 3D geometry, byte for byte as stored;
  3. the SHA-256 of the body is compared with the strong ETag of the answer, so a damaged file is refused.

Written in --out (an existing file is never overwritten):
  ALC<n>.sdf      one file per compound
  ligands.sdf     every compound in one multi-record SDF, ready for most docking front ends
  license.tsv     alchemia_id, package, SPDX id and licence URL of each compound
  sources.json    the attribution text of every source, from GET /v1/sources/attribution

What this set is and is not:
  * The SDF is the canonical structure. The PDBQT files prepared for docking are not served to an API key;
    they are in the bundles and in the one-compound package, which need the signed-in session of the
    platform (docs/USING_THE_DATA.md). Most docking tools prepare a PDBQT from the SDF.
  * A structure prepared by the pipeline is not validated for your target: protonation and tautomer states
    may need work for your binding site. Stereoisomers are not enumerated.
  * Each compound keeps the licence of its package. If license.tsv lists AURORA-NC compounds, those are for
    non-commercial use only. Cite AURORA and the upstream sources when you publish (README, Citing).
Licensed under Apache-2.0 (LICENSE-CODE).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

from aurora_client import AuroraClient, AuroraError, read_ids


def write_new(path: Path, data: bytes) -> None:
    with open(path, "xb") as handle:  # "x": fail rather than overwrite
        handle.write(data)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--ids-file", help="file with one alchemia_id per line")
    parser.add_argument("--ids", nargs="*", help="alchemia_id values on the command line")
    parser.add_argument("--out", default="aurora_docking_set", help="output folder; must not hold files of an earlier run")
    args = parser.parse_args()

    ids = read_ids(args.ids_file, args.ids)
    if not ids:
        parser.error("give at least one alchemia_id with --ids or --ids-file")
    out = Path(args.out)
    if out.exists() and (not out.is_dir() or any(out.iterdir())):
        print(f"error: {out} is not an empty folder; choose a new one", file=sys.stderr)
        return 1

    try:
        client = AuroraClient()
        found, missing = client.batch(ids, fields="sdf_available")
    except (ValueError, AuroraError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    out.mkdir(parents=True, exist_ok=True)
    for alchemia_id in missing:
        print(f"skip {alchemia_id}: not served to this account", file=sys.stderr)

    records: list[bytes] = []
    licence_rows = ["alchemia_id\tpackage\tlicense_spdx\tlicense_url"]
    for compound in found:
        alchemia_id = compound["alchemia_id"]
        if not compound.get("sdf_available"):
            print(f"skip {alchemia_id}: no SDF", file=sys.stderr)
            continue
        try:
            body, headers = client.get_bytes(f"/v1/compounds/{alchemia_id}/structure.sdf")
        except AuroraError as exc:
            print(f"skip {alchemia_id}: {exc}", file=sys.stderr)
            continue
        etag = (headers.get("ETag") or "").strip().removeprefix("W/").strip('"')
        digest = hashlib.sha256(body).hexdigest()
        if etag and etag != digest:
            print(f"skip {alchemia_id}: the file does not match its ETag", file=sys.stderr)
            continue
        write_new(out / f"{alchemia_id}.sdf", body)
        record = body.rstrip(b"\r\n")
        if not record.endswith(b"$$$$"):
            record += b"\n$$$$"
        records.append(record + b"\n")
        licence = compound.get("license") or {}
        licence_rows.append("\t".join([alchemia_id, licence.get("package", ""), licence.get("spdx", ""), licence.get("url", "")]))

    write_new(out / "ligands.sdf", b"".join(records))
    write_new(out / "license.tsv", ("\n".join(licence_rows) + "\n").encode("utf-8"))
    try:
        attribution = client.get("/v1/sources/attribution")
        write_new(out / "sources.json", json.dumps(attribution, indent=2, ensure_ascii=False).encode("utf-8"))
    except AuroraError as exc:
        print(f"note: attribution not written: {exc}", file=sys.stderr)

    noncommercial = sum(1 for row in licence_rows[1:] if row.split("\t")[1] == "AURORA-NC")
    print(f"{len(records)} structures written to {out}", file=sys.stderr)
    if noncommercial:
        print(f"{noncommercial} of them are AURORA-NC: non-commercial use only (license.tsv)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
