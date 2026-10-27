# API

[Repository home](../README.md) · [Docs index](README.md)

AURORA is served through a versioned REST API at `https://aurora.alchemia.solutions/v1/`. The OpenAPI
document of the API is the contract, and the interactive reference is under
[Documents](https://aurora.alchemia.solutions/docs/api) on the platform. This page lists which routes need
a token and which do not. It does not repeat the parameters or the answers: read them in the reference.

## Access

The platform is a closed beta, and the v1.3 release has been live since 2026-10-26. The routes below need no
token. Every other route, except the health probes and the sign-in doors, needs a Bearer token from an
approved account.

Send the token as `Authorization: Bearer <token>`. A missing or invalid token answers 401. Sign In and Sign
Up exist on the platform, and sign-up for the public is off until the privacy policy is published. Nobody
receives direct database access, not even read-only.

## Routes that need no token (since the v1.3 release)

| Route | What it returns |
|---|---|
| `GET /v1/public/summary` | Aggregates for the public Home |
| `GET /v1/catalog/stats` | Live catalog statistics |
| `GET /v1/collections` | The collections |
| `GET /v1/collections/{slug}` | One collection |
| `GET /v1/collections/{slug}/sources` | The sources shown for a collection, with license and attribution |
| `GET /v1/collections/{slug}/bundles` | The bundles of a collection: sizes, counts and checksums, no file |
| `GET /v1/sources/attribution` | All displayed sources with license and attribution |
| `GET /v1/dashboard/collections`, `licenses`, `sources`, `admet`, `clinical-phases` | Aggregates for the Dashboard |
| `GET /v1/collaborate/config`, `forms`, `citation`, `community` | The static texts and limits of Collaborate |

Routes behind a feature flag can answer 404 or 503 when the flag is off. Reads are rate limited, and a
limit answers 429 with `Retry-After`. The sign-in doors (`POST /v1/auth/login`, `POST /v1/auth/register`,
`GET /v1/auth/providers`) and the health probes (`GET /health/live`, `GET /health/ready`) need no token
either.

## Routes that need a Bearer token

| Route | What it does |
|---|---|
| `GET /v1/search/text?q=...` | Search by identifier, name or synonym |
| `POST /v1/search/substructure` | SMARTS substructure search. Body: `smarts`, `limit` |
| `POST /v1/search/similarity` | Tanimoto similarity, Morgan radius 2, 2048 bits. Body: `smiles`, `min_similarity`, `limit` |
| `GET /v1/compounds`, `GET /v1/compounds/batch` | Listing with keyset cursors, and a batch summary |
| `GET /v1/compounds/{alchemia_id}` and its sub-resources | The record of one compound |
| `GET /v1/collections/{slug}/compounds` | The compounds of a collection |
| `GET /v1/compounds/{alchemia_id}/download/...` and the bundle download routes | Files. The packages are not published, so downloads answer that the package is not ready |
| `GET /v1/auth/me`, `/v1/account/*` | Your own account |
| `/v1/collaborate/*` forms | Register a study, request a database, send a published work |

## Behaviour to expect

- The public compound identifier is `alchemia_id`, of the form `ALC<n>`. Internal keys and raw identifiers
  of third-party records never appear.
- Listings are cursor based (`items`, `has_more`, `next_cursor`).
- Chemical queries are `POST`, so SMARTS and SMILES stay out of URLs and logs.
- Errors come back as an envelope with `code`, `message` and `request_id`.
- Every compound answer carries its `license`: the package it belongs to.

## Examples

[`examples/python/read_api.py`](../examples/python/read_api.py) and
[`examples/curl/read_api.sh`](../examples/curl/read_api.sh). Both only read. They call the open routes
without a token and the others with `AURORA_TOKEN`. Neither calls a download or a write route.
