# examples/python

`read_api.py` calls three open routes (public summary, catalog statistics, collections) and then the routes
that need a token (text search, substructure search, similarity search and the record of the first hit). It
prints the start of each answer.

## How to use

```bash
pip install requests
export AURORA_TOKEN=<a token from your approved account>
python examples/python/read_api.py
```

`AURORA_BASE_URL` overrides the address. When a route needs a token and none is set, the program says that
the API answered 401 and goes on.

## What is not here

No write calls and no embedded token. The program does not describe the shape of the answers: read the
OpenAPI reference on the platform.
