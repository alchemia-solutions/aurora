#!/usr/bin/env python3
"""Read-only calls to the public AURORA API.

    pip install requests
    export AURORA_TOKEN=<your beta invitation token>
    python examples/python/read_api.py

The API answers in closed beta: without a token, /v1/ answers 401.
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


def show(title: str, response: requests.Response) -> None:
    print(f"== {title}: HTTP {response.status_code}")
    if response.status_code == 401:
        print("   The API is in closed beta and needs an invitation token (AURORA_TOKEN).")
        return
    response.raise_for_status()
    print(json.dumps(response.json(), indent=2)[:1500])


def main() -> int:
    s = session()
    show("catalog stats", s.get(f"{BASE_URL}/v1/catalog/stats", timeout=TIMEOUT_SECONDS))
    show("collections", s.get(f"{BASE_URL}/v1/collections", timeout=TIMEOUT_SECONDS))
    show(
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
    return 0


if __name__ == "__main__":
    sys.exit(main())
