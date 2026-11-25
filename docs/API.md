# API

[Repository home](../README.md) · [Docs index](README.md)

AURORA is served through a versioned REST API at `https://aurora.alchemia.solutions/v1/`. This page is a guide:
one example call and the shape of its answer for each group of routes, then the full table of routes. It
follows the OpenAPI contract file of the platform repository, `info.version` 1.5.2, 116 operations on 106 paths,
read on 2026-11-25. Production behaviour (API keys, the rate limit, which features are on) was checked on
2026-11-25 and is recorded in [QUICKSTART.md](QUICKSTART.md); start there if you have no key yet. The
interactive reference and the OpenAPI file are not published in the beta.

In the answers below, values in angle brackets (`<integer>`, `<SMILES>`) stand for the type of the field, not
a value of the corpus. The `license` objects show the real text the platform uses for each package.

## Access

The platform is a closed beta for approved accounts. Send a token as `Authorization: Bearer <token>`, never
in a URL. The token is either the signed-in session of the platform or an API key (`aurk_...`) created in
Profile. A missing, invalid, expired or revoked token answers 401.

An API key only reads. The platform holds one allow-list of the routes a key may call, and refuses every
other route with `403 api_key_not_allowed`. The column "API key" of the [route table](#route-table) is read
from that allow-list in the platform code on 2026-11-25. In production on 2026-11-25 a key was answered 200
on compounds, the batch summary, features, fingerprints, provenance, the SDF structure, the activity rows
(`/activities`), text search, collections and the source attribution, and 403 on `/bioactivity`, bundles, the
one-compound package and the account.

Sign-up is open by request: `POST /v1/auth/register` creates a pending account and an administrator approves
it. The Terms of Use and the Privacy Policy are in version 1.1 since platform 1.5.2 (2026-11-23). Nobody
receives direct database access, not even read-only.

## Errors and the rate limit

Every 4xx and 5xx answer is a problem document (`application/problem+json`, RFC 9457):

```json
{
  "type": "urn:alchemia:aurora:problem:not_found",
  "title": "Not Found",
  "status": 404,
  "detail": "<human-readable message>",
  "code": "not_found",
  "request_id": "<id>",
  "details": null,
  "error": { "code": "not_found", "message": "<human-readable message>", "request_id": "<id>", "details": null }
}
```

Branch on `code`, show `detail`, and quote `request_id` when you report a problem. `error` repeats the
same three fields for older clients. The codes you will meet most are in
[QUICKSTART.md](QUICKSTART.md#5-limits-and-errors).

The limit in production on 2026-11-25 is 60 requests per 60 seconds per address, shared by every key of the
account. Over it the API answers `429` (`code` `rate_limited`) with `Retry-After`: wait that many seconds.
[`aurora_client.py`](../examples/python/aurora_client.py) does this for you.

## Open: the public summary

```bash
curl -s https://aurora.alchemia.solutions/v1/public/summary
```

```json
{
  "release_version": "<string>",
  "measured_at": "<timestamp>",
  "packages": [ "..." ],
  "collections": [ "..." ],
  "sources": [ "..." ],
  "phases": { "...": "..." },
  "unavailable_sections": [ "..." ]
}
```

The aggregates behind the Home page. It holds no compound and needs no token.

## Search

```bash
curl -s -H "Authorization: Bearer $AURORA_TOKEN" \
  "https://aurora.alchemia.solutions/v1/search/text?q=caffeine&limit=5&max_mw=500"
```

```json
{
  "items": [
    {
      "alchemia_id": "ALC<n>",
      "license": { "package": "AURORA", "label": "AURORA (CC BY-SA 4.0)", "spdx": "CC-BY-SA-4.0",
                   "url": "https://creativecommons.org/licenses/by-sa/4.0/", "noncommercial": false },
      "preferred_name": "<string>",
      "canonical_smiles": "<SMILES>",
      "inchikey": "<InChIKey>",
      "molecular_weight": "<number>", "logp": "<number>", "tpsa": "<number>", "qed": "<number>",
      "sdf_available": true, "pdbqt_available": true,
      "spaces": [ "<collection slug>" ],
      "matched_name": "<the string that matched>",
      "match_type": "preferred_name",
      "score": 1.0
    }
  ],
  "truncated": false
}
```

The query matches an `alchemia_id`, an InChIKey, a cross-reference, a name or a synonym; `match_type` says
which, in that order of rank, with a fuzzy tier last. `truncated` is true when more matches exist beyond
`limit`. The same property bounds as the compound listing apply (`min_mw`, `max_logp`, ...), and `space`
restricts the search to one collection.

Chemical search is `POST`, so SMARTS and SMILES stay out of URLs and logs: `POST /v1/search/substructure`
(body `smarts`) and `POST /v1/search/similarity` (body `smiles`, `min_similarity`). Both were off in
production on 2026-11-25 and answer `503` with `substructure_search_unavailable` or
`similarity_search_unavailable`.

## Compounds

### One record

```bash
curl -s -H "Authorization: Bearer $AURORA_TOKEN" "https://aurora.alchemia.solutions/v1/compounds/ALC1"
```

```json
{
  "alchemia_id": "ALC1",
  "license": { "package": "AURORA", "label": "AURORA (CC BY-SA 4.0)", "spdx": "CC-BY-SA-4.0",
               "url": "https://creativecommons.org/licenses/by-sa/4.0/", "noncommercial": false },
  "inchikey": "<InChIKey>", "inchi": "<InChI>", "canonical_smiles": "<SMILES>",
  "preferred_name": "<string>", "formula": "<string>",
  "is_complete": true, "qc_status": "passed",
  "descriptors": { "molecular_weight": "<number>", "logp": "<number>", "tpsa": "<number>",
                   "num_h_donors": "<integer>", "num_h_acceptors": "<integer>", "qed": "<number>", "sascore": "<number>" },
  "scores": { "lipinski_violations": "<integer>", "veber_pass": true, "pains_hit": false, "brenk_hit": false, "nih_hit": false },
  "sources": [ "..." ], "names": [ "..." ], "structure_files": [ "..." ],
  "scaffold": { "...": "..." }, "classification": [ "..." ],
  "truncated": { "...": "..." }
}
```

The record is bounded: long lists are cut to their first rows, and `truncated` says which. `fields=a,b` keeps
only the top-level fields you name (`alchemia_id` and `license` always stay); `include=features,structures`
adds the answers of those sub-resources under `included`. An AURORA-NC compound carries
`"package": "AURORA-NC"`, `"spdx": "CC-BY-NC-4.0"` and `"noncommercial": true`, and an account without NC
access is answered 404 for it, as for a compound that does not exist.

### A listing, filtered on the server

```bash
curl -s -H "Authorization: Bearer $AURORA_TOKEN" \
  "https://aurora.alchemia.solutions/v1/compounds?limit=100&max_mw=500&max_logp=5&veber_pass=true&has_sdf=true"
```

```json
{
  "items": [ { "alchemia_id": "ALC<n>", "license": { "...": "..." }, "molecular_weight": "<number>", "...": "..." } ],
  "has_more": true,
  "next_cursor": "<opaque string>"
}
```

Pass `next_cursor` back as `cursor` until `has_more` is false. Items have the shape of a search hit without
the match fields. `GET /v1/collections/{slug}/compounds` takes the same filters inside one collection.
`GET /v1/compounds/batch?ids=ALC1,ALC2` returns `items` (up to 50 ids per call, in the order asked) and
`not_found`, the ids your account is not served.

### Sub-resources

```bash
curl -s -H "Authorization: Bearer $AURORA_TOKEN" "https://aurora.alchemia.solutions/v1/compounds/ALC1/features"
```

```json
{
  "alchemia_id": "ALC1",
  "license": { "...": "..." },
  "descriptor_version": "<string>", "values_2d": { "...": "..." }, "values_3d": { "...": "..." },
  "admet_model_version": "<string>",
  "admet_profile": { "admet_hERG": "<number>", "admet_AMES": "<number>", "...": "..." },
  "fingerprint_version": "<string>"
}
```

`admet_profile` holds the ADMET-AI predictions keyed by task; they are predictions, never measurements.
`.../structure.sdf` returns the 3D SDF exactly as stored (`chemical/x-mdl-sdfile`). Its strong `ETag` is the
SHA-256 of the body, `If-None-Match` answers 304, and `?v=<sha256>` gives an address that can be cached for
good.

## Collections and sources

```bash
curl -s -H "Authorization: Bearer $AURORA_TOKEN" "https://aurora.alchemia.solutions/v1/collections?top_level=true"
```

```json
{
  "items": [
    {
      "slug": "natural-space", "name": "<string>", "type": "thematic",
      "description": "<string>", "criteria": "<the rule that decides membership>",
      "status": "ready", "availability": "available",
      "compound_count": "<integer>", "compound_count_cc_by_nc": "<integer>",
      "licenses": [ { "package": "AURORA", "spdx": "CC-BY-SA-4.0", "compound_count": "<integer>", "...": "..." } ],
      "parent_slug": null, "subcollections": [ "<slug>" ],
      "release_version": "<string>", "measured_at": "<timestamp>"
    }
  ],
  "has_more": false,
  "next_cursor": null
}
```

Collections overlap, and a parent holds the union of its subcollections, so their counts do not add up.
`GET /v1/sources/attribution` returns, for every source, `display_name`, `licence`, `licence_url`, `package`,
`attribution_text` and `terms`: the text to credit when you publish.

## Files, bioactivity and the account (session only)

These routes need the signed-in session of the platform; an API key is refused with
`403 api_key_not_allowed`. An item of `GET /v1/bundles` looks like this:

```json
{
  "id": "<bundle id>", "name": "<string>",
  "collection": "<collection slug>", "package": "nc", "kind": "descriptors", "format": "tar.zst",
  "compounds": "<integer>", "bytes": "<integer>",
  "license": { "spdx": "CC-BY-NC-4.0", "label": "<string>", "url": "https://creativecommons.org/licenses/by-nc/4.0/",
               "noncommercial": true, "scope": "all-rows", "per_row_file": "license_per_row.tsv" },
  "attribution": [ { "key": "<source key>", "name": "<string>", "text": "<string>" } ],
  "availability": "available", "legal_review": "approved",
  "can_download": true
}
```

`GET /v1/bundles/{bundle_id}/download` then returns a short-lived signed `url` with the `sha256` and `bytes`
of the archive. What the archives hold and how to check them: [USING_THE_DATA.md](USING_THE_DATA.md).

## Route table

"API key" is from the allow-list in the platform code (2026-11-25); rows marked "checked" were called with a
key in production on 2026-11-25.

### Routes that need no token

| Route | What it returns |
|---|---|
| `GET /v1/public/summary` | Aggregates behind the public Home. It holds no compound |
| `GET /health/live`, `GET /health/ready` | The health probes. Not exposed on the public address (404 there, 2026-11-25) |
| `POST /v1/auth/login`, `POST /v1/auth/register`, `POST /v1/auth/forgot-password`, `POST /v1/auth/reset-password`, `POST /v1/auth/reset-password/check`, `POST /v1/auth/confirm-email`, `POST /v1/auth/email-change/confirm`, `POST /v1/auth/resend-confirmation`, `POST /v1/auth/session/refresh`, `POST /v1/auth/session/logout` | The sign-in doors of an account, with a few more of the same kind in the contract |
| `GET /v1/auth/providers`, `GET /v1/auth/password-policy`, `GET /v1/auth/oauth/{provider}/authorize` and `/callback` | Which sign-in methods work, the password rules, and the OAuth steps |

### Routes that need a Bearer token

| Route | What it does | API key |
|---|---|---|
| `GET /v1/search/text?q=...` | Search by identifier, name or synonym. Optional: `limit`, `availability`, `sources`, `space`, `fields`, property bounds | yes, checked |
| `POST /v1/search/substructure` | SMARTS substructure search. Body: `smarts` (required, at most 500 characters), `limit`, `availability`, `use_chirality`, `sources`, `space`. Off in production on 2026-11-25: 503 `substructure_search_unavailable` | yes |
| `POST /v1/search/similarity` | Tanimoto similarity, Morgan radius 2, 2048 bits. Body: `smiles` (required), `min_similarity` (0.1 to 1, default 0.7), `limit`, `availability`, `sources`, `space`. Off in production on 2026-11-25: 503 `similarity_search_unavailable` | yes |
| `GET /v1/compounds`, `GET /v1/compounds/batch?ids=...` | Listing with keyset cursors and server-side filters, and a summary of up to 50 ids | yes |
| `GET /v1/compounds/{alchemia_id}` | The record of one compound | yes, checked |
| `GET /v1/compounds/{alchemia_id}/features`, `.../fingerprints`, `.../protonation-variants`, `.../provenance`, `.../external-ids`, `.../structures`, `.../structure.sdf`, `.../structure.svg`, `.../structure2d.json` | Sub-resources of one compound | yes |
| `GET /v1/compounds/{alchemia_id}/activities`, `GET /v1/compounds/{alchemia_id}/bioactivity` | Bioactivity rows of a compound. On in production (2026-11-25) for the signed-in session | `bioactivity`: no, checked. `activities`: yes, checked |
| `GET /v1/id-history/{alchemia_id}` | The old-to-new map of the renumbering of release 2.0.0 | no |
| `GET /v1/collections`, `GET /v1/collections/{slug}`, `.../compounds`, `.../sources` | The collections, one collection, its compounds and its sources | yes (`/v1/collections` checked) |
| `GET /v1/catalog/stats` | Catalog statistics | yes |
| `GET /v1/dashboard/collections`, `licenses`, `sources`, `admet`, `clinical-phases` | Aggregates for the Dashboard. The contract calls them anonymous behind a flag | yes |
| `GET /v1/sources`, `GET /v1/sources/attribution`, `GET /v1/sources/{source_key}` | The sources shown, with attribution | yes |
| `GET /v1/compounds/{alchemia_id}/download/{kind}`, `GET /v1/compounds/{alchemia_id}/file/{file_format}` | One file of one compound as a download | no |
| `GET /v1/compounds/{alchemia_id}/package` | The signed link of the `.zip` package of one compound. Behind `INDIVIDUAL_PACKAGES_ENABLED`, on in production on 2026-11-25 | no, checked |
| `GET /v1/capabilities` | What this deployment can offer to the current session | no |
| `GET /v1/bundles`, `GET /v1/bundles/{bundle_id}/download` | The bundles of the release by collection and package, and the signed link of one. The NC access is needed for an NC bundle | no, checked |
| `GET /v1/collections/{slug}/bundles`, `.../bundles/formats`, `.../bundles/{bundle_id}/download` | The bundles of one collection, its download formats and their state, and the signed link of one | list and formats: yes; download: no |
| `GET /v1/nc/collections`, `GET /v1/nc/compounds` | The AURORA-NC package: the count per collection and the list of compounds. They need an approved account with the NC access | no |
| `GET /v1/auth/me` | Who the token belongs to, its scopes and expiry | yes |
| `/v1/account/*` | Your own account | no, checked |
| `/v1/collaborate/*` | Register a study, request a database, send a published work | no |
| `GET /v1/account/api-keys`, `POST /v1/account/api-keys`, `POST /v1/account/api-keys/{key_id}/revoke` | Your API keys: list, create, revoke | no |
| `/v1/account/consent`, `/v1/account/nc-terms`, `/v1/account/export`, `/v1/account/erase`, `/v1/account/delete` | Your acceptances, your NC terms, a copy of your data, and its erasure | no |
| `POST /v1/auth/email-change`, `GET /v1/auth/security-summary`, `POST /v1/auth/session/logout-all` | Change the e-mail, see your sessions, sign out everywhere | no |
| `GET /v1/social/profile`, `PUT /v1/social/profile`, `GET /v1/social/people/{ref}`, `GET /v1/social/ranking` | The contributor profile and the Contributors Ranking | no |
| `GET /v1/pipeline/stats` | The curation funnel of one release per gate. Off in production on 2026-11-25: 404 | yes |

The `/v1/admin/*` routes are for the operators of the platform and are not part of a consumer's use.

## Behaviour to expect

- The public compound identifier is `alchemia_id`, of the form `ALC<n>`. Internal keys and raw identifiers
  of third-party records never appear.
- Listings are cursor based (`items`, `has_more`, `next_cursor`). The search routes answer `items` and
  `truncated`.
- Every compound answer carries its `license`: the package it belongs to.
- Only compounds of the two packages are served. Any other is answered as a compound that does not exist.

## Examples

In [`examples/python/`](../examples/python/): `aurora_client.py` (a small client with cursors, retry on 429
and errors with `request_id`), `filter_compounds.py`, `docking_set.py` and `read_api.py`; in
[`examples/curl/`](../examples/curl/): `read_api.sh`. All of them only read.
