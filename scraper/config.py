"""Configuration: which sites/queries the tracker checks."""

USER_AGENT = (
    "ProteinPriceTrackerBot/1.0 (+https://github.com/; personal price-tracking project; "
    "contact: contacttoashutosh18@gmail.com)"
)

REQUEST_TIMEOUT = 20

# Nutrabay: server-rendered search results, robots.txt allows /search
NUTRABAY_QUERIES = [
    "whey protein",
    "whey protein isolate",
    "plant protein",
]

# D2C brands running on Shopify, whose /products.json endpoint is publicly
# exposed by Shopify itself (not a scraping workaround).
SHOPIFY_STORES = {
    "Fast&Up": "https://in.fastandup.com",
    "OZiva": "https://oziva.in",
    "Wellbeing Nutrition": "https://wellbeingnutrition.com",
    "AS-IT-IS Nutrition": "https://asitisnutrition.com",
    "MyFitness": "https://myfitness.co.in",
    "Naturaltein": "https://naturaltein.in",
    "GNC India": "https://gnc.in",
}

# Only keep Shopify products whose title matches one of these (case-insensitive)
PROTEIN_KEYWORDS = ["protein", "whey", "isolate", "casein"]

# Drop matches that are protein-adjacent merch/accessories, not the powder itself
EXCLUDE_KEYWORDS = [
    "shaker", "bottle", "bag", "t-shirt", "tshirt", "hoodie", "tank",
    "cap", "wristband", "glove", "belt", "backpack", "gift card", "voucher",
]

TOP_N_PER_SOURCE = 15
