# API

[Repository home](../README.md) · [Docs index](README.md)

AURORA is meant to be served through a versioned REST API at `https://aurora.alchemia.solutions/v1/`. This
page lists the routes of the OpenAPI contract of the platform, version 1.4.0 of the closed beta, read on
2026-11-17 from the contract file of the platform repository. The contract is what this page follows. The
instance that answers in the beta may run another version, and a route listed here can answer 404, or answer
without a token.
This page does not repeat the parameters or the answers: read them in the interactive reference, under
Documents on the platform, which needs an approved account during the beta.

## Access

The platform is a closed beta for approved accounts. In that mode the contract of version 1.4.0 leaves three kinds of route
open: the health probes, the sign-in doors and one route of aggregates. Every other route needs a Bearer
token and answers 401 without it.

Send the token as `Authorization: Bearer <token>`. A missing or invalid token answers 401. Sign In exists on
the platform. The Terms of Use and the Privacy Policy are final (version 1.0), and sign-up for the public is not open: it opens as its own step after the next platform release is cut, with no date. Nobody receives
direct database access, not even read-only. A request can be rate limited, and a limit answers 429
with `Retry-After`.

## Routes that need no token

| Route | What it returns |
|---|---|
| `GET /v1/public/summary` | Aggregates behind the public Home. It holds no compound |
| `GET /health/live`, `GET /health/ready` | The health probes |
| `POST /v1/auth/login`, `POST /v1/auth/register`, `POST /v1/auth/forgot-password`, `POST /v1/auth/reset-password`, `POST /v1/auth/confirm-email`, `POST /v1/auth/resend-confirmation`, `POST /v1/auth/session/refresh`, `POST /v1/auth/session/logout` | The sign-in doors of an account, with a few more of the same kind in the contract |
| `GET /v1/auth/providers`, `GET /v1/auth/password-policy`, `GET /v1/auth/oauth/{provider}/authorize` and `/callback` | Which sign-in methods work, the password rules, and the OAuth steps |

## Routes that need a Bearer token

| Route | What it does |
|---|---|
| `GET /v1/search/text?q=...` | Search by identifier, name or synonym. Optional: `limit`, `availability`, `sources`, `space`, `fields` |
| `POST /v1/search/substructure` | Off in the beta (switched off; expect an error, not results). SMARTS substructure search. Body: `smarts` (required, at most 500 characters), `limit`, `availability`, `use_chirality`, `sources`, `space` |
| `POST /v1/search/similarity` | Off in the beta (switched off; expect an error, not results). Tanimoto similarity, Morgan radius 2, 2048 bits. Body: `smiles` (required), `min_similarity` (0.1 to 1, default 0.7), `limit`, `availability`, `sources`, `space` |
| `GET /v1/compounds`, `GET /v1/compounds/batch?ids=...` | Listing with keyset cursors, and a batch summary |
| `GET /v1/compounds/{alchemia_id}` | The record of one compound |
| `GET /v1/compounds/{alchemia_id}/features`, `.../fingerprints`, `.../protonation-variants`, `.../provenance`, `.../external-ids`, `.../structures`, `.../structure.sdf`, `.../structure.svg`, `.../structure2d.json` | Sub-resources of one compound |
| `GET /v1/compounds/{alchemia_id}/activities`, `GET /v1/compounds/{alchemia_id}/bioactivity` | Bioactivity rows of a compound. Behind a feature flag that is off in the beta: expect 404 or 503 |
| `GET /v1/id-history/{alchemia_id}` | The old-to-new map of the renumbering of release 2.0.0 |
| `GET /v1/collections`, `GET /v1/collections/{slug}`, `.../compounds`, `.../sources` | The collections, one collection, its compounds and its sources |
| `GET /v1/catalog/stats` | Catalog statistics |
| `GET /v1/dashboard/collections`, `licenses`, `sources`, `admet`, `clinical-phases` | Aggregates for the Dashboard |
| `GET /v1/sources`, `GET /v1/sources/attribution`, `GET /v1/sources/{source_key}` | The sources shown, with attribution |
| `GET /v1/compounds/{alchemia_id}/download/{kind}`, `GET /v1/compounds/{alchemia_id}/file/{file_format}` and the bundle routes under `/v1/collections/{slug}/bundles` | Files. No package is published, so these answer that the package is not ready. The one-compound package route, `GET /v1/compounds/{alchemia_id}/package`, is in the platform code of 2026-11-19 and not in the 1.4.0 contract this page follows |
| `/v1/account/*`, `GET /v1/auth/me` | Your own account |
| `/v1/collaborate/*` | Register a study, request a database, send a published work |

The `/v1/admin/*` routes are for the operators of the platform and are not part of a consumer's use.

## Behaviour to expect

- The public compound identifier is `alchemia_id`, of the form `ALC<n>`. Internal keys and raw identifiers
  of third-party records never appear.
- Listings are cursor based (`items`, `has_more`, `next_cursor`). The search routes answer `items` and
  `truncated`.
- Chemical queries are `POST`, so SMARTS and SMILES stay out of URLs and logs.
- Errors come back as an envelope with `code`, `message` and `request_id`.
- Every compound answer carries its `license`: the package it belongs to.
- Only compounds of the two packages are served. Any other is answered as a compound that does not exist.

## Examples

[`examples/python/read_api.py`](../examples/python/read_api.py) and
[`examples/curl/read_api.sh`](../examples/curl/read_api.sh). Both only read. They call the one open route
without a token and the others with `AURORA_TOKEN`. Neither calls a download or a write route.
