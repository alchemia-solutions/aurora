# Quickstart

[Repository home](../README.md) · [Docs index](README.md)

From an account to your first API call. Everything on this page was checked against the platform in production
(version 1.5.2) on 2026-11-25 with an approved test account. The platform is a closed beta: an administrator
approves each account before it can read compounds.

## 1. Create an account and wait for approval

1. Open <https://aurora.alchemia.solutions/enter> and choose **Sign Up**.
2. Accept the Terms of Use and the Privacy Policy (version 1.1). Accepting them at sign-up also opens the
   AURORA-NC package (non-commercial use only) to your account.
3. Your account is created pending. No confirmation link is sent: an administrator reviews the request.
4. When the account is approved you receive an e-mail from `contact@alchemia.solutions` with a button to log in.

Without an approved account only the Home page and the sign-in page open. The collections, the Explorer, the
Dashboard, Collaborate, Documents and your Profile all ask you to sign in.

## 2. Create an API key

Sign in, open **Profile** and create a key. A key:

- starts with `aurk_`, and the whole key is shown **once**, when it is created. Store it like a password;
- lasts 7, 30, 90 or 365 days (30 by default), and an account holds at most 5 active keys;
- **only reads**: it can search and read compounds (record, features, fingerprints, provenance, structures and
  activity rows), collections and sources. It cannot download files, read the `/bioactivity` view, send forms or
  change the account. Those need the signed-in session of the platform;
- can be revoked at any time from the same page. A revoked or expired key is refused.

Send it in the `Authorization` header, never in a URL:

```bash
export AURORA_TOKEN="aurk_..."   # your key
```

## 3. Your first calls

```bash
BASE=https://aurora.alchemia.solutions

# Search by name, identifier or synonym
curl -s -H "Authorization: Bearer $AURORA_TOKEN" "$BASE/v1/search/text?q=caffeine&limit=5"

# One compound, by its public identifier
curl -s -H "Authorization: Bearer $AURORA_TOKEN" "$BASE/v1/compounds/ALC1"

# Its 3D structure as SDF
curl -s -H "Authorization: Bearer $AURORA_TOKEN" "$BASE/v1/compounds/ALC1/structure.sdf" -o ALC1.sdf

# The collections
curl -s -H "Authorization: Bearer $AURORA_TOKEN" "$BASE/v1/collections"
```

The public identifier of a compound is `alchemia_id`, of the form `ALC<n>`. Every compound answer carries its
`license`, the package it belongs to.

## 4. Walk a listing

Listings use cursors. Ask for a page, then pass `next_cursor` back until `has_more` is false:

```python
import os, requests

BASE = "https://aurora.alchemia.solutions"
s = requests.Session()
s.headers["Authorization"] = f"Bearer {os.environ['AURORA_TOKEN']}"

params = {"limit": 100}
while True:
    page = s.get(f"{BASE}/v1/compounds", params=params, timeout=30)
    page.raise_for_status()
    body = page.json()
    for item in body["items"]:
        print(item["alchemia_id"])
    if not body["has_more"]:
        break
    params["cursor"] = body["next_cursor"]
```

## 5. Limits and errors

- **Rate limit:** 60 requests per 60 seconds per address, shared by every key of the account. Over the limit the
  API answers `429` with a `Retry-After` header: wait that many seconds and try again.
- **Errors** come back as a problem document with `code`, `message` and `request_id`. Quote the `request_id`
  when you report a problem.

| Status | Usual `code` | Meaning |
|---|---|---|
| 401 | | No token, or a token that is invalid or expired |
| 403 | `api_key_not_allowed` | The route needs the signed-in session, not an API key (downloads, the `/bioactivity` view, account) |
| 404 | `not_found` | No such compound for your account. An NC compound is answered this way to an account without NC access |
| 429 | | Rate limited. Read `Retry-After` |
| 503 | `similarity_search_unavailable`, `substructure_search_unavailable` | The search is not turned on in this deployment |

## 6. Download the data

Files are not handed to API keys. Sign in on the platform and open a collection: its **Downloads** section
(`#downloads`) lists the bundles of the AURORA package (CC BY-SA 4.0) and of the AURORA-NC package
(CC BY-NC 4.0). Each download is a short-lived signed link. The Explorer also has a **Download Data** button for
one compound. What a bundle holds and how to cite it: [Packages](../README.md#packages) and
[Licence](../README.md#licence). How to check and open a bundle: [USING_THE_DATA.md](USING_THE_DATA.md).

## What this deployment offers today

Read on 2026-11-25 from production:

| Feature | State |
|---|---|
| Text search, compound record, structures, collections, sources | On |
| API keys (read only) | On |
| Bioactivity of a compound | On: `/activities` with a session or a key, `/bioactivity` with the session only |
| One-compound package (`/v1/compounds/{alchemia_id}/package`) | On, with the signed-in session only |
| Similarity search | Off: answers 503 |
| Substructure search | Off: answers 503 |
| Pipeline funnel (`/v1/pipeline/stats`) | Off: answers 404 |
| Public OpenAPI file and interactive reference | Not published |
| Health probes (`/health/*`) | Not exposed on the public address |

This table changes as the beta opens features. [CHANGELOG.md](../CHANGELOG.md) records each change with its date.
