# 🧪 Test Cases — Car Price Prediction Streamlit App

> Run these in your Streamlit app at `http://localhost:8501` to verify everything works correctly.
> Model: **LightGBM** (R² = 0.9376) — retrained without target-leaking features.

---

## 📋 Quick Reference Table

| TC | Car | Category | Fuel · Transmission | Expected Price |
|:--:|-----|:--------:|:--------------------:|---------------:|
| 01 | Maruti, 8yr, 85K km | 🟢 Budget | Petrol · Manual | **₹2,69,428** (2.69L) |
| 02 | Honda, 4yr, 45K km | 🔵 Mid-range | Petrol · Manual | **₹8,11,211** (8.11L) |
| 03 | Hyundai, 3yr, 30K km, 7-seat | 🟠 Premium | Diesel · Automatic | **₹20,24,066** (20.24L) |
| 04 | BMW, 2yr, 18K km | 🟣 Luxury | Diesel · Automatic | **₹34,82,137** (34.82L) |
| 05 | Jaguar, 1yr, 8K km | 🟣 Luxury | Diesel · Automatic | **₹33,81,736** (33.82L) |
| 06 | Maruti, 15yr, 200K km | 🔴 Edge case | Petrol · Manual | **₹1,49,935** (1.50L) |
| 07 | Tata, 1yr, 10K km | 🔴 Edge case | Electric · Automatic | **₹15,22,314** (15.22L) |
| 08 | Hyundai, 6yr, 70K km | 🟢 Budget | CNG · Manual | **₹4,63,865** (4.64L) |
| 09 | Toyota, 5yr, 55K km, 8-seat | 🔵 Mid-range | Diesel · Manual | **₹14,40,709** (14.41L) |
| 10 | Ford, 4yr, 40K km | 🟠 Premium | Petrol · Automatic | **₹8,27,232** (8.27L) |
| 11 | Audi, 1yr, 5K km | 🟣 Luxury | Petrol · Automatic | **₹35,06,699** (35.07L) — highest |
| 12 | Honda, 7yr, 130K km | 🔴 Edge case | Diesel · Manual | **₹4,95,458** (4.95L) |

---

## TC01 — Budget Hatchback
🟢 **Budget** · Tests high age + high km depreciation on a budget brand

| Field | Value | | Field | Value |
|-------|-------|-|-------|-------|
| Brand | Maruti | | Mileage | 22.0 kmpl |
| Vehicle Age | 8 years | | Engine | 998 cc |
| KM Driven | 85,000 | | Max Power | 67.0 bhp |
| Seller Type | Individual | | Seats | 5 |
| Fuel Type | Petrol | | Transmission | Manual |

> **Expected Price: ₹2,69,428 (2.69L)**
> Budget segment with heavy age + mileage depreciation. The retrained model now reflects a realistic depreciation curve rather than an artificially flat price.

---

## TC02 — Mid-Range Sedan (Dealer)
🔵 **Mid-range** · Tests dealer trust premium + moderate usage

| Field | Value | | Field | Value |
|-------|-------|-|-------|-------|
| Brand | Honda | | Mileage | 17.0 kmpl |
| Vehicle Age | 4 years | | Engine | 1497 cc |
| KM Driven | 45,000 | | Max Power | 119.0 bhp |
| Seller Type | Dealer | | Seats | 5 |
| Fuel Type | Petrol | | Transmission | Manual |

> **Expected Price: ₹8,11,211 (8.11L)**
> A well-maintained 4-year Honda Petrol through a dealer. This reflects real market value for the mid-segment far better than earlier estimates.

---

## TC03 — Premium Diesel SUV
🟠 **Premium** · Tests Diesel + Automatic + 7 seats + low age combined

| Field | Value | | Field | Value |
|-------|-------|-|-------|-------|
| Brand | Hyundai | | Mileage | 17.0 kmpl |
| Vehicle Age | 3 years | | Engine | 1995 cc |
| KM Driven | 30,000 | | Max Power | 148.0 bhp |
| Seller Type | Dealer | | Seats | 7 |
| Fuel Type | Diesel | | Transmission | Automatic |

> **Expected Price: ₹20,24,066 (20.24L)**
> Multiple premium signals (diesel, automatic, 7-seat, young age) stack together. This now matches real CarDekho listings for a comparable Hyundai diesel SUV.

---

## TC04 — Luxury German Sedan (BMW)
🟣 **Luxury** · Tests luxury brand + barely used + high power

| Field | Value | | Field | Value |
|-------|-------|-|-------|-------|
| Brand | BMW | | Mileage | 14.0 kmpl |
| Vehicle Age | 2 years | | Engine | 1998 cc |
| KM Driven | 18,000 | | Max Power | 190.0 bhp |
| Seller Type | Dealer | | Seats | 5 |
| Fuel Type | Diesel | | Transmission | Automatic |

> **Expected Price: ₹34,82,137 (34.82L)**
> Nearly-new BMW diesel automatic. Correctly predicts a price in line with real used BMW 3-Series listings. Compare with TC05 and TC11.

---

## TC05 — Ultra Luxury (Jaguar)
🟣 **Luxury** · Tests massive engine + ultra-high power + nearly new

| Field | Value | | Field | Value |
|-------|-------|-|-------|-------|
| Brand | Jaguar | | Mileage | 12.0 kmpl |
| Vehicle Age | 1 year | | Engine | 2993 cc |
| KM Driven | 8,000 | | Max Power | 296.0 bhp |
| Seller Type | Dealer | | Seats | 5 |
| Fuel Type | Diesel | | Transmission | Automatic |

> **Expected Price: ₹33,81,736 (33.82L)**
> Highest power figure in the test set (296 bhp). Slightly below TC04 BMW despite the bigger engine — both sit just under TC11 Audi, the overall highest prediction.

---

## TC06 — Old Car, Very High Mileage ⚠️ Edge Case
🔴 **Edge case** · Maximum depreciation stress test — must never go negative

| Field | Value | | Field | Value |
|-------|-------|-|-------|-------|
| Brand | Maruti | | Mileage | 18.0 kmpl |
| Vehicle Age | 15 years | | Engine | 1197 cc |
| KM Driven | 2,00,000 | | Max Power | 82.0 bhp |
| Seller Type | Individual | | Seats | 5 |
| Fuel Type | Petrol | | Transmission | Manual |

> **Expected Price: ₹1,49,935 (1.50L)** — ✅ lowest in the test set
> 15 years and 2 lakh km of depreciation. The model correctly floors at a low but positive value — never ₹0 or negative.

---

## TC07 — New Electric Car ⚠️ Edge Case
🔴 **Edge case** · Electric fuel type with mileage set to 0.0

| Field | Value | | Field | Value |
|-------|-------|-|-------|-------|
| Brand | Tata | | Mileage | 0.0 kmpl |
| Vehicle Age | 1 year | | Engine | 1200 cc |
| KM Driven | 10,000 | | Max Power | 130.0 bhp |
| Seller Type | Dealer | | Seats | 5 |
| Fuel Type | Electric | | Transmission | Automatic |

> **Expected Price: ₹15,22,314 (15.22L)**
> Electric cars report 0 kmpl mileage — this confirms the model handles that edge case correctly. Predicts a value consistent with a nearly-new Tata Nexon EV.

---

## TC08 — CNG Budget Car ⚠️ Edge Case
🟢 **Budget** · CNG is the rarest fuel type in the dataset

| Field | Value | | Field | Value |
|-------|-------|-|-------|-------|
| Brand | Hyundai | | Mileage | 22.0 kmpl |
| Vehicle Age | 6 years | | Engine | 1197 cc |
| KM Driven | 70,000 | | Max Power | 82.0 bhp |
| Seller Type | Individual | | Seats | 5 |
| Fuel Type | CNG | | Transmission | Manual |

> **Expected Price: ₹4,63,865 (4.64L)**
> CNG is underrepresented in the dataset — this validates that minority-category encoding still produces a sensible price.

---

## TC09 — Family MUV (8 Seater)
🔵 **Mid-range** · 8 seats + large diesel engine

| Field | Value | | Field | Value |
|-------|-------|-|-------|-------|
| Brand | Toyota | | Mileage | 15.0 kmpl |
| Vehicle Age | 5 years | | Engine | 2494 cc |
| KM Driven | 55,000 | | Max Power | 148.0 bhp |
| Seller Type | Dealer | | Seats | 8 |
| Fuel Type | Diesel | | Transmission | Manual |

> **Expected Price: ₹14,40,709 (14.41L)**
> An 8-seat diesel MUV — the model's prediction lines up closely with real Toyota Innova Crysta resale prices.

---

## TC10 — Sports Car via Trustmark Dealer
🟠 **Premium** · Trustmark Dealer is the rarest of the 3 seller types

| Field | Value | | Field | Value |
|-------|-------|-|-------|-------|
| Brand | Ford | | Mileage | 14.0 kmpl |
| Vehicle Age | 4 years | | Engine | 1496 cc |
| KM Driven | 40,000 | | Max Power | 123.0 bhp |
| Seller Type | Trustmark Dealer | | Seats | 5 |
| Fuel Type | Petrol | | Transmission | Automatic |

> **Expected Price: ₹8,27,232 (8.27L)**
> Specifically exercises the "Trustmark Dealer" option. A realistic price for a 4-year Ford Petrol Automatic.

---

## TC11 — Nearly New Audi
🟣 **Luxury** · Highest predicted price in the entire test set

| Field | Value | | Field | Value |
|-------|-------|-|-------|-------|
| Brand | Audi | | Mileage | 11.0 kmpl |
| Vehicle Age | 1 year | | Engine | 1984 cc |
| KM Driven | 5,000 | | Max Power | 190.0 bhp |
| Seller Type | Dealer | | Seats | 5 |
| Fuel Type | Petrol | | Transmission | Automatic |

> **Expected Price: ₹35,06,699 (35.07L)** — 🏆 highest in the test set
> Barely used, high-power, premium German brand. Correctly outranks TC04 (BMW) and TC05 (Jaguar) despite similar specs.

---

## TC12 — High Mileage Diesel (Individual Seller) ⚠️ Edge Case
🔴 **Edge case** · Individual seller discount vs. high-km diesel tradeoff

| Field | Value | | Field | Value |
|-------|-------|-|-------|-------|
| Brand | Honda | | Mileage | 20.0 kmpl |
| Vehicle Age | 7 years | | Engine | 1498 cc |
| KM Driven | 1,30,000 | | Max Power | 100.0 bhp |
| Seller Type | Individual | | Seats | 5 |
| Fuel Type | Diesel | | Transmission | Manual |

> **Expected Price: ₹4,95,458 (4.95L)**
> Good diesel fuel economy offsets high mileage — a realistic price for a 7-year individually-sold Honda diesel.

---

## ✅ What to Verify

| Check | Expected Result |
|-------|-----------------|
| Price is never ₹0 or negative | ✅ TC06 floors at ₹1.50L, never zero |
| Lowest price in the set | TC06 (Old Maruti, 15yr/200K km) |
| Highest price in the set | TC11 (Nearly new Audi) |
| Electric fuel type (mileage = 0) | TC07 must not crash or error |
| CNG fuel type (rare category) | TC08 must encode correctly |
| All 3 seller types work | TC10 confirms "Trustmark Dealer" |
| Price ordering | TC01 < TC02 < TC09 ≈ TC03 < TC05 < TC04 < TC11 |
| History table updates per prediction | Run TCs in sequence, check the table |
| Theme toggle preserves form values | Switch Light/Dark — values stay intact |
| +/− buttons don't reset other fields | Only the field you change should change |

---

## 🔄 UI / Persistence Tests

These don't check prices — they check **app behaviour**:

1. **Field persistence** — Fill in TC03 → predict → change only the Brand to BMW → predict again. Every other field should remain exactly as entered.
2. **Theme persistence** — Fill in any test case → switch to Dark Mode → confirm no values reset.
3. **History tracking** — Run TC01, TC02, TC03 in sequence → the history table should show all three with the correct prices → click **Clear History** → table disappears.
4. **Stepper isolation** — Click the **+ / −** buttons on KM Driven → only KM Driven should change; every other field stays put.

---

<sub>Model: LightGBM · R² = 0.9376 · Retrained without target-leaking features · Last verified against live predictions</sub>
