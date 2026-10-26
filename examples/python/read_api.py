#!/usr/bin/env python3
"""Read-only calls to the AURORA API.

    pip install requests
    export AURORA_TOKEN=<a token from your approved account>   # only for the routes that need one
    python examples/python/read_api.py

Open routes (no token, when the v1.3 release is live): /v1/public/summary, /v1/catalog/stats, /v1/collections.
Routes with a Bearer token: /v1/search/*, /v1/compounds/{alchemia_id}. See docs/API.md.
Licensed under Apache-2.0 (LICENSE-CODE).
"""
from __future__ import annotations

import json
import os
import sys

import requests

BASE_URL = os.environ.get("AURORA_BASE_URL", "https://aurora.alchemia.solutions")
TIMEOUT_SECONDS = 30


def session() -> requests.Session:
    s = requests.Session()
    key = os.environ.get("AURORA_TOKEN")
    if key:
        s.headers["Authorization"] = f"Bearer {key}"
    return s


def show(title: str, response: requests.Response) -> dict | None:
    print(f"== {title}: HTTP {response.status_code}")
    if response.status_code == 401:
        print("   This route needs a Bearer token from an approved account (AURORA_TOKEN).")
        return None
    response.raise_for_status()
    body = response.json()
    print(json.dumps(body, indent=2)[:1200])
    return body


def main() -> int:
    s = session()
    # Open routes: no token needed once the v1.3 release is live.
    show("public summary", s.get(f"{BASE_URL}/v1/public/summary", timeout=TIMEOUT_SECONDS))
    show("catalog stats", s.get(f"{BASE_URL}/v1/catalog/stats", timeout=TIMEOUT_SECONDS))
    show("collections", s.get(f"{BASE_URL}/v1/collections", params={"limit": 10}, timeout=TIMEOUT_SECONDS))

    # Routes with a Bearer token.
    hits = show(
        "text search",
        s.get(f"{BASE_URL}/v1/search/text", params={"q": "quercetin", "limit": 5}, timeout=TIMEOUT_SECONDS),
    )
    show(
        "substructure (benzene ring)",
        s.post(f"{BASE_URL}/v1/search/substructure", json={"smarts": "c1ccccc1", "limit": 5},
               timeout=TIMEOUT_SECONDS),
    )
    show(
        "similarity (ethanol)",
        s.post(f"{BASE_URL}/v1/search/similarity", json={"smiles": "CCO", "min_similarity": 0.9, "limit": 5},
               timeout=TIMEOUT_SECONDS),
    )
    if hits and hits.get("items"):
        alchemia_id = hits["items"][0]["alchemia_id"]
        show(f"compound {alchemia_id}", s.get(f"{BASE_URL}/v1/compounds/{alchemia_id}", timeout=TIMEOUT_SECONDS))
    return 0


if __name__ == "__main__":
    sys.exit(main())
