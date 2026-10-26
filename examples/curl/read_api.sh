#!/usr/bin/env bash
# Read-only calls to the public AURORA API. Licensed under Apache-2.0 (LICENSE-CODE).
#
#   export AURORA_TOKEN=<your beta invitation token>
#   bash examples/curl/read_api.sh
#
# The API answers in closed beta: without a token, /v1/ answers 401.
set -euo pipefail

BASE_URL="${AURORA_BASE_URL:-https://aurora.alchemia.solutions}"
AUTH=()
if [[ -n "${AURORA_TOKEN:-}" ]]; then
  AUTH=(-H "Authorization: Bearer ${AURORA_TOKEN}")
fi

echo "== catalog stats"
curl -sS --max-time 30 "${AUTH[@]}" "${BASE_URL}/v1/catalog/stats"; echo

echo "== collections"
curl -sS --max-time 30 "${AUTH[@]}" "${BASE_URL}/v1/collections"; echo

echo "== text search"
curl -sS --max-time 30 "${AUTH[@]}" "${BASE_URL}/v1/search/text?q=quercetin&limit=5"; echo

echo "== substructure (benzene ring)"
curl -sS --max-time 30 "${AUTH[@]}" -X POST -H "Content-Type: application/json" \
  -d '{"smarts":"c1ccccc1","limit":5}' "${BASE_URL}/v1/search/substructure"; echo

echo "== similarity (ethanol)"
curl -sS --max-time 30 "${AUTH[@]}" -X POST -H "Content-Type: application/json" \
  -d '{"smiles":"CCO","min_similarity":0.9,"limit":5}' "${BASE_URL}/v1/search/similarity"; echo
