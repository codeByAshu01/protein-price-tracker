"""Renders data/latest.json into a README.md price table."""

import os

README_PATH = os.path.join(os.path.dirname(__file__), "..", "README.md")

HEADER = """# Protein Price Tracker (India)

Daily-updated protein powder prices scraped from Indian D2C brand stores and
Nutrabay via a [GitHub Actions](.github/workflows/daily-price-check.yml) cron
job. Data sources and rationale: see [SOURCES.md](SOURCES.md).

**Last checked:** {checked_at}

Full history: [`data/history.csv`](data/history.csv) &middot; latest snapshot:
[`data/latest.json`](data/latest.json)

<details>
<summary>Run it yourself / add more sources</summary>

```bash
pip install -r requirements.txt
python -m scraper.main
```

Add or remove sites in [`scraper/config.py`](scraper/config.py) — Shopify D2C
brands just need a store URL added to `SHOPIFY_STORES`, no code changes.
See [SOURCES.md](SOURCES.md) for why each current source was chosen (and
why Amazon/Flipkart/HealthKart/BigBasket aren't scraped).

</details>

---
"""


def _fmt_price(v):
    return f"₹{v:,.0f}" if v is not None else "-"


def _fmt_pct(v):
    return f"{v:.0f}%" if v is not None else "-"


def _fmt_per100g(v):
    return f"₹{v:.2f}" if v is not None else "-"


def render_readme(items, checked_at):
    by_source = {}
    for item in items:
        by_source.setdefault(item["source"], []).append(item)

    lines = [HEADER.format(checked_at=checked_at)]

    for source in sorted(by_source):
        source_items = sorted(by_source[source], key=lambda x: (x["price"] is None, x["price"]))
        lines.append(f"## {source}\n")
        lines.append("| Product | MRP | Price | Discount | ₹/100g (pack) | Stock | Link |")
        lines.append("|---|---:|---:|---:|---:|:---:|---|")
        for item in source_items:
            stock = "✅" if item["in_stock"] else "❌"
            name = item["name"].replace("|", "-")
            lines.append(
                f"| {name} | {_fmt_price(item['mrp'])} | {_fmt_price(item['price'])} | "
                f"{_fmt_pct(item['discount_pct'])} | {_fmt_per100g(item['price_per_100g'])} | "
                f"{stock} | [view]({item['url']}) |"
            )
        lines.append("")

    lines.append(
        "\n*₹/100g is price per 100g of product weight, not per gram of protein "
        "(macros aren't available from these feeds). Prices are snapshots at "
        "check time and may have changed since — always verify on the retailer's site.*\n"
    )

    with open(README_PATH, "w") as f:
        f.write("\n".join(lines))
