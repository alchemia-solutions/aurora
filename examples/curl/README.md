# examples/curl

`read_api.sh` makes the same read calls as the Python example, except the record of the first hit, with `curl`.
The public summary needs no token; every other call sends `AURORA_TOKEN`.

## How to use

```bash
export AURORA_TOKEN=<a token from your approved account>
bash examples/curl/read_api.sh
```

`AURORA_BASE_URL` overrides the address. Without a token every call but the first answers 401.

## What is not here

No write calls and no embedded token.
