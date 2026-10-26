# API

AURORA is served through a versioned REST API at `https://aurora.alchemia.solutions/v1/`. The OpenAPI
document of the API is the contract, and the interactive reference is under
[Documents](https://aurora.alchemia.solutions/docs) on the platform. This page only says what the
examples in this repository call.

## Access

The platform is in closed beta. Without an invitation token, `/v1/` answers 401. Send the token as
`Authorization: Bearer <token>`. Nobody receives direct database access, not even read-only.

## Routes the examples use

| Route | What it does |
|---|---|
| `GET /v1/catalog/stats` | Aggregate counts |
| `GET /v1/collections` | The collections |
| `GET /v1/search/text?q=...&limit=...` | Search by identifier, name or synonym |
| `POST /v1/search/substructure` | Body: `smarts`, `limit` |
| `POST /v1/search/similarity` | Body: `smiles`, `min_similarity`, `limit` |

Other routes exist for compounds, sources, downloads and accounts. Read them in the OpenAPI reference
rather than here, because this page does not track every change.

## Behaviour to expect

- Errors come back as an envelope with `code`, `message` and `request_id`.
- Reads are rate limited.
- Similarity uses Morgan fingerprints, radius 2, 2048 bits, generated on the server from your SMILES.
- Internal row keys and raw identifiers of third-party records never appear in a response.

## Examples

[`examples/python/read_api.py`](../examples/python/read_api.py) and
[`examples/curl/read_api.sh`](../examples/curl/read_api.sh). Both only read.
