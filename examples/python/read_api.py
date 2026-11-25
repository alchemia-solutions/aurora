#!/usr/bin/env python3
"""Read-only calls to the AURORA API, checked against platform version 1.5.2 in production on 2026-11-25 (closed beta).

    pip install requests
    export AURORA_TOKEN=<an API key (aurk_...) created in Profile of your approved account>   # for every route except the first
    python examples/python/read_api.py

Open route (no token): /v1/public/summary. Routes with a Bearer token: /v1/catalog/stats, /v1/collections,
/v1/search/text, /v1/compounds/{alchemia_id}. See docs/API.md. The platform is a closed beta and no package is
published.
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
    # The one open route of the closed beta: aggregates, no compound.
    show("public summary", s.get(f"{BASE_URL}/v1/public/summary", timeout=TIMEOUT_SECONDS))

    # Routes with a Bearer token.
    show("catalog stats", s.get(f"{BASE_URL}/v1/catalog/stats", timeout=TIMEOUT_SECONDS))
    show("collections", s.get(f"{BASE_URL}/v1/collections", params={"limit": 10}, timeout=TIMEOUT_SECONDS))
    hits = show(
        "text search",
        s.get(f"{BASE_URL}/v1/search/text", params={"q": "quercetin", "limit": 5}, timeout=TIMEOUT_SECONDS),
    )
    if hits and hits.get("items"):
        alchemia_id = hits["items"][0]["alchemia_id"]
        show(f"compound {alchemia_id}", s.get(f"{BASE_URL}/v1/compounds/{alchemia_id}", timeout=TIMEOUT_SECONDS))
    return 0


if __name__ == "__main__":
    sys.exit(main())
