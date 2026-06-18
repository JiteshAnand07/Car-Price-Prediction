# 🚗 Car Price Prediction System

> **Industry-grade machine learning pipeline** for predicting used car resale prices using 15,000+ real-world listings, 11 regression algorithms, and a polished Streamlit web application.

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://python.org)
[![LightGBM](https://img.shields.io/badge/LightGBM-4.3-green?logo=lightgbm)](https://lightgbm.readthedocs.io)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35-red?logo=streamlit)](https://streamlit.io)
[![R² Score](https://img.shields.io/badge/R²%20Score-0.9897-brightgreen)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

---

## 📋 Project Overview

This end-to-end machine learning project predicts the resale price of used cars based on features like brand, fuel type, vehicle age, kilometers driven, engine size, and power output. The system achieves an R² score of **0.9897**, meaning it explains ~98.97% of variance in car prices.

The project follows a rigorous ML workflow:
- Automated data cleaning & feature engineering
- Extensive EDA with publication-quality visualizations
- 11 regression models compared side-by-side
- Hyperparameter tuning with RandomizedSearchCV
- Residual analysis and model diagnostics
- Production-ready Streamlit web application

---

## ✨ Features

| Feature | Details |
|---------|---------|
| **Dataset** | 15,411 used car listings from CarDekho |
| **Algorithms** | 11 models including XGBoost, LightGBM, CatBoost |
| **Best Model** | LightGBM (R² = 0.9897) |
| **CV Score** | 0.9902 ± 0.0006 (5-Fold) |
| **Frontend** | Dark-themed Streamlit app with prediction history |
| **Explainability** | Feature importance visualization |

---

## 📂 Project Structure

```
Car_Price_Prediction/
│
├── 📓 Car_Price_Prediction.ipynb     ← Main ML notebook
├── 🌐 app.py                         ← Streamlit frontend
├── 📦 requirements.txt               ← Python dependencies
├── 📖 README.md                      ← This file
│
├── models/
│   ├── model.pkl                     ← Trained LightGBM model
│   ├── scaler.pkl                    ← StandardScaler
│   ├── encoders.pkl                  ← LabelEncoders (dict)
│   └── meta.json                     ← Feature names, metrics, cat values
│
├── data/
│   └── used_car_data.csv             ← Dataset
│
├── assets/
│   └── (screenshots, images)
│
└── screenshots/
    └── (app screenshots)
```

---

## 📊 Dataset

- **Source:** CarDekho Used Car Listings
- **Records:** 15,411 entries (14,956 after cleaning)
- **Target:** `selling_price` (INR)
- **Features:** brand, vehicle_age, km_driven, seller_type, fuel_type, transmission_type, mileage, engine, max_power, seats

### Feature Description

| Feature | Type | Description |
|---------|------|-------------|
| `brand` | Categorical | Car manufacturer (Maruti, Hyundai, etc.) |
| `vehicle_age` | Numerical | Age of the car in years |
| `km_driven` | Numerical | Total kilometers driven |
| `seller_type` | Categorical | Dealer / Individual / Trustmark Dealer |
| `fuel_type` | Categorical | Petrol / Diesel / CNG / LPG / Electric |
| `transmission_type` | Categorical | Manual / Automatic |
| `mileage` | Numerical | Fuel efficiency (kmpl) |
| `engine` | Numerical | Engine displacement (cc) |
| `max_power` | Numerical | Peak power output (bhp) |
| `seats` | Numerical | Number of seating positions |

---

## 🛠️ Technologies Used

| Category | Technology |
|----------|-----------|
| Language | Python 3.10+ |
| ML Framework | Scikit-learn, XGBoost, LightGBM, CatBoost |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn, Plotly |
| Model Serialization | Joblib |
| Web Framework | Streamlit |
| Notebook | Jupyter |

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.10 or higher
- pip package manager
- Git (optional)

### Step 1: Clone the repository
```bash
git clone https://github.com/yourusername/car-price-prediction.git
cd car-price-prediction
```

### Step 2: Create virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows
```

### Step 3: Install dependencies
```bash
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

### App Features
- 🎨 Dark-themed modern UI
- 📊 Live model performance metrics
- 🔧 Interactive input form for all car features
- 💰 Instant price prediction with confidence range
- 📋 Session-based prediction history with stats
- 📈 Key price driver explanations
- 🗑️ Reset history button

---

## 🏆 Model Comparison

| Model | R² Score | MAE (₹) | RMSE (₹) |
|-------|----------|---------|---------|
| **LightGBM** ✅ | **0.9897** | **27,645** | **58,137** |
| XGBoost | 0.9878 | 26,534 | 63,124 |
| CatBoost | 0.9812 | 43,627 | 78,471 |
| Random Forest | 0.9781 | 30,616 | 84,696 |
| Extra Trees | 0.9713 | 49,520 | 96,862 |
| Gradient Boosting | 0.9555 | 73,568 | 120,691 |
| Decision Tree | 0.9405 | 69,600 | 139,598 |
| Lasso Regression | 0.7424 | 178,772 | 290,380 |
| Linear Regression | 0.7422 | 178,773 | 290,472 |
| Ridge Regression | 0.7420 | 178,819 | 290,572 |
| AdaBoost | 0.6546 | 294,130 | 336,213 |

---

## 🔮 Feature Importance

Top features influencing car price:
1. 🏅 **Price per KM** — derived feature (most predictive)
2. 🛣️ **KM Driven** — usage history
3. ⚡ **Max Power** — performance indicator
4. ⚙️ **Engine CC** — displacement
5. 📅 **Vehicle Age** — depreciation

---

## ☁️ Deployment

### GitHub
```bash
git init
git add .
git commit -m "🚀 Initial commit: Car Price Prediction System"
git remote add origin https://github.com/yourusername/car-price-prediction.git
git push -u origin main
```

### Streamlit Community Cloud
1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Set `app.py` as the main file
5. Add `requirements.txt` — Streamlit Cloud installs automatically
6. Click **Deploy** 🚀

> **Note:** Include model `.pkl` files in your repo (use Git LFS if >100MB), or add a `setup.sh` script that runs the training pipeline on first boot.

---

## 🔮 Future Scope

- [ ] Add SHAP explainability (force plots per prediction)
- [ ] Deploy on Hugging Face Spaces
- [ ] Integrate live CarDekho API for real-time data
- [ ] Add image-based brand recognition
- [ ] Time-series forecasting for price trends
- [ ] REST API using FastAPI
- [ ] Mobile app integration

---

## 👤 Author

**Jitesh**

---

## 📄 License

This project is licensed under the MIT License.

---

*Built with ❤️ using Python, LightGBM & Streamlit*
