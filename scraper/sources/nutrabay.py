"""Nutrabay source: parses the server-rendered __NEXT_DATA__ JSON on search pages.

Respects robots.txt (nutrabay.com does not disallow /search).
"""

import json
import re
import urllib.parse

import requests

from ..config import NUTRABAY_QUERIES, REQUEST_TIMEOUT, USER_AGENT
from .common import make_item

NEXT_DATA_RE = re.compile(
    r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', re.S
)


def _fetch_search_results(query, session):
    url = f"https://www.nutrabay.com/search?q={urllib.parse.quote(query)}"
    resp = session.get(url, timeout=REQUEST_TIMEOUT)
    resp.raise_for_status()
    m = NEXT_DATA_RE.search(resp.text)
    if not m:
        return []
    data = json.loads(m.group(1))
    try:
        results = (
            data["props"]["pageProps"]["initialState"]["searchPage"]
            ["ProductSearchListing"]["data"]["results"]
        )
    except (KeyError, TypeError):
        return []
    return results


def fetch():
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT, "Accept-Language": "en-IN,en;q=0.9"})

    items = []
    seen_skus = set()
    for query in NUTRABAY_QUERIES:
        try:
            results = _fetch_search_results(query, session)
        except Exception as exc:  # noqa: BLE001 - keep the daily run alive
            print(f"[nutrabay] query '{query}' failed: {exc}")
            continue

        for r in results:
            sku = r.get("sku") or r.get("variant_slug")
            if not sku or sku in seen_skus:
                continue
            seen_skus.add(sku)

            price = r.get("discounted_price") or r.get("price")
            mrp = r.get("price")
            slug = r.get("slug", "")
            pid = r.get("pid", "")
            url = f"https://nutrabay.com/product/{slug}/?pId={pid}" if slug else "https://nutrabay.com/"

            items.append(
                make_item(
                    source="Nutrabay",
                    name=r.get("name", "Unknown"),
                    brand=r.get("brand", ""),
                    mrp=mrp,
                    price=price,
                    url=url,
                    in_stock=r.get("availability") == "instock",
                    size_hint=r.get("variant_slug", ""),
                )
            )

    return items
