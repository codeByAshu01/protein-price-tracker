# Protein Price Tracker (India)

Daily-updated protein powder prices scraped from Indian D2C brand stores and
Nutrabay via a [GitHub Actions](.github/workflows/daily-price-check.yml) cron
job. Data sources and rationale: see [SOURCES.md](SOURCES.md).

**Last checked:** 2026-09-06 13:26 IST

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

## AS-IT-IS Nutrition

| Product | MRP | Price | Discount | ₹/100g (pack) | Stock | Link |
|---|---:|---:|---:|---:|:---:|---|
| AS-IT-IS ONE Brown Rice Protein - 27g Protein per Serving - Plant Protein - Single-Ingredient, Unflavoured (35g) | ₹175 | ₹122 | 30% | - | ✅ | [view](https://asitisnutrition.com/products/as-it-is-nutrition-brown-rice-protein-80-designed-as-meal-supplement-lab-tested-unflavoured) |
| AS-IT-IS ONE Pea Protein Isolate - 29g Protein per Serving - Plant Protein - Single-Ingredient, Unflavoured (36g-Sachet) | ₹175 | ₹122 | 30% | - | ❌ | [view](https://asitisnutrition.com/products/as-it-is-nutrition-pea-protein-isolate-powder) |
| AS-IT-IS ONE Soy Protein Isolate - 30g Protein per Serving - Plant Protein - Single-Ingredient, Unflavoured (35g) | ₹175 | ₹122 | 30% | - | ❌ | [view](https://asitisnutrition.com/products/as-it-is-nutrition-buy-soy-protein-isolate-powder-in-india) |
| AS-IT-IS ATOM Beginners Whey Protein - 15g Protein per Serving - With DigeZyme® Enzymes (Choco Hazel Fusion / 37g) | ₹203 | ₹131 | 36% | - | ✅ | [view](https://asitisnutrition.com/products/atom-beginners-whey-protein) |
| AS-IT-IS ATOM Performance Whey - 25g Protein per Serving - With Safed Musli, Mucuna & DigeZyme® Enzymes (Double Rich Chocolate / 45g) | ₹220 | ₹140 | 36% | - | ❌ | [view](https://asitisnutrition.com/products/as-it-is-atom-performance-whey-1kg-with-safed-musli-for-faster-recovery-highly-bioavailable) |
| AS-IT-IS ATOM Performance Whey - 25g Protein per Serving - With Safed Musli, Mucuna & DigeZyme® Enzymes (Pista Fusion / 45g) | ₹2,485 | ₹140 | 94% | - | ❌ | [view](https://asitisnutrition.com/products/as-it-is-atom-performance-whey-1kg-with-safed-musli-for-faster-recovery-highly-bioavailable) |
| AS-IT-IS ATOM Performance Whey - 25g Protein per Serving - With Safed Musli, Mucuna & DigeZyme® Enzymes (Cafe Latte / 45g) | ₹2,485 | ₹140 | 94% | - | ❌ | [view](https://asitisnutrition.com/products/as-it-is-atom-performance-whey-1kg-with-safed-musli-for-faster-recovery-highly-bioavailable) |
| AS-IT-IS ATOM Performance Whey - 25g Protein per Serving - With Safed Musli, Mucuna & DigeZyme® Enzymes (Cookie delight / 45g) | ₹2,485 | ₹140 | 94% | - | ❌ | [view](https://asitisnutrition.com/products/as-it-is-atom-performance-whey-1kg-with-safed-musli-for-faster-recovery-highly-bioavailable) |
| AS-IT-IS ATOM Performance Whey - 25g Protein per Serving - With Safed Musli, Mucuna & DigeZyme® Enzymes (Choco hazel fusion / 45g) | ₹2,485 | ₹140 | 94% | - | ❌ | [view](https://asitisnutrition.com/products/as-it-is-atom-performance-whey-1kg-with-safed-musli-for-faster-recovery-highly-bioavailable) |
| AS-IT-IS ATOM Whey Protein - 27g Protein per Serving - DigeZyme® Enzymes & 1 Billion CFU Probiotics (Double Rich Chocolate / (36g Travel Sachet)) | ₹262 | ₹167 | 36% | ₹463.89 | ✅ | [view](https://asitisnutrition.com/products/atom-whey-protein) |
| AS-IT-IS ONE Whey Protein Concentrate Sachets - 28g Protein per Serving - Unflavoured (35g Sachet (Pack of 1)) | ₹305 | ₹178 | 42% | ₹593.33 | ✅ | [view](https://asitisnutrition.com/products/whey-protein-30g-sachet) |
| AS-IT-IS ATOM Nitro Whey with Creasure® - 33g Protein, 3g Creatine per Serving - With DigeZyme® Enzymes (Double Rich Chocolate / 45g) | ₹289 | ₹185 | 36% | - | ✅ | [view](https://asitisnutrition.com/products/atom-nitro-whey-with-creatine-i-33g-protein-3g-creatine-7-4g-bcaa) |
| AS-IT-IS ATOM Nitro Whey with Creasure® - 33g Protein, 3g Creatine per Serving - With DigeZyme® Enzymes (Kesar Kulfi / 45g) | ₹3,407 | ₹185 | 95% | - | ❌ | [view](https://asitisnutrition.com/products/atom-nitro-whey-with-creatine-i-33g-protein-3g-creatine-7-4g-bcaa) |
| AS-IT-IS ATOM Nitro Whey with Creasure® - 33g Protein, 3g Creatine per Serving - With DigeZyme® Enzymes (Classic Vanilla / 45g) | ₹3,407 | ₹185 | 95% | - | ❌ | [view](https://asitisnutrition.com/products/atom-nitro-whey-with-creatine-i-33g-protein-3g-creatine-7-4g-bcaa) |
| AS-IT-IS ONE Whey Protein Concentrate Sachets - 28g Protein per Serving - Unflavoured (35g Sachet (Pack of 1) + Shaker) | ₹438 | ₹303 | 31% | ₹1010.00 | ❌ | [view](https://asitisnutrition.com/products/whey-protein-30g-sachet) |

## Fast&Up

| Product | MRP | Price | Discount | ₹/100g (pack) | Stock | Link |
|---|---:|---:|---:|---:|:---:|---|
| 100% Pure & Natural Moringa Powder | ₹250 | ₹238 | 5% | - | ✅ | [view](https://in.fastandup.com/products/100-pure-natural-moringa-powder) |
| Plant Protein - Assorted Pack | ₹270 | ₹243 | 10% | - | ✅ | [view](https://in.fastandup.com/products/fast-up-plant-protein-assorted-pack) |
| Plant Protein - Rich Chocolate - Single Serving Sachet Combo Pack (Rich Chocolate / Pack of 5) | ₹450 | ₹396 | 12% | - | ✅ | [view](https://in.fastandup.com/products/plant-protein-rich-chocolate-single-serving-sachet-combo-pack) |
| Plant Protein - Rich Chocolate - Single Serving Sachet Combo Pack (Rich Chocolate / Pack of 10) | ₹900 | ₹765 | 15% | - | ✅ | [view](https://in.fastandup.com/products/plant-protein-rich-chocolate-single-serving-sachet-combo-pack) |
| Plant Protein - Rich Chocolate - Single Serving Sachet Combo Pack (Rich Chocolate / Pack of 15) | ₹1,350 | ₹1,107 | 18% | - | ✅ | [view](https://in.fastandup.com/products/plant-protein-rich-chocolate-single-serving-sachet-combo-pack) |
| Plant Protein - Cookies & Cream - 500g | ₹1,599 | ₹1,199 | 25% | ₹239.80 | ✅ | [view](https://in.fastandup.com/products/plant-protein-cookies-cream-500g) |
| Plant Protein - Rich Chocolate – 500gms | ₹1,599 | ₹1,199 | 25% | ₹239.80 | ✅ | [view](https://in.fastandup.com/products/plant-protein-powder-500gms) |
| Plant Protein - Alphonso Mango - 1Kg | ₹3,115 | ₹2,181 | 30% | ₹218.10 | ✅ | [view](https://in.fastandup.com/products/plant-protein-alphonso-mango-25-servings) |
| Plant Protein - Kesar Kulfi - 1kg | ₹3,115 | ₹2,181 | 30% | ₹218.10 | ❌ | [view](https://in.fastandup.com/products/plant-protein-powder-special-festive-pack) |
| Plant Protein - Cookies & Cream - 1Kg | ₹3,115 | ₹2,181 | 30% | ₹218.10 | ✅ | [view](https://in.fastandup.com/products/plant-protein-cookies-cream-1-kg) |
| Plant Protein - Strawberry Blast - 25 Servings | ₹3,115 | ₹2,181 | 30% | - | ❌ | [view](https://in.fastandup.com/products/plant-protein-strawberry-25-servings) |
| Plant Protein - Rich Chocolate - 1kg | ₹3,115 | ₹2,181 | 30% | ₹218.10 | ✅ | [view](https://in.fastandup.com/products/plant-protein-rich-chocolate-1kg) |
| Plant Protein - Cookies & Cream - 500g Pack of 2 | ₹3,198 | ₹2,239 | 30% | ₹447.80 | ✅ | [view](https://in.fastandup.com/products/plant-protein-cookies-cream-500g-pack-of-2) |
| Daily Fiber + Plant Protein Rich Chocolate Combo | ₹3,715 | ₹2,299 | 38% | - | ✅ | [view](https://in.fastandup.com/products/daily-fiber-plant-protein-rich-chocolate-combo) |
| Plant Protein Rich Chocolate - 1kg pouch+ Plant Protein Cookies Cream- 1kg Pouch | ₹6,230 | ₹3,427 | 45% | ₹342.70 | ❌ | [view](https://in.fastandup.com/products/plant-protein-rich-chocolate-1kg-pouch-plant-protein-cookies-cream-1kg-pouch) |

## GNC India

| Product | MRP | Price | Discount | ₹/100g (pack) | Stock | Link |
|---|---:|---:|---:|---:|:---:|---|
| PP Protein Wafer Bar Mini 20gm (Chocolate / 20 gm) | ₹60 | ₹40 | 33% | ₹200.00 | ✅ | [view](https://gnc.in/products/pp-protein-wafer-bar-mini-20gm) |
| PP Protein Wafer Bar Mini 20gm (Coffee / 20 gm) | ₹60 | ₹40 | 33% | ₹200.00 | ✅ | [view](https://gnc.in/products/pp-protein-wafer-bar-mini-20gm) |
| PP Protein Wafer Bar Mini 20gm (Peanut Butter / 20 gm) | ₹60 | ₹40 | 33% | ₹200.00 | ✅ | [view](https://gnc.in/products/pp-protein-wafer-bar-mini-20gm) |
| GNC Protein Wafer Bar (Chocolate) (Pack of 1 / Chocolate) | ₹59 | ₹55 | 7% | - | ✅ | [view](https://gnc.in/products/gnc-protein-wafer-bar-chocolate) |
| GNC Protein Wafer Bar (Peanut butter) (Pack of 1 / Peanut Butter) | ₹59 | ₹55 | 7% | - | ✅ | [view](https://gnc.in/products/gnc-protein-wafer-bar-peanut-butter) |
| GNC Protein Wafer Bar (Coffee) (Pack of 1 / Coffee) | ₹59 | ₹55 | 7% | - | ✅ | [view](https://gnc.in/products/gnc-protein-wafer-bar-coffee) |
| GNC Protein Wafer Bar (40g / Chocolate) | ₹60 | ₹55 | 8% | ₹137.50 | ✅ | [view](https://gnc.in/products/gnc-protein-wafer-bar-upsell) |
| GNC Select Fermented Yeast Protein Isolate (35 gm / Chocolate) | ₹149 | ₹59 | 60% | ₹168.57 | ✅ | [view](https://gnc.in/products/gnc-select-fermented-yeast-protein) |
| GNC Select Fermented Yeast Protein Isolate (35 gm / Coffee) | ₹149 | ₹59 | 60% | ₹168.57 | ✅ | [view](https://gnc.in/products/gnc-select-fermented-yeast-protein) |
| GNC Select Fermented Yeast Protein Isolate (35 gm / Vanilla) | ₹149 | ₹59 | 60% | ₹168.57 | ✅ | [view](https://gnc.in/products/gnc-select-fermented-yeast-protein) |
| GNC Select Fermented Yeast Protein Isolate (35gm) (35 gm / Chocolate) | ₹149 | ₹65 | 56% | ₹185.71 | ✅ | [view](https://gnc.in/products/gnc-select-fermented-yeast-protein-isolate-35gm) |
| GNC Select Fermented Yeast Protein Isolate (35gm) (35 gm / Coffee) | ₹149 | ₹65 | 56% | ₹185.71 | ✅ | [view](https://gnc.in/products/gnc-select-fermented-yeast-protein-isolate-35gm) |
| GNC Select Fermented Yeast Protein Isolate (35gm) (35 gm / Vanilla) | ₹149 | ₹65 | 56% | ₹185.71 | ✅ | [view](https://gnc.in/products/gnc-select-fermented-yeast-protein-isolate-35gm) |
| 100% Whey Protein Sachets 35gm - Clearance Sale- Expiry - 2025-11-30 (Mawa Kulfi) | ₹199 | ₹70 | 65% | ₹200.00 | ❌ | [view](https://gnc.in/products/100-whey-protein-sachets-35gm) |
| GNC Protein Wafer Bar (Pack of 1 / Chocolate) | ₹120 | ₹79 | 34% | - | ✅ | [view](https://gnc.in/products/gnc-protein-wafer-bar) |

## MyFitness

| Product | MRP | Price | Discount | ₹/100g (pack) | Stock | Link |
|---|---:|---:|---:|---:|:---:|---|
| MyFitness Peanut Butter - Chocolate - 26% Protein - Crispy - Chocolate Peanut Butter Spread (227g) | ₹159 | ₹149 | 6% | ₹65.64 | ✅ | [view](https://myfitness.co.in/products/chocolate-crispy) |
| Pro.Fitness High Protein Chocolate Oats - Dark Chocolate - Healthy Oats With Nuts, Seeds & Added Whey (375g) | ₹339 | ₹219 | 35% | ₹58.40 | ✅ | [view](https://myfitness.co.in/products/high-protein-oats-900g-27g-protein) |
| Pro.Fitness Rolled Oats - 13% Protein - Healthy Oats With High Fiber and Zero Cholesterol (900g) | ₹320 | ₹269 | 16% | - | ❌ | [view](https://myfitness.co.in/products/pro-fitness-rolled-oats-900g) |
| MyFitness Peanut Butter - Classic Zero - 28% Protein - Extra Crunchy - Zero Sugar Peanut Spread (510 g) | ₹349 | ₹275 | 21% | ₹53.92 | ✅ | [view](https://myfitness.co.in/products/myfitness-zero-peanut-butter-crunchy-510g) |
| MyFitness Peanut Butter - Chocolate - 26% Protein - Crunchy - Chocolate Peanut Butter Spread (510 g) | ₹319 | ₹275 | 14% | ₹45.08 | ✅ | [view](https://myfitness.co.in/products/myfitness-chocolate-peanut-butter-crunchy) |
| MyFitness Peanut Butter - Natural Unsweetened - 31% Protein - Crunchy - Zero Sugar Peanut Butter Spread (510 g) | ₹319 | ₹275 | 14% | ₹45.08 | ✅ | [view](https://myfitness.co.in/products/myfitness-all-natural-peanut-butter-crunchy) |
| MyFitness Peanut Butter - Natural Unsweetened - 25% Protein - Smooth - Zero Sugar Peanut Butter Spread (510 g) | ₹319 | ₹275 | 14% | ₹45.08 | ✅ | [view](https://myfitness.co.in/products/myfitness-all-natural-peanut-butter-smooth) |
| MyFitness Peanut Butter - Chocolate - 26% Protein - Crispy - Chocolate Peanut Butter Spread (510 g) | ₹319 | ₹275 | 14% | ₹45.08 | ✅ | [view](https://myfitness.co.in/products/myfitness-chocolate-peanut-butter-crispy) |
| MyFitness Peanut Butter - Chocolate - 28% Protein - Smooth - Chocolate Peanut Butter Spread (510 g) | ₹319 | ₹275 | 14% | ₹45.08 | ✅ | [view](https://myfitness.co.in/products/myfitness-chocolate-peanut-butter-smooth) |
| MyFitness Peanut Butter - Original - 28% Protein - Crunchy - Classic Peanut Butter Spread (510 g) | ₹319 | ₹275 | 14% | ₹45.08 | ✅ | [view](https://myfitness.co.in/products/myfitness-original-peanut-butter-crunchy) |
| MyFitness Peanut Butter - Original - 28% Protein - Smooth - Classic Peanut Butter Spread (510 g) | ₹319 | ₹275 | 14% | ₹45.08 | ✅ | [view](https://myfitness.co.in/products/myfitness-original-peanut-butter-smooth) |
| MyFitness Peanut Butter - Chocolate - 25% Protein - Almond Crunch - Chocolate Peanut Butter Spread (510 g) | ₹379 | ₹279 | 26% | ₹54.71 | ✅ | [view](https://myfitness.co.in/products/myfitness-chocolate-peanut-butter-with-almond-crunch) |
| MyFitness x Batman - Chocolate Zero Peanut Butter Extra Crunchy - 27% Protein - Zero Added Sugar - High Protein (510 g) | ₹369 | ₹299 | 19% | ₹58.63 | ✅ | [view](https://myfitness.co.in/products/myfitness-zero-chocolate-peanut-butter-crunchy-zero-sugar-extra-crunch-510g-27g-protein-10g-fiber-tasty-healthy-nut-butter-spread-cholesterol-free-zero-trans-fat-crunchy-peanut-butter) |
| MyFitness Peanut Butter - Dark Chocolate - 30% Protein - Smooth - Rich Chocolate Peanut Butter Spread (510 g) | ₹399 | ₹299 | 25% | ₹49.02 | ✅ | [view](https://myfitness.co.in/products/myfitness-olympia-edition-dark-chocolate-peanut-butter-with-added-whey-smooth) |
| MyFitness Peanut Butter - Dark Chocolate - 29% Protein - Crispy - Rich Chocolate Peanut Butter Spread (510 g) | ₹399 | ₹319 | 20% | ₹52.30 | ✅ | [view](https://myfitness.co.in/products/myfitness-peanut-butter-dark-chocolate-29-protein-crispy-rich-chocolate-peanut-butter-spread) |

## Naturaltein

| Product | MRP | Price | Discount | ₹/100g (pack) | Stock | Link |
|---|---:|---:|---:|---:|:---:|---|
| The Protein Dessert E-Cook Book by Naturaltein | ₹599 | ₹399 | 33% | - | ✅ | [view](https://naturaltein.in/products/the-protein-dessert-e-cook-book-by-naturaltein) |
| Natural Plant Protein (Chocolate / 1 Box (500 g)) | ₹3,000 | ₹1,112 | 63% | ₹222.40 | ✅ | [view](https://naturaltein.in/products/plant-protein) |
| Natural Plant Protein (Mango / 1 Box (500 g)) | ₹3,000 | ₹1,112 | 63% | ₹222.40 | ✅ | [view](https://naturaltein.in/products/plant-protein) |
| Natural Plant Protein (Berry / 1 Box (500 g)) | ₹3,000 | ₹1,112 | 63% | ₹222.40 | ✅ | [view](https://naturaltein.in/products/plant-protein) |
| Natural Plant Protein (Pista / 1 Box (500 g)) | ₹3,000 | ₹1,112 | 63% | ₹222.40 | ✅ | [view](https://naturaltein.in/products/plant-protein) |
| Natural Plant Protein (Coffee / 1 Box (500 g)) | ₹3,000 | ₹1,112 | 63% | ₹222.40 | ✅ | [view](https://naturaltein.in/products/plant-protein) |
| Natural Whey Protein Concentrate (Italian Ice Cream / 1 Box (300 g)) | ₹1,424 | ₹1,299 | 9% | ₹433.00 | ❌ | [view](https://naturaltein.in/products/whey-protein-concentrate) |
| Natural Whey Protein Concentrate (Chocolate Biscoff / 1 Box (300 g)) | ₹1,424 | ₹1,399 | 2% | ₹466.33 | ❌ | [view](https://naturaltein.in/products/whey-protein-concentrate) |
| Natural Whey Protein Concentrate (Chocolate Caramel / 1 Box (300 g)) | ₹1,424 | ₹1,399 | 2% | ₹466.33 | ❌ | [view](https://naturaltein.in/products/whey-protein-concentrate) |
| Natural Whey Protein Concentrate (Chocolate / 1 Box (300 g)) | ₹2,500 | ₹1,524 | 39% | ₹508.00 | ✅ | [view](https://naturaltein.in/products/whey-protein-concentrate) |
| Natural Whey Protein Concentrate (Unflavoured / 1 Box (300 g)) | ₹2,500 | ₹1,524 | 39% | ₹508.00 | ❌ | [view](https://naturaltein.in/products/whey-protein-concentrate) |
| Natural Whey Protein Concentrate (Caffe Mocha / 1 Box (300 g)) | ₹2,500 | ₹1,524 | 39% | ₹508.00 | ✅ | [view](https://naturaltein.in/products/whey-protein-concentrate) |
| Natural Plant Protein (Chocolate / 2 Boxes (1 kg)) | ₹6,000 | ₹1,600 | 73% | ₹160.00 | ✅ | [view](https://naturaltein.in/products/plant-protein) |
| Natural Plant Protein (Mango / 2 Boxes (1 kg)) | ₹6,000 | ₹1,600 | 73% | ₹160.00 | ✅ | [view](https://naturaltein.in/products/plant-protein) |
| Natural Plant Protein (Berry / 2 Boxes (1 kg)) | ₹6,000 | ₹1,600 | 73% | ₹160.00 | ✅ | [view](https://naturaltein.in/products/plant-protein) |

## Nutrabay

| Product | MRP | Price | Discount | ₹/100g (pack) | Stock | Link |
|---|---:|---:|---:|---:|:---:|---|
| Nutrabay Gold Pea Protein | ₹69 | ₹69 | 0% | ₹172.50 | ✅ | [view](https://nutrabay.com/product/nutrabay-gold-hydrolyzed-pea-protein/?pId=3302532) |
| Nutrabay Gold Pea Protein | ₹69 | ₹69 | 0% | ₹172.50 | ✅ | [view](https://nutrabay.com/product/nutrabay-gold-hydrolyzed-pea-protein/?pId=3302532) |
| Velbiom Happy Cultures Tastiest Plant Protein | ₹600 | ₹499 | 17% | ₹346.53 | ✅ | [view](https://nutrabay.com/product/velbiom-happy-cultures-tastiest-plant-protein/?pId=7407265) |
| Nutrabay Pure Pea Protein Isolate | ₹669 | ₹599 | 10% | ₹119.80 | ✅ | [view](https://nutrabay.com/product/nutrabay-pure-100-pea-protein-isolate/?pId=4537768) |
| TruNativ Plant Based Everyday Protein - Protein You Can Cook With! | ₹699 | ₹599 | 14% | ₹363.03 | ✅ | [view](https://nutrabay.com/product/trunativ-plant-based-everyday-protein-protein-you-can-cook-with/?pId=9485223) |
| Nutrabay BioAbsorb™ Whey Protein Powder - Clinically Tested 54% Better Protein Absorption - 26g Protein/Scoop - India's 1st Protein with ProDiFi™ for No Bloating - No Added Sugar | ₹859 | ₹699 | 19% | ₹386.19 | ✅ | [view](https://nutrabay.com/product/nutrabay-bioabsorb-whey-protein/?pId=8042444) |
| Nutrabay Wellness Vegan Plant Protein Powder + Superfoods | ₹1,199 | ₹699 | 42% | ₹139.80 | ✅ | [view](https://nutrabay.com/product/nutrabay-wellness-vegan-plant-protein-powder-superfoods/?pId=4698878) |
| Nutrabay Wellness Vegan Plant Protein Powder + Superfoods | ₹1,199 | ₹799 | 33% | ₹159.80 | ✅ | [view](https://nutrabay.com/product/nutrabay-wellness-vegan-plant-protein-powder-superfoods/?pId=4698878) |
| Nutrabay Gold Pea Protein | ₹1,049 | ₹799 | 24% | ₹159.80 | ✅ | [view](https://nutrabay.com/product/nutrabay-gold-hydrolyzed-pea-protein/?pId=3302532) |
| Nutrabay Gold Pea Protein | ₹1,049 | ₹799 | 24% | ₹159.80 | ✅ | [view](https://nutrabay.com/product/nutrabay-gold-hydrolyzed-pea-protein/?pId=3302532) |
| Nutrabay Gold Pea Protein | ₹1,049 | ₹799 | 24% | ₹159.80 | ✅ | [view](https://nutrabay.com/product/nutrabay-gold-hydrolyzed-pea-protein/?pId=3302532) |
| Nutrabay Pure Pea Protein Isolate | ₹1,349 | ₹849 | 37% | ₹84.90 | ✅ | [view](https://nutrabay.com/product/nutrabay-pure-100-pea-protein-isolate/?pId=4537768) |
| Velbiom Happy Cultures Tastiest Plant Protein | ₹1,699 | ₹949 | 44% | ₹187.92 | ✅ | [view](https://nutrabay.com/product/velbiom-happy-cultures-tastiest-plant-protein/?pId=7407265) |
| Velbiom Happy Cultures Tastiest Plant Protein | ₹1,699 | ₹949 | 44% | ₹187.92 | ✅ | [view](https://nutrabay.com/product/velbiom-happy-cultures-tastiest-plant-protein/?pId=7407265) |
| Velbiom Happy Cultures Tastiest Plant Protein | ₹1,699 | ₹949 | 44% | ₹187.92 | ✅ | [view](https://nutrabay.com/product/velbiom-happy-cultures-tastiest-plant-protein/?pId=7407265) |

## OZiva

| Product | MRP | Price | Discount | ₹/100g (pack) | Stock | Link |
|---|---:|---:|---:|---:|:---:|---|
| Plant Protein + Pro-Digest (Mango) | ₹139 | ₹139 | 0% | - | ✅ | [view](https://oziva.in/products/plant-protein-pro-digest) |
| Pro-Collagen Protein Peptides Caramel - 250g | ₹799 | ₹433 | 46% | ₹173.20 | ✅ | [view](https://oziva.in/products/pro-collagen-protein-peptides-caramel-250g) |
| Vegan Collagen, Clinically Proven (Watermelon / Starter Pack-125g) | ₹499 | ₹459 | 8% | ₹367.20 | ✅ | [view](https://oziva.in/products/plant-based-collagen) |
| Plant Protein + Pro-Digest (Assorted) | ₹699 | ₹699 | 0% | - | ✅ | [view](https://oziva.in/products/plant-protein-pro-digest) |
| Plant Protein + Pro-Digest (Chocolate) | ₹699 | ₹699 | 0% | - | ❌ | [view](https://oziva.in/products/plant-protein-pro-digest) |
| Plant Protein + Pro-Digest (Strawberry) | ₹699 | ₹699 | 0% | - | ❌ | [view](https://oziva.in/products/plant-protein-pro-digest) |
| Plant Protein + Pro-Digest (Vanilla) | ₹699 | ₹699 | 0% | - | ❌ | [view](https://oziva.in/products/plant-protein-pro-digest) |
| Plant Protein + Pro-Digest (Assorted / Starter Pack) | ₹699 | ₹699 | 0% | - | ✅ | [view](https://oziva.in/products/oziva-bioactive-plant-protein-with-25g-vegan-protein-5-5-bcaas-100-rda-vitamins-minerals-ayurvedic-herbs-for-better-endurance-stamina-muscle-recovery-1-kg) |
| Daily Protein Activ for Women (Rich Chocolate / Starter Pack) | ₹799 | ₹749 | 6% | - | ✅ | [view](https://oziva.in/products/daily-protein-activ-for-women-with-clean-whey-protein-multivitamins-tulsi-probiotics-for-improved-everyday-energy-stamina-bone-health-immune-health) |
| Daily Protein Activ for Women (Classic Vanilla / Starter Pack) | ₹799 | ₹749 | 6% | - | ✅ | [view](https://oziva.in/products/daily-protein-activ-for-women-with-clean-whey-protein-multivitamins-tulsi-probiotics-for-improved-everyday-energy-stamina-bone-health-immune-health) |
| Pro-Collagen Protein Peptides, 250 g (Starter Pack) | ₹849 | ₹799 | 6% | ₹319.60 | ✅ | [view](https://oziva.in/products/oziva-pro-collagen-protein-peptides-with-clean-protein-green-coffee-hyaluronic-acid-biotin-for-skin-hair-health-muscle-joint-health-protein-breakdown-caramel-250-g) |
| Vegan Collagen, Clinically Proven (Guava Glow / Starter Pack) | ₹959 | ₹929 | 3% | - | ✅ | [view](https://oziva.in/products/plant-based-collagen) |
| Vegan Collagen, Clinically Proven (Classic / Starter Pack) | ₹959 | ₹929 | 3% | - | ✅ | [view](https://oziva.in/products/plant-based-collagen) |
| Vegan Collagen, Clinically Proven (Berry Orange / Starter Pack) | ₹959 | ₹929 | 3% | - | ✅ | [view](https://oziva.in/products/plant-based-collagen) |
| Vegan Collagen, Clinically Proven (Watermelon / Starter Pack) | ₹959 | ₹929 | 3% | - | ✅ | [view](https://oziva.in/products/plant-based-collagen) |

## Wellbeing Nutrition

| Product | MRP | Price | Discount | ₹/100g (pack) | Stock | Link |
|---|---:|---:|---:|---:|:---:|---|
| Kids Protein Vanilla Free Sachet | ₹79 | ₹79 | 0% | - | ✅ | [view](https://wellbeingnutrition.com/products/kids-protein-vanilla-free-sachet) |
| Kids Protein Chocolate Sachet | ₹79 | ₹79 | 0% | - | ✅ | [view](https://wellbeingnutrition.com/products/kids-protein-chocolate-sachet) |
| Kids Protein Vanilla Sachet | ₹79 | ₹79 | 0% | - | ✅ | [view](https://wellbeingnutrition.com/products/kids-protein-vanilla-sachet) |
| Vegan Protein Dark Chocolate Hazelnut Sachet | ₹150 | ₹150 | 0% | - | ✅ | [view](https://wellbeingnutrition.com/products/vegan-protein-dark-chocolate-hazelnut-sachet) |
| Whey Protein Isolate Dark Chocolate Sachet (Pack of 1) | ₹160 | ₹160 | 0% | - | ❌ | [view](https://wellbeingnutrition.com/products/whey-protein-isolate-dark-chocolate-sachet) |
| Whey Protein Isolate + Concentrate Mango Sachets (Pack of 1) | ₹1,399 | ₹1,399 | 0% | - | ❌ | [view](https://wellbeingnutrition.com/products/whey-protein-isolate-concentrate-mango-sachets) |
| Plant Protein 22g - 500g - 3B CFU Probiotics - Dark Chocolate Hazelnut (Pack of 1) | ₹1,799 | ₹1,709 | 5% | ₹341.80 | ✅ | [view](https://wellbeingnutrition.com/products/vegan-protein-dark-chocolate-hazelnut) |
| Plant Protein 22g - 500g - 3B CFU Probiotics - Italian Cafe Mocha (Pack of 1) | ₹1,799 | ₹1,709 | 5% | ₹341.80 | ❌ | [view](https://wellbeingnutrition.com/products/vegan-protein-italian-cafe-mocha) |
| Plant Protein 22g - 500g - 3B CFU Probiotics - Belgian Dark Chocolate (Pack of 1) | ₹1,799 | ₹1,709 | 5% | ₹341.80 | ✅ | [view](https://wellbeingnutrition.com/products/vegan-protein-belgian-chocolate) |
| Plant Protein 22g - 500g - 3B CFU Probiotics - French Vanilla Caramel (Pack of 1) | ₹1,799 | ₹1,709 | 5% | ₹341.80 | ✅ | [view](https://wellbeingnutrition.com/products/vegan-protein-french-vanilla-caramel) |
| Plant Protein 22g - 500g - 3B CFU Probiotics - Canadian Mixed Berry (Pack of 1) | ₹1,799 | ₹1,709 | 5% | ₹341.80 | ✅ | [view](https://wellbeingnutrition.com/products/vegan-protein-canadian-mixed-berry) |
| Her Superfood Plant Protein - Chocolate Peanut Butter (Pack of 1) | ₹1,799 | ₹1,709 | 5% | - | ✅ | [view](https://wellbeingnutrition.com/products/superfood-plant-protein-powder-for-women) |
| Superfood Plant Protein - British Banoffee Pie (Pack of 1) | ₹1,799 | ₹1,709 | 5% | - | ✅ | [view](https://wellbeingnutrition.com/products/superfood-plant-protein-powder-in-banoffee-pie) |
| Whey Protein Isolate + Concentrate Mango Sachets (Pack of 2) | ₹2,798 | ₹2,798 | 0% | - | ❌ | [view](https://wellbeingnutrition.com/products/whey-protein-isolate-concentrate-mango-sachets) |
| Plant Protein 22g - 907g - 3B CFU Probiotics - French Vanilla Caramel (Pack of 1) | ₹3,399 | ₹3,229 | 5% | ₹356.01 | ✅ | [view](https://wellbeingnutrition.com/products/vegan-protein-french-vanilla-caramel-copy) |


*₹/100g is price per 100g of product weight, not per gram of protein (macros aren't available from these feeds). Prices are snapshots at check time and may have changed since — always verify on the retailer's site.*
