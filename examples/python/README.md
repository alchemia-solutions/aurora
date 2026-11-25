# examples/python

| File | What it does |
|---|---|
| `aurora_client.py` | A small read-only client. It reads the token from `AURORA_TOKEN` and sends it only in the `Authorization` header, refuses a plain `http://` address except on localhost, waits `Retry-After` and tries again on 429, walks cursor listings, reads up to 50 ids per batch call, and raises `AuroraError` with `status`, `code`, `message` and `request_id` |
| `filter_compounds.py` | Filters a list of `alchemia_id` values by molecular weight, logP, TPSA and QED, then by predicted ADMET values (`--admet "hERG<=0.5"`). Writes a TSV with the package and licence of each compound |
| `docking_set.py` | Builds a ligand set for docking from a list: one 3D SDF per compound, checked against its `ETag`, one multi-record `ligands.sdf`, a `license.tsv` and the attribution of the sources |
| `read_api.py` | Calls the public summary and a few routes that need a token, and prints the start of each answer |

## How to use

```bash
pip install requests
export AURORA_TOKEN=aurk_...        # an API key from Profile of your approved account
python examples/python/filter_compounds.py --ids ALC1 ALC2 --max-mw 500 --admet "hERG<=0.5" > kept.tsv
cut -f1 kept.tsv | tail -n +2 > kept_ids.txt
python examples/python/docking_set.py --ids-file kept_ids.txt --out my_ligands
```

Run the scripts from any folder; they import `aurora_client.py` from their own folder. `AURORA_BASE_URL`
overrides the address. The routes they call, and which of them an API key may call, are in
[../../docs/API.md](../../docs/API.md). What the values mean and what each licence asks of you:
[../../docs/USING_THE_DATA.md](../../docs/USING_THE_DATA.md).

The client follows the OpenAPI contract of platform version 1.5.2 (read 2026-11-25). In production on
2026-11-25 an API key was answered 200 on compounds, text search and collections. `filter_compounds.py` and
`docking_set.py` also call the batch route, `/features`, `structure.sdf` and `/v1/sources/attribution`, which
the platform's allow-list for keys includes; those were not part of that production check.

## What is not here

No write calls, no embedded token, no download of bundles or packages (they need the signed-in session of
the platform). `docking_set.py` writes only into the folder you name, and refuses a folder that already holds
files. ADMET values are predictions, never measurements.
