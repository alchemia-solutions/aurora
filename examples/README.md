# examples

Small programs that only read the AURORA API. They send no credential anywhere except the token you set in
your own shell.

| Folder | What it holds |
|---|---|
| [python](python/) | `read_api.py`, using `requests` |
| [curl](curl/) | `read_api.sh`, using `curl` |

## How to use

Run the program of your choice. The routes that need no token run as they are, once the v1.3 release is
live. For the others set `AURORA_TOKEN` to the token of your approved account, or the API answers 401. What
the calls do, and which routes need a token, is in [../docs/API.md](../docs/API.md).

## What is not here

No write calls, no download of files, no token and no database connection. Nobody gets direct database
access.
