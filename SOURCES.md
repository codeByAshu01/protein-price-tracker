# Data sources and why they were chosen

Before writing any scraper, each candidate site was checked for (a) whether
plain HTTP requests actually return usable data, and (b) whether `robots.txt`
permits fetching that URL. Sites that failed either check were excluded
rather than worked around.

| Site | Result | Included? |
|---|---|---|
| **Nutrabay** | `robots.txt` allows `/search`; search pages are server-rendered Next.js with a `__NEXT_DATA__` JSON blob containing full price/stock data. | ✅ |
| **Fast&Up, OZiva, Wellbeing Nutrition, Boldfit** | All run on Shopify, which exposes a public `/products.json` feed by default on every store — not a scraping workaround, an intentionally public endpoint. | ✅ |
| **Amazon.in** | Returns a bot-verification/CAPTCHA challenge page to plain HTTP requests; no reliable way to fetch prices without their paid/account-gated Product Advertising API. | ❌ (excluded — see below) |
| **Flipkart** | `robots.txt` explicitly disallows `/search?` and `/ps/` (product pages). | ❌ excluded to respect robots.txt |
| **HealthKart** | `robots.txt` disallows both `/search/` and `/p/` (product pages). The only page type with embedded price data is the disallowed search page; category pages are client-rendered with no price in the initial HTML. | ❌ excluded to respect robots.txt |
| **BigBasket** | `robots.txt` is permissive, but the page is fully client-rendered (Next.js) with no price data in the raw HTML — would require a headless browser (Playwright) to render JS. | ❌ excluded from v1 (see "Adding more sources" below) |

## Why not Amazon?

Reliable, ToS-compliant Amazon.in pricing requires the official **Product
Advertising API (PA-API)**, which needs your own free Amazon Associates
account and API keys — plus Amazon requires the account to generate a
minimum number of qualifying sales periodically to keep API access active.
That's a real (if not monetary) ongoing cost, so it was left out of v1 by
request. If you later want it added:

1. Sign up at [affiliate-program.amazon.in](https://affiliate-program.amazon.in/)
2. Request PA-API access from the Associates dashboard
3. Add `AMAZON_ACCESS_KEY`, `AMAZON_SECRET_KEY`, `AMAZON_PARTNER_TAG` as
   GitHub repo secrets
4. A new `scraper/sources/amazon.py` module can call PA-API's
   `SearchItems`/`GetItems` operations directly — no scraping involved.

## Adding more sources later

- **BigBasket**: would need `playwright` added to `requirements.txt` and the
  GitHub Actions job to install browser binaries (`playwright install
  chromium`) — heavier and slower, so deferred.
- **Flipkart Affiliate API**: same shape as the Amazon option above — free
  affiliate signup, official API, no scraping.
- **More Shopify D2C brands**: just add `"Brand Name": "https://store-url"`
  to `SHOPIFY_STORES` in `scraper/config.py` — no other code changes needed.
