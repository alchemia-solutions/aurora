#!/usr/bin/env python3
"""A small read-only client for the AURORA API.

    pip install requests
    export AURORA_TOKEN=aurk_...      # an API key created in Profile of your approved account

    from aurora_client import AuroraClient, AuroraError
    client = AuroraClient()
    record = client.get("/v1/compounds/ALC1")
    for item in client.paginate("/v1/compounds", {"max_mw": 500, "limit": 100}):
        ...

What it does, and nothing more:
  * reads the token from AURORA_TOKEN and sends it only in the Authorization header, never in a URL;
  * refuses a plain http:// address except on localhost, so the token never travels unencrypted;
  * on 429 waits the seconds of Retry-After (or a short back-off when the header is missing) and tries again;
  * walks cursor listings (items, has_more, next_cursor);
  * turns an error answer into AuroraError with its status, code, message and request_id. Quote the
    request_id when you report a problem.

It never writes to the API. Shapes of the answers: docs/API.md. Checked against the OpenAPI contract of
platform version 1.5.2 (read 2026-11-25); the production behaviour it relies on (API keys, cursors, 429 with
Retry-After, the error envelope) is the one docs/QUICKSTART.md records for 2026-11-25.
Licensed under Apache-2.0 (LICENSE-CODE).
"""
from __future__ import annotations

import email.utils
import os
import time
from datetime import datetime, timezone
from typing import Any, Iterator
from urllib.parse import urlparse

import requests

DEFAULT_BASE_URL = "https://aurora.alchemia.solutions"
LOCAL_HOSTS = {"localhost", "127.0.0.1", "::1"}
BATCH_MAX_IDS = 50  # GET /v1/compounds/batch takes at most 50 ids (OpenAPI contract 1.5.2)


class AuroraError(Exception):
    """An error answer of the API: the problem document's code, message and request_id."""

    def __init__(self, status: int, code: str | None, message: str, request_id: str | None) -> None:
        self.status = status
        self.code = code
        self.message = message
        self.request_id = request_id
        where = f" (request_id {request_id})" if request_id else ""
        label = f" {code}" if code else ""
        super().__init__(f"HTTP {status}{label}: {message}{where}")


def _retry_after_seconds(value: str | None) -> float | None:
    """Retry-After is either a number of seconds or an HTTP date (RFC 9110). None when absent or unreadable."""
    if not value:
        return None
    value = value.strip()
    if value.isdigit():
        return float(value)
    try:
        when = email.utils.parsedate_to_datetime(value)
    except (TypeError, ValueError):
        return None
    if when.tzinfo is None:
        when = when.replace(tzinfo=timezone.utc)
    return max(0.0, (when - datetime.now(timezone.utc)).total_seconds())


def _error_from(response: requests.Response) -> AuroraError:
    code = message = request_id = None
    try:
        body = response.json()
    except ValueError:
        body = None
    if isinstance(body, dict):
        nested = body.get("error") if isinstance(body.get("error"), dict) else {}
        code = body.get("code") or nested.get("code")
        message = nested.get("message") or body.get("detail") or body.get("title")
        request_id = body.get("request_id") or nested.get("request_id")
    request_id = request_id or response.headers.get("X-Request-ID")
    return AuroraError(response.status_code, code, message or response.reason or "error", request_id)


class AuroraClient:
    def __init__(
        self,
        token: str | None = None,
        base_url: str | None = None,
        timeout: float = 30.0,
        max_retries: int = 5,
        max_wait_seconds: float = 120.0,
    ) -> None:
        self.base_url = (base_url or os.environ.get("AURORA_BASE_URL") or DEFAULT_BASE_URL).rstrip("/")
        parsed = urlparse(self.base_url)
        if parsed.scheme != "https" and not (parsed.scheme == "http" and parsed.hostname in LOCAL_HOSTS):
            raise ValueError(f"refusing to send a token to {self.base_url}: use https")
        token = token if token is not None else os.environ.get("AURORA_TOKEN")
        if not token:
            raise ValueError("set AURORA_TOKEN to an API key of your approved account (see docs/QUICKSTART.md)")
        self.timeout = timeout
        self.max_retries = max_retries
        self.max_wait_seconds = max_wait_seconds
        self.session = requests.Session()
        self.session.headers["Authorization"] = f"Bearer {token}"
        self.session.headers["User-Agent"] = "aurora-public-examples"

    def request(self, method: str, path: str, **kwargs: Any) -> requests.Response:
        """One call, repeated on 429 after Retry-After. Any other status of 400 or more raises AuroraError."""
        url = f"{self.base_url}{path}"
        attempt = 0
        while True:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)
            if response.status_code != 429 or attempt >= self.max_retries:
                break
            wait = _retry_after_seconds(response.headers.get("Retry-After"))
            if wait is None:
                wait = min(2.0 ** attempt, 30.0)
            wait = min(wait, self.max_wait_seconds)
            attempt += 1
            print(f"   rate limited, waiting {wait:.0f} s (attempt {attempt} of {self.max_retries})")
            time.sleep(wait)
        if response.status_code >= 400:
            raise _error_from(response)
        return response

    def get(self, path: str, params: dict[str, Any] | None = None) -> Any:
        return self.request("GET", path, params=params).json()

    def get_bytes(self, path: str, params: dict[str, Any] | None = None) -> tuple[bytes, requests.structures.CaseInsensitiveDict]:
        response = self.request("GET", path, params=params)
        return response.content, response.headers

    def paginate(self, path: str, params: dict[str, Any] | None = None) -> Iterator[dict[str, Any]]:
        """Every item of a cursor listing: pass next_cursor back until has_more is false."""
        params = dict(params or {})
        while True:
            page = self.get(path, params)
            yield from page.get("items", [])
            if not page.get("has_more") or not page.get("next_cursor"):
                return
            params["cursor"] = page["next_cursor"]

    def batch(self, ids: list[str], fields: str | None = None) -> tuple[list[dict[str, Any]], list[str]]:
        """Summaries of many compounds, BATCH_MAX_IDS per call. Returns (found, not_found)."""
        found: list[dict[str, Any]] = []
        missing: list[str] = []
        for start in range(0, len(ids), BATCH_MAX_IDS):
            params: dict[str, Any] = {"ids": ",".join(ids[start:start + BATCH_MAX_IDS])}
            if fields:
                params["fields"] = fields
            page = self.get("/v1/compounds/batch", params)
            found.extend(page.get("items", []))
            missing.extend(page.get("not_found", []))
        return found, missing


def read_ids(path: str | None, inline: list[str] | None) -> list[str]:
    """alchemia_id values from a file (one per line, # comments allowed) and from the command line, once each, in order."""
    raw: list[str] = list(inline or [])
    if path:
        with open(path, encoding="utf-8") as handle:
            raw.extend(line.split("#", 1)[0].strip() for line in handle)
    seen: set[str] = set()
    ids: list[str] = []
    for value in raw:
        value = value.strip().upper()
        if value and value not in seen:
            seen.add(value)
            ids.append(value)
    return ids
