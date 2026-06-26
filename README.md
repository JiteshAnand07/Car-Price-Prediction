<div align="center">
<<<<<<< Updated upstream
        
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=28&pause=1000&color=2563EB&center=true&vCenter=true&width=600&lines=Car+Price+Prediction+System;Machine+Learning+%7C+LightGBM+%7C+Streamlit" alt="Typing SVG" />
        
=======

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=28&pause=1000&color=2563EB&center=true&vCenter=true&width=600&lines=Car+Price+Prediction+System;Machine+Learning%7CLightGBM%7CStreamlit" alt="Typing SVG" />

>>>>>>> Stashed changes
<br/>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![LightGBM](https://img.shields.io/badge/LightGBM-Best_Model-2ecc71?style=for-the-badge&logo=leaflet&logoColor=white)](https://lightgbm.readthedocs.io)
[![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML_Pipeline-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org)

<br/>

[![R² Score](https://img.shields.io/badge/R²_Score-0.9376-brightgreen?style=flat-square)]()
[![CV Score](https://img.shields.io/badge/CV_R²-0.9360_±_0.0044-blue?style=flat-square)]()
[![Models](https://img.shields.io/badge/Models_Tested-11-purple?style=flat-square)]()
[![Records](https://img.shields.io/badge/Training_Records-14%2C353-orange?style=flat-square)]()
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

<br/>

> **An end-to-end industry-grade machine learning system** that predicts used car resale prices with an **R² of 0.9376** — featuring a leak-free ML pipeline, 11 algorithms, hyperparameter tuning, and a professional dual-theme Streamlit web application.

</div>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Live Demo](#-live-demo)
- [Dataset](#-dataset)
- [Project Structure](#-project-structure)
- [Technologies Used](#️-technologies-used)
- [ML Pipeline](#-ml-pipeline)
- [What Was Built](#-what-was-built)
- [Model Results](#-model-results)
- [Feature Engineering](#️-feature-engineering)
- [Residual Analysis](#-residual-analysis)
- [Streamlit App](#-streamlit-app)
- [Test Cases](#-test-cases)
- [Installation & Setup](#-installation--setup)
- [Deployment](#️-deployment)
- [Future Scope](#-future-scope)

---

## 🎯 Overview

The used car market in India is worth billions of dollars yet pricing remains inconsistent — buyers overpay, sellers undervalue. This project solves that with a **data-driven ML system** trained on 15,000+ real-world CarDekho listings.

| Attribute | Details |
|-----------|---------|
| **Problem Type** | Supervised Regression |
| **Target Variable** | `selling_price` (INR) |
| **Dataset Size** | 15,411 entries → 14,353 after cleaning & outlier treatment |
| **Best Model** | LightGBM (tuned) |
| **R² Score** | 0.9376 |
| **Adjusted R²** | 0.9373 |
| **CV R² (5-fold)** | 0.9360 ± 0.0044 |
| **MAE** | ₹80,355 |
| **RMSE** | ₹132,436 |
| **% predictions within ±10%** | 52.0% |
| **% predictions within ±20%** | 81.4% |

---

## 🚀 Live Demo

```bash
# Clone → Install → Run in 3 steps
git clone https://github.com/yourusername/car-price-prediction.git
cd car-price-prediction
pip install -r requirements.txt && streamlit run app.py
```

Open **http://localhost:8501** in your browser.

---

## 📊 Dataset

- **Source:** CarDekho Used Car Listings
- **Records:** 15,411 entries → 14,353 after cleaning and outlier treatment
- **Target:** `selling_price` (INR)
- **Features:** brand, vehicle_age, km_driven, seller_type, fuel_type, transmission_type, mileage, engine, max_power, seats

### Feature Description

| Feature | Type | Description |
|---------|------|-------------|
| `brand` | Categorical | Car manufacturer — 25 unique brands after cleaning (Maruti, Hyundai, BMW, etc.) |
| `vehicle_age` | Numerical | Age of the car in years |
| `km_driven` | Numerical | Total kilometers driven |
| `seller_type` | Categorical | Dealer / Individual / Trustmark Dealer |
| `fuel_type` | Categorical | Petrol / Diesel / CNG / LPG / Electric |
| `transmission_type` | Categorical | Manual / Automatic |
| `mileage` | Numerical | Fuel efficiency (kmpl) — set 0 for Electric |
| `engine` | Numerical | Engine displacement (cc) |
| `max_power` | Numerical | Peak power output (bhp) |
| `seats` | Numerical | Number of seating positions (2–9) |
| `selling_price` | **Target** | Resale price in Indian Rupees (₹) |

---


## 📂 Project Structure

```
Car_Price_Prediction/
│
├── 📓 Car_Price_Prediction.ipynb   ← Full ML notebook (53 cells, pre-executed)
├── 🌐 app.py                       ← Streamlit web application
├── 📦 requirements.txt             ← All Python dependencies
├── 📖 README.md                    ← This file
├── 🧪 test_cases.md                ← 12 structured test cases
│
├── models/
│   ├── model.pkl                   ← Trained LightGBM model (tuned)
│   ├── scaler.pkl                  ← Fitted StandardScaler
│   ├── encoders.pkl                ← LabelEncoders dict (4 columns)
│   └── meta.json                   ← Feature names, cat values, all scores
│
├── data/
│   └── used_car_data.csv           ← Raw dataset (15,411 records)
│
├── assets/                         ← Generated chart PNGs from notebook
│   ├── univariate.png
│   ├── categorical.png
│   ├── bivariate.png
│   ├── multivariate.png
│   ├── outliers.png
│   ├── feature_importance.png
│   ├── model_comparison.png
│   └── residuals.png
│
└── screenshots/                    ← App screenshots
```

---

## 🛠️ Technologies Used

<div align="center">

| Category | Technology |
|----------|-----------|
| Language | Python 3.10+ |
| ML Framework | LightGBM, XGBoost, CatBoost, Scikit-learn |
| Data Processing | Pandas, NumPy, SciPy |
| Visualization | Matplotlib, Seaborn, Plotly |
| Model Serialization | Joblib |
| Web Framework | Streamlit |
| Notebook | Jupyter |

</div>

---

## 🤖 ML Pipeline

```
Raw CSV (15,411 rows, 14 columns)
        │
        ▼
  Data Cleaning          → Drop IDs, remove 168 duplicates, drop invalid rows
        │
        ▼
  Outlier Treatment      → Winsorization (1st–99th percentile, -888 rows)
        │
        ▼
  Feature Engineering    → 5 derived features (no target leakage)
        │
        ▼
  Label Encoding         → 4 categorical columns
        │
        ▼
  StandardScaler         → Normalize all 15 features
        │
        ▼
  Train/Test Split       → 80% train (11,482) / 20% test (2,871), random_state=42
        │
        ▼
  Train 11 Models        → Compare R², MAE, RMSE, Adj R²
        │
        ▼
  RandomizedSearchCV     → Tune LightGBM (40 iter, 3-fold CV)
        │
        ▼
  5-Fold Cross Validation → Final stability check
        │
        ▼
  Serialize Artifacts    → model.pkl, scaler.pkl, encoders.pkl, meta.json
        │
        ▼
  Streamlit App          → Load artifacts → predict → display
```

---

## 🔨 What Was Built

This project was built entirely from scratch, covering every stage of a professional ML workflow:

### ✅ Phase 1 — Data Pipeline
- Loaded and inspected 15,411 car listings across 14 columns
- Dropped identifier columns (`Unnamed: 0`, `car_name`, `model`)
- Removed 168 duplicate rows and all invalid entries (zero/negative price, km, engine, power, seats)
- Stripped whitespace from all string columns
- Applied 1st–99th percentile Winsorization on price, km, engine, and power (removed 888 extreme outliers)

### ✅ Phase 2 — Exploratory Data Analysis
- **Univariate analysis** — histograms + KDE plots for all numerical features
- **Bivariate analysis** — scatter plots, box plots, violin plots
- **Multivariate analysis** — correlation heatmap, brand-wise price comparison
- Generated **8 publication-quality chart assets** saved to `assets/`

### ✅ Phase 3 — Feature Engineering
Created 5 derived features — **none of which use the target variable**, avoiding data leakage at inference time:

| Feature | Formula | Why |
|---------|---------|-----|
| `power_per_engine` | `max_power / (engine + 1)` | Performance-to-displacement ratio |
| `age_km` | `vehicle_age × km_driven` | Combined wear/depreciation indicator |
| `log_km` | `log1p(km_driven)` | Reduces right-skew of km distribution |
| `engine_age` | `engine × vehicle_age` | Engine size weighted by age |
| `power_age` | `max_power / (vehicle_age + 1)` | Power retention relative to age |

> ⚠️ **Note:** An earlier version of this project included a `price_per_km` feature (`selling_price / km_driven`). This was **removed** because it directly derives from the target variable — at real prediction time the price is unknown, so this feature can't exist outside training, and including it caused severely distorted predictions in production. All 5 features above are safe because they only use input fields the user actually provides.

### ✅ Phase 4 — Encoding & Scaling
- **Label Encoding** applied to all 4 categorical columns (`brand`, `seller_type`, `fuel_type`, `transmission_type`) — compatible with tree-based models
- **StandardScaler** applied to all 15 features

### ✅ Phase 5 — Model Training (11 Algorithms)
Trained and evaluated every major regression algorithm on an 80/20 split (11,482 train / 2,871 test samples).

### ✅ Phase 6 — Hyperparameter Tuning
- **RandomizedSearchCV** with 40 iterations, 3-fold CV on LightGBM
- Parameters tuned: `n_estimators`, `max_depth`, `learning_rate`, `num_leaves`, `subsample`, `colsample_bytree`, `min_child_samples`, `reg_alpha`, `reg_lambda`
- Tuning improved R² only marginally (0.9376 → 0.9377), confirming the baseline configuration was already near-optimal

### ✅ Phase 7 — Model Diagnostics
- Residual plot, Predicted vs Actual scatter, Error distribution histogram
- **52.0%** of predictions fall within ±10% of actual price; **81.4%** fall within ±20%

### ✅ Phase 8 — Artifact Serialization
Saved `model.pkl`, `scaler.pkl`, `encoders.pkl`, `meta.json` for production use.

### ✅ Phase 9 — Streamlit Web Application
Full-featured dual-theme frontend with persistent form state.

### ✅ Phase 10 — Testing
12 structured test cases covering all categories, fuel types, seller types, and edge cases.

---

## 🏆 Model Results

All 11 models trained and evaluated on the same 80/20 split (test set: 2,871 samples):

| Rank | Model | R² Score | Adj R² | MAE (₹) | RMSE (₹) |
|------|-------|:--------:|:------:|--------:|---------:|
| 🥇 | **LightGBM** | **0.9376** | **0.9373** | **80,355** | **132,436** |
| 🥈 | XGBoost | 0.9359 | 0.9355 | 80,646 | 134,247 |
| 🥉 | CatBoost | 0.9309 | 0.9306 | 85,705 | 139,332 |
| 4 | Random Forest | 0.9247 | 0.9243 | 84,721 | 145,450 |
| 5 | Extra Trees | 0.9200 | 0.9196 | 88,855 | 149,936 |
| 6 | Gradient Boosting | 0.9109 | 0.9104 | 97,557 | 158,260 |
| 7 | Decision Tree | 0.8793 | 0.8786 | 98,287 | 184,198 |
| 8 | AdaBoost | 0.8132 | 0.8122 | 154,139 | 229,105 |
| 9 | Linear Regression | 0.7673 | 0.7660 | 161,566 | 255,742 |
| 10 | Lasso Regression | 0.7673 | 0.7660 | 161,466 | 255,748 |
| 11 | Ridge Regression | 0.7672 | 0.7660 | 161,435 | 255,766 |

**Cross-validation (5-fold) on LightGBM:** `0.9360 ± 0.0044` — confirms stable, consistent performance with no overfitting.

> Tree-based ensembles significantly outperform linear models (R² ≈ 0.77 for linear vs. R² ≈ 0.94 for LightGBM), confirming that car pricing is inherently non-linear with respect to these features.

---

## ⚙️ Feature Engineering

Top 5 features by importance in the final tuned LightGBM model:

```
mileage             ████████████████████  #1 — 1,882
age_km              █████████████████     #2 — 1,543
km_driven           ████████████████      #3 — 1,454
power_age           ██████████████        #4 — 1,272
power_per_engine    ████████████          #5 — 1,150
```

Usage and depreciation signals (`mileage`, `age_km`, `km_driven`) dominate the model — confirming that how much a car has been driven and for how long matters more than raw engine specs alone.

---

## 🔍 Residual Analysis

| Metric | Value |
|--------|-------|
| Mean Residual | ₹321 (≈ 0, as expected for an unbiased model) |
| Std of Residuals | ₹132,374 |
| % predictions within ±10% of actual price | 52.0% |
| % predictions within ±20% of actual price | 81.4% |

See `assets/residuals.png` for the full Predicted vs Actual plot, residual scatter, and error distribution histogram.

---

## 🌐 Streamlit App

A fully-featured, production-ready web application at `app.py`.

### Features

| Feature | Description |
|---------|-------------|
| 🌙 **Dual Theme** | Light / Dark mode toggle — full CSS theming, persists across predictions |
| 🎨 **Top Bar Theming** | Deploy toolbar changes color with theme |
| 🔧 **Input Form** | All 10 car features with dropdowns, sliders, number inputs |
| 💾 **Persistent State** | +/− buttons on number inputs never reset other fields |
| 💰 **Price Card** | Animated green result card with ₹ amount + lakh conversion |
| 📊 **Confidence Range** | ±5% price range displayed per prediction |
| 📋 **Prediction History** | Session-based table with highest/lowest/average stats |
| 🗑️ **Clear History** | Dedicated sidebar button — only this clears history |
| 🏆 **Model Ranking** | Live top-5 model leaderboard in sidebar |
| 📈 **Price Drivers** | 8 key factors explained with business context |

### Screenshots

| Light Theme | Dark Theme |
|:-----------:|:----------:|
| *(add screenshot)* | *(add screenshot)* |

---

## 🧪 Test Cases

12 structured test cases covering all scenarios. Run these in the app to verify correctness:

| TC | Description | Category | Expected Price |
|----|-------------|----------|---------------:|
| TC01 | Maruti, 8yr, 85K km, Petrol, Manual | 🟢 Budget | ₹2,69,428 |
| TC02 | Honda, 4yr, 45K km, Petrol, Manual | 🔵 Mid-range | ₹8,11,211 |
| TC03 | Hyundai, 3yr, 30K km, Diesel, Auto, 7-seat | 🟠 Premium | ₹20,24,066 |
| TC04 | BMW, 2yr, 18K km, Diesel, Auto | 🟣 Luxury | ₹34,82,137 |
| TC05 | Jaguar, 1yr, 8K km, 296bhp, Diesel | 🟣 Luxury | ₹33,81,736 |
| TC06 | Maruti, 15yr, 2L km — max depreciation | 🔴 Edge case | ₹1,49,935 |
| TC07 | Tata Electric, mileage=0.0 | 🔴 Edge case | ₹15,22,314 |
| TC08 | Hyundai CNG — rare fuel type | 🔴 Edge case | ₹4,63,865 |
| TC09 | Toyota, 8-seat MUV, large diesel | 🔵 Mid-range | ₹14,40,709 |
| TC10 | Ford, Trustmark Dealer seller type | 🟠 Premium | ₹8,27,232 |
| TC11 | Audi, 1yr, 5K km, Petrol Auto | 🟣 Luxury | ₹35,06,699 |
| TC12 | Honda, 7yr, 1.3L km, Individual | 🔴 Edge case | ₹4,95,458 |

See [`test_cases.md`](test_cases.md) for full field-by-field values and verification checklist.

---

## 🚀 Installation & Setup

### Prerequisites
- Python **3.10+**
- pip package manager
- Git (optional)

### Setup

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/car-price-prediction.git
cd car-price-prediction

# 2. Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt
```

---

## 📓 Running the Notebook

```bash
jupyter notebook Car_Price_Prediction.ipynb
```

Run all cells top-to-bottom. The notebook will:
1. Load and clean the dataset
2. Perform EDA with publication-quality visualizations
3. Engineer 5 leak-free features
4. Train and evaluate 11 regression models
5. Tune the best model with RandomizedSearchCV
6. Save model artifacts to `models/`

---

## 🌐 Running the Streamlit App

Ensure the notebook has been run first (to generate model files in `models/`), then:

```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`

---

## ☁️ Deployment

### Push to GitHub
```bash
git init
git add .
git commit -m "🚀 Initial commit: Car Price Prediction System"
git remote add origin https://github.com/yourusername/car-price-prediction.git
git push -u origin main
```

### Deploy on Streamlit Community Cloud
1. Push your repo to GitHub (include the `models/` folder)
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Select the repository → set **Main file path** to `app.py`
5. Click **Deploy** 🚀

> If model `.pkl` files exceed 100MB, use [Git LFS](https://git-lfs.com). This model is ~1.2MB, so it pushes normally.

---

## 🔮 Future Scope

- [ ] **SHAP explainability** — per-prediction force plots so users understand *why*
- [ ] **REST API** — FastAPI endpoint for mobile/web app integration
- [ ] **Hugging Face Spaces** deployment
- [ ] **Live data pipeline** — integrate a live CarDekho-style API for real-time data
- [ ] **Image input** — estimate condition from car photos using a CNN
- [ ] **Price trend forecasting** — time-series analysis for seasonal patterns
- [ ] **Ensemble stacking** — LightGBM + XGBoost + CatBoost meta-learner

---

## 📄 License

This project is licensed under the [`MIT License`](LICENSE) — feel free to use, modify, and distribute.

---

<div align="center">

**⭐ If you found this project useful, please consider giving it a star!**

Built with ❤️ using Python · LightGBM · Streamlit

</div>
