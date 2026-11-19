# examples/python

`read_api.py` calls the one route that needs no token (the public summary) and then the routes that need a
token (catalog statistics, collections, text search by identifier, name or synonym, and the record of the first
hit). It prints the start of each answer. The substructure and similarity search routes are off in the beta, so
the program does not call them.

## How to use

```bash
pip install requests
export AURORA_TOKEN=<a token from your approved account>
python examples/python/read_api.py
```

`AURORA_BASE_URL` overrides the address. When a route needs a token and none is set, the program says that
the API answered 401 and goes on. Any other error status stops the program with the error.

## What is not here

No write calls and no embedded token. The program does not describe the shape of the answers: read the
OpenAPI contract (see [../../docs/API.md](../../docs/API.md)).
