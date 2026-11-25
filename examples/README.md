# examples

Small programs that only read the AURORA API. They send no credential anywhere except the token you set in
your own shell.

| Folder | What it holds |
|---|---|
| [python](python/) | `aurora_client.py`, a small client, with `filter_compounds.py` and `docking_set.py` that use it; `read_api.py`. All use `requests` |
| [curl](curl/) | `read_api.sh`, using `curl` |

## How to use

Run the program of your choice. The platform is a closed beta. One route, the public summary, needs no token. For every other route set
`AURORA_TOKEN` to the token of your approved account, or the API answers 401. What the calls do, and which
routes need a token, is in [../docs/API.md](../docs/API.md); how to work with the data, in
[../docs/USING_THE_DATA.md](../docs/USING_THE_DATA.md). The calls follow the OpenAPI contract of platform
version 1.5.2, checked in production on 2026-11-25.

## What is not here

No write calls, no download of bundles or packages, no token and no database connection. `docking_set.py` saves the 3D structures it reads through the API in a folder you name. Nobody gets direct database
access.
