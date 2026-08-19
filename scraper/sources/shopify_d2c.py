"""D2C brand source: reads each store's public Shopify /products.json feed.

This is a standard endpoint Shopify exposes on every store by default -
not a scraping workaround, and near-real-time since it reflects live
storefront pricing/stock.
"""

import requests

from ..config import (
    EXCLUDE_KEYWORDS,
    PROTEIN_KEYWORDS,
    REQUEST_TIMEOUT,
    SHOPIFY_STORES,
    USER_AGENT,
)
from .common import make_item


def _is_protein_product(title, product_type, tags):
    haystack = " ".join([title or "", product_type or "", " ".join(tags or [])]).lower()
    if any(kw in haystack for kw in EXCLUDE_KEYWORDS):
        return False
    return any(kw in haystack for kw in PROTEIN_KEYWORDS)


def _fetch_store(brand, base_url, session):
    items = []
    page = 1
    while page <= 3:  # a few pages is plenty for a daily digest
        url = f"{base_url}/products.json?limit=250&page={page}"
        resp = session.get(url, timeout=REQUEST_TIMEOUT)
        if resp.status_code != 200:
            break
        products = resp.json().get("products", [])
        if not products:
            break

        for p in products:
            if not _is_protein_product(p.get("title"), p.get("product_type"), p.get("tags")):
                continue
            for v in p.get("variants", []):
                price = float(v["price"]) if v.get("price") else None
                if not price:  # skips None and free/₹0 sample & giveaway variants
                    continue
                mrp = float(v["compare_at_price"]) if v.get("compare_at_price") else price
                items.append(
                    make_item(
                        source=brand,
                        name=f"{p.get('title', 'Unknown')} ({v.get('title')})"
                        if v.get("title") and v.get("title") != "Default Title"
                        else p.get("title", "Unknown"),
                        brand=p.get("vendor", brand),
                        mrp=mrp,
                        price=price,
                        url=f"{base_url}/products/{p.get('handle', '')}",
                        in_stock=bool(v.get("available")),
                        size_g_override=v.get("grams") or None,
                    )
                )
        page += 1

    return items


def fetch():
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})

    items = []
    for brand, base_url in SHOPIFY_STORES.items():
        try:
            items.extend(_fetch_store(brand, base_url, session))
        except Exception as exc:  # noqa: BLE001 - keep the daily run alive
            print(f"[shopify_d2c] {brand} failed: {exc}")
            continue

    return items
