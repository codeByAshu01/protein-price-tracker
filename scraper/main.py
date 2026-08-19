"""Entry point: fetch prices from every source, write data files, render README."""

import csv
import json
import os
from datetime import datetime
from zoneinfo import ZoneInfo

from .config import TOP_N_PER_SOURCE
from .render import render_readme
from .sources import nutrabay, shopify_d2c

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
IST = ZoneInfo("Asia/Kolkata")

SOURCES = [nutrabay, shopify_d2c]


def collect_items():
    items = []
    for module in SOURCES:
        fetched = module.fetch()
        print(f"[main] {module.__name__.split('.')[-1]}: {len(fetched)} items")
        items.extend(fetched)
    return items


def trim_per_source(items):
    by_source = {}
    for item in items:
        by_source.setdefault(item["source"], []).append(item)

    trimmed = []
    for source_items in by_source.values():
        source_items.sort(key=lambda x: (x["price"] is None, x["price"]))
        trimmed.extend(source_items[:TOP_N_PER_SOURCE])
    return trimmed


def write_latest(items, checked_at):
    os.makedirs(DATA_DIR, exist_ok=True)
    payload = {"checked_at": checked_at, "items": items}
    with open(os.path.join(DATA_DIR, "latest.json"), "w") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)


def append_history(items, checked_at):
    path = os.path.join(DATA_DIR, "history.csv")
    is_new = not os.path.exists(path)
    fieldnames = [
        "checked_at", "source", "brand", "name", "mrp", "price",
        "discount_pct", "price_per_100g", "in_stock", "url",
    ]
    with open(path, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if is_new:
            writer.writeheader()
        for item in items:
            row = {k: item.get(k) for k in fieldnames if k != "checked_at"}
            row["checked_at"] = checked_at
            writer.writerow(row)


def main():
    checked_at = datetime.now(IST).strftime("%Y-%m-%d %H:%M IST")
    items = collect_items()

    if not items:
        print("[main] no items fetched from any source, skipping data update")
        return

    items = trim_per_source(items)
    write_latest(items, checked_at)
    append_history(items, checked_at)
    render_readme(items, checked_at)
    print(f"[main] done: {len(items)} items written, checked at {checked_at}")


if __name__ == "__main__":
    main()
