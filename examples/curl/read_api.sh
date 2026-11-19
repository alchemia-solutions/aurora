#!/usr/bin/env bash
# Read-only calls to the AURORA API, following the OpenAPI contract of platform version 1.4.0 (closed beta).
# Licensed under Apache-2.0 (LICENSE-CODE).
#
#   export AURORA_TOKEN=<a token from your approved account>   # for every route except the first
#   bash examples/curl/read_api.sh
#
# Open route (no token): /v1/public/summary. Routes with a Bearer token: /v1/catalog/stats, /v1/collections,
# /v1/search/text. See docs/API.md. The platform is a closed beta and no package is published.
set -euo pipefail

BASE_URL="${AURORA_BASE_URL:-https://aurora.alchemia.solutions}"
AUTH=()
if [[ -n "${AURORA_TOKEN:-}" ]]; then
  AUTH=(-H "Authorization: Bearer ${AURORA_TOKEN}")
fi

echo "== public summary (no token)"
curl -sS --max-time 30 "${BASE_URL}/v1/public/summary"; echo

echo "== catalog stats (Bearer token)"
curl -sS --max-time 30 "${AUTH[@]}" "${BASE_URL}/v1/catalog/stats"; echo

echo "== collections (Bearer token)"
curl -sS --max-time 30 "${AUTH[@]}" "${BASE_URL}/v1/collections?limit=10"; echo

echo "== text search (Bearer token)"
curl -sS --max-time 30 "${AUTH[@]}" "${BASE_URL}/v1/search/text?q=quercetin&limit=5"; echo
