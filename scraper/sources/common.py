"""Shared helpers used by every source module."""

import re

_SIZE_RE = re.compile(r"(\d+(?:\.\d+)?)[\s-]*(kg|g|gm|gms|grams?)\b", re.IGNORECASE)
# Numbers followed by these words are serving/dosage claims, not pack weight
# (e.g. "26g Protein/Scoop", "26g-protein-per-serving" in slugs) - never
# trust them as size. Separator may be whitespace (titles) or "-" (slugs).
_SERVING_CONTEXT_RE = re.compile(r"^[\s-]*(protein|bcaa|scoop|serving|dose|per\b)", re.IGNORECASE)


def extract_size_g(*texts):
    """Best-effort extraction of pack size in grams from product title/variant text.

    Scans every provided text for weight-like tokens, discards ones that read
    as a per-serving/dosage claim rather than total pack weight, and returns
    the largest remaining value (pack size is almost always the largest
    weight mentioned; serving sizes are smaller).
    """
    candidates = []
    for text in texts:
        if not text:
            continue
        for m in _SIZE_RE.finditer(text):
            trailing = text[m.end():m.end() + 20]
            if _SERVING_CONTEXT_RE.match(trailing):
                continue
            value = float(m.group(1))
            unit = m.group(2).lower()
            candidates.append(value * 1000 if unit == "kg" else value)
    return max(candidates) if candidates else None


def make_item(source, name, brand, mrp, price, url, in_stock=True, size_hint="", size_g_override=None):
    size_g = size_g_override if size_g_override else extract_size_g(name, size_hint)
    discount_pct = None
    if mrp and price and mrp > 0 and mrp >= price:
        discount_pct = round((1 - price / mrp) * 100, 1)
    price_per_100g = round(price / size_g * 100, 2) if size_g and price else None
    # Sanity clamp: real protein powder runs roughly ₹30-3000/100g in India.
    # Anything outside that points to bad source metadata (e.g. a Shopify
    # "grams" field set to shipping weight, not content weight) rather than
    # a genuine price - better to show nothing than a misleading number.
    if price_per_100g is not None and not (30 <= price_per_100g <= 3000):
        price_per_100g = None
    return {
        "source": source,
        "name": name.strip() if name else name,
        "brand": brand,
        "mrp": mrp,
        "price": price,
        "discount_pct": discount_pct,
        "size_g": size_g,
        "price_per_100g": price_per_100g,
        "url": url,
        "in_stock": in_stock,
    }
