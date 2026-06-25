<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=28&pause=1000&color=2563EB&center=true&vCenter=true&width=600&lines=🚗+Car+Price+Prediction+System;mmmmMachine+Learning+%7C+LightGBM+%7C+Streamlit" alt="Typing SVG" />

<br/>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![LightGBM](https://img.shields.io/badge/LightGBM-Best_Model-2ecc71?style=for-the-badge&logo=leaflet&logoColor=white)](https://lightgbm.readthedocs.io)
[![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML_Pipeline-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org)

<br/>

[![R² Score](https://img.shields.io/badge/R²_Score-0.9878-brightgreen?style=flat-square)]()
[![CV Score](https://img.shields.io/badge/CV_R²-0.9898_±_0.0012-blue?style=flat-square)]()
[![Models](https://img.shields.io/badge/Models_Tested-11-purple?style=flat-square)]()
[![Records](https://img.shields.io/badge/Training_Records-14%2C956-orange?style=flat-square)]()
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

<br/>

> **An end-to-end industry-grade machine learning system** that predicts used car resale prices with **98.78% accuracy** — featuring a complete ML pipeline, 11 algorithms, hyperparameter tuning, and a professional dual-theme Streamlit web application.

</div>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Live Demo](#-live-demo)
- [What Was Built](#-what-was-built)
- [Project Structure](#-project-structure)
- [Dataset](#-dataset)
- [ML Pipeline](#-ml-pipeline)
- [Model Results](#-model-results)
- [Feature Engineering](#-feature-engineering)
- [Streamlit App](#-streamlit-app)
- [Test Cases](#-test-cases)
- [Installation](#-installation)
- [Running the Project](#-running-the-project)
- [Deployment](#-deployment)
- [Future Scope](#-future-scope)
- [Author](#-author)

---

## 🎯 Overview

The used car market in India is worth billions of dollars yet pricing remains inconsistent — buyers overpay, sellers undervalue. This project solves that with a **data-driven ML system** trained on 15,000+ real-world CarDekho listings.

| Attribute | Details |
|-----------|---------|
| **Problem Type** | Supervised Regression |
| **Target Variable** | `selling_price` (INR) |
| **Dataset Size** | 15,411 entries → 14,956 after cleaning |
| **Best Model** | LightGBM |
| **R² Score** | 0.9878 |
| **CV R² (5-fold)** | 0.9898 ± 0.0012 |
| **MAE** | ₹25,279 |
| **RMSE** | ₹58,634 |

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

## 🔨 What Was Built

This project was built entirely from scratch covering every stage of a professional ML workflow:

### ✅ Phase 1 — Data Pipeline
- Loaded and inspected 15,411 car listings
- Removed duplicates, null values, and invalid entries
- Fixed data types and stripped whitespace
- Applied 1st–99th percentile Winsorization for outlier treatment

### ✅ Phase 2 — Exploratory Data Analysis
- **Univariate analysis** — histograms + KDE plots for all numerical features
- **Bivariate analysis** — scatter plots, box plots, violin plots
- **Multivariate analysis** — correlation heatmap, brand-wise price comparison
- Generated **8 publication-quality chart assets** saved to `assets/`

### ✅ Phase 3 — Feature Engineering
Created 4 derived features that significantly boosted model performance:

| Feature | Formula | Why |
|---------|---------|-----|
| `price_per_km` | `selling_price / (km_driven + 1)` | Value relative to usage — #1 predictor |
| `power_per_engine` | `max_power / (engine + 1)` | Performance-to-displacement ratio |
| `age_km` | `vehicle_age × km_driven` | Combined wear indicator |
| `log_km` | `log1p(km_driven)` | Reduces right-skew of km distribution |

### ✅ Phase 4 — Encoding & Scaling
- **Label Encoding** applied to all 4 categorical columns (`brand`, `seller_type`, `fuel_type`, `transmission_type`) — compatible with tree-based models
- **StandardScaler** applied to all features for linear model compatibility

### ✅ Phase 5 — Model Training (11 Algorithms)
Trained and evaluated every major regression algorithm side-by-side.

### ✅ Phase 6 — Hyperparameter Tuning
- **RandomizedSearchCV** with 30 iterations, 3-fold CV on LightGBM
- Parameters tuned: `n_estimators`, `max_depth`, `learning_rate`, `subsample`, `colsample_bytree`, `num_leaves`, `min_child_samples`

### ✅ Phase 7 — Model Diagnostics
- Residual plot, Predicted vs Actual scatter, Error distribution histogram
- **92%** of predictions fall within ±10% of actual price

### ✅ Phase 8 — Artifact Serialization
Saved `model.pkl`, `scaler.pkl`, `encoders.pkl`, `meta.json` for production use.

### ✅ Phase 9 — Streamlit Web Application
Full-featured dual-theme frontend with persistent form state.

### ✅ Phase 10 — Testing
12 structured test cases covering all categories, fuel types, seller types, and edge cases.

---

## 📂 Project Structure

```
Car_Price_Prediction/
│
├── 📓 Car_Price_Prediction.ipynb   ← Full ML notebook (27 cells, pre-executed)
├── 🌐 app.py                       ← Streamlit web application (744 lines)
├── 📦 requirements.txt             ← All Python dependencies (pinned)
├── 📖 README.md                    ← This file
├── 🧪 test_cases.md                ← 12 structured test cases
│
├── models/
│   ├── model.pkl                   ← Trained LightGBM model
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

## 📊 Dataset

- **Source:** CarDekho Used Car Listings
- **Records:** 15,411 entries (14,956 after cleaning)
- **Target:** `selling_price` (INR)
- **Features:** brand, vehicle_age, km_driven, seller_type, fuel_type, transmission_type, mileage, engine, max_power, seats, selling_price

### Feature Description

| Feature | Type | Description |
|---------|------|-------------|
| `brand` | Categorical | Car manufacturer (Maruti, Hyundai, BMW, etc.) |
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

## 🤖 ML Pipeline

```
Raw CSV (15,411 rows)
        │
        ▼
  Data Cleaning          → Remove duplicates, nulls, invalids
        │
        ▼
  Outlier Treatment      → Winsorization (1st–99th percentile)
        │
        ▼
  Feature Engineering    → 4 derived features added
        │
        ▼
  Label Encoding         → 4 categorical columns
        │
        ▼
  StandardScaler         → Normalize all features
        │
        ▼
  Train/Test Split       → 80% train / 20% test (random_state=42)
        │
        ▼
  Train 11 Models        → Compare R², MAE, RMSE, Adj R²
        │
        ▼
  RandomizedSearchCV     → Tune LightGBM (30 iter, 3-fold CV)
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

## 🏆 Model Results

All 11 models trained and evaluated on the same 80/20 split:

| Rank | Model | R² Score | MAE (₹) | RMSE (₹) |
|------|-------|:--------:|--------:|--------:|
| 🥇 | **LightGBM** | **0.9878** | **25,279** | **58,634** |
| 🥈 | XGBoost | 0.9871 | 23,900 | 60,259 |
| 🥉 | Random Forest | 0.9819 | 25,663 | 71,281 |
| 4 | CatBoost | 0.9807 | 38,505 | 73,553 |
| 5 | Extra Trees | 0.9719 | 40,697 | 88,822 |
| 6 | Gradient Boosting | 0.9609 | 65,272 | 104,822 |
| 7 | Decision Tree | 0.9584 | 54,482 | 108,186 |
| 8 | Ridge Regression | 0.8145 | 142,982 | 228,343 |
| 9 | Lasso Regression | 0.8143 | 143,124 | 228,422 |
| 10 | Linear Regression | 0.8142 | 143,265 | 228,503 |
| 11 | AdaBoost | 0.7152 | 249,585 | 282,928 |

**Cross-validation (5-fold) on LightGBM:** `0.9898 ± 0.0012` — confirms no overfitting.

> Tree-based ensembles significantly outperform linear models, confirming that car pricing is inherently non-linear.

---

## ⚙️ Feature Engineering

Feature importance from the final LightGBM model:

```
price_per_km        ████████████████████  #1 — strongest signal
log_km              ████████████████      #2
age_km              ████████████          #3
max_power           ███████████           #4
engine              █████████             #5
vehicle_age         ████████              #6
km_driven           ███████               #7
brand               ██████                #8
power_per_engine    █████                 #9
mileage             ████                  #10
fuel_type           ███                   #11
transmission_type   ██                    #12
seller_type         ██                    #13
seats               █                     #14
```

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
|----|-------------|----------|---------------|
| TC01 | Maruti, 8yr, 85K km, Petrol, Manual | Budget | ₹1,62,956 |
| TC02 | Honda, 4yr, 45K km, Petrol, Manual | Mid-range | ₹1,98,427 |
| TC03 | Hyundai, 3yr, 30K km, Diesel, Auto, 7-seat | Premium | ₹4,24,246 |
| TC04 | BMW, 2yr, 18K km, Diesel, Auto | Luxury | ₹4,96,203 |
| TC05 | Jaguar, 1yr, 8K km, 296bhp, Diesel | Ultra Luxury | ₹4,62,763 |
| TC06 | Maruti, 15yr, 2L km — max depreciation | ⚠️ Edge | ₹1,80,150 |
| TC07 | Tata Electric, mileage=0.0 | ⚠️ Edge | ₹1,30,253 |
| TC08 | Hyundai CNG — rare fuel type | ⚠️ Edge | ₹1,97,395 |
| TC09 | Toyota, 8-seat MUV, large diesel | Mid-range | ₹4,98,286 |
| TC10 | Ford, Trustmark Dealer seller type | Premium | ₹1,89,738 |
| TC11 | Audi, 1yr, 5K km, Petrol Auto | Luxury | ₹3,90,276 |
| TC12 | Honda, 7yr, 1.3L km, Individual | ⚠️ Edge | ₹2,17,783 |

See [`test_cases.md`](test_cases.md) for full field-by-field values.

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
2. Perform EDA with 20+ visualizations
3. Train 11 regression models
4. Evaluate and compare all models
5. Tune the best model
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
1. Push your repo to GitHub (include `models/` folder)
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Select the repository → set **Main file path** to `app.py`
5. Click **Deploy** 🚀

> If model `.pkl` files exceed 100MB, use [Git LFS](https://git-lfs.com). Otherwise they push normally.

---

## 🔮 Future Scope

- [ ] **SHAP explainability** — per-prediction force plots so users understand *why*
- [ ] **REST API** — FastAPI endpoint for mobile/web app integration
- [ ] **Hugging Face Spaces** deployment
- [ ] **Live data pipeline** — Integrate live CarDekho API for real-time data
- [ ] **Image input** — estimate condition from car photos using CNN
- [ ] **Price trend forecasting** — time-series analysis for seasonal patterns

---

## 🛠️ Technologies Used

<div align="center">

| Category | Technology |
|-------|-----------|
| Language | Python 3.10+ |
| ML Framework | LightGBM, XGBoost, CatBoost, Scikit-learn |
| Data Processing | Pandas, NumPy, SciPy |
| Visualization | Matplotlib, Seaborn, Plotly |
| Model Serialization | Joblib |
| Web Framework | Streamlit |
| Notebook | Jupyter |

</div>

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute.

---

<div align="center">

**⭐ If you found this project useful, please consider giving it a star!**

Built with ❤️ using Python · LightGBM · Streamlit

</div>
