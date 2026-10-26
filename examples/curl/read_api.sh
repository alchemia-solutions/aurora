#!/usr/bin/env bash
# Read-only calls to the AURORA API. Licensed under Apache-2.0 (LICENSE-CODE).
#
#   export AURORA_TOKEN=<a token from your approved account>   # only for the routes that need one
#   bash examples/curl/read_api.sh
#
# Open routes (no token, when the v1.3 release is live): /v1/public/summary, /v1/catalog/stats, /v1/collections.
# Routes with a Bearer token: /v1/search/*. See docs/API.md.
set -euo pipefail

BASE_URL="${AURORA_BASE_URL:-https://aurora.alchemia.solutions}"
AUTH=()
if [[ -n "${AURORA_TOKEN:-}" ]]; then
  AUTH=(-H "Authorization: Bearer ${AURORA_TOKEN}")
fi

echo "== public summary (open)"
curl -sS --max-time 30 "${BASE_URL}/v1/public/summary"; echo

echo "== catalog stats (open)"
curl -sS --max-time 30 "${BASE_URL}/v1/catalog/stats"; echo

echo "== collections (open)"
curl -sS --max-time 30 "${BASE_URL}/v1/collections?limit=10"; echo

echo "== text search (Bearer token)"
curl -sS --max-time 30 "${AUTH[@]}" "${BASE_URL}/v1/search/text?q=quercetin&limit=5"; echo

echo "== substructure, benzene ring (Bearer token)"
curl -sS --max-time 30 "${AUTH[@]}" -X POST -H "Content-Type: application/json" \
  -d '{"smarts":"c1ccccc1","limit":5}' "${BASE_URL}/v1/search/substructure"; echo

echo "== similarity, ethanol (Bearer token)"
curl -sS --max-time 30 "${AUTH[@]}" -X POST -H "Content-Type: application/json" \
  -d '{"smiles":"CCO","min_similarity":0.9,"limit":5}' "${BASE_URL}/v1/search/similarity"; echo
