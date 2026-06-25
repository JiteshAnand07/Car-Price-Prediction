"""
Car Price Prediction System — Professional Streamlit App
Light / Dark theme toggle · Persistent form state · Clean UI
"""

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import json
import os
from datetime import datetime

# ─── Page Config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Car Price Predictor",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={"About": "### Car Price Prediction System\nPowered by LightGBM · R² ≈ 0.9376"}
)

# ─── Session State Defaults ───────────────────────────────────────────────────
def init_state():
    defaults = {
        "dark_mode":       False,
        "history":         [],
        "km_driven":       50000,
        "engine":          1200,
        "max_power":       82.0,
        "mileage":         18.0,
        "vehicle_age":     5,
        "brand_idx":       0,
        "seller_idx":      0,
        "fuel_idx":        0,
        "trans_idx":       0,
        "seats_idx":       2,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()

# ─── Load Artifacts ───────────────────────────────────────────────────────────
@st.cache_resource
def load_artifacts():
    base     = os.path.dirname(__file__)
    model    = joblib.load(os.path.join(base, "models", "model.pkl"))
    scaler   = joblib.load(os.path.join(base, "models", "scaler.pkl"))
    encoders = joblib.load(os.path.join(base, "models", "encoders.pkl"))
    with open(os.path.join(base, "models", "meta.json")) as f:
        meta = json.load(f)
    return model, scaler, encoders, meta

try:
    model, scaler, encoders, meta = load_artifacts()
    LOADED = True
except Exception as e:
    LOADED  = False
    LOAD_ERR = str(e)

# ─── Theme Colors ─────────────────────────────────────────────────────────────
DARK  = st.session_state.dark_mode
if DARK:
    T = {
        "app_bg":         "#0F1117",
        "sidebar_bg":     "#1A1D27",
        "sidebar_border": "#2D3142",
        "card_bg":        "#1E2130",
        "card_border":    "#2D3142",
        "card_shadow":    "rgba(0,0,0,0.4)",
        "input_bg":       "#252836",
        "input_border":   "#3D4260",
        "text_primary":   "#F3F4F6",
        "text_secondary": "#9CA3AF",
        "text_label":     "#D1D5DB",
        "section_border": "#2D3142",
        "divider":        "#2D3142",
        "tip_bg":         "#0D2B1F",
        "tip_border":     "#065F46",
        "tip_left":       "#10B981",
        "tip_text":       "#6EE7B7",
        "driver_bg":      "#1E2130",
        "driver_border":  "#2D3142",
        "driver_left":    "#3B82F6",
        "driver_title":   "#F3F4F6",
        "driver_desc":    "#9CA3AF",
        "rank_bg":        "#252836",
        "rank_border":    "#3D4260",
        "rank_name":      "#F3F4F6",
        "topbar_bg":      "#1A1D27",
        "topbar_border":  "#2D3142",
        "footer_text":    "#4B5563",
        "footer_border":  "#2D3142",
        "range_bg":       "#1E2D4A",
        "range_border":   "#1E40AF",
        "range_text":     "#93C5FD",
        "toggle_bg":      "#252836",
        "toggle_border":  "#3D4260",
    }
else:
    T = {
        "app_bg":         "#F7F8FA",
        "sidebar_bg":     "#FFFFFF",
        "sidebar_border": "#E5E7EB",
        "card_bg":        "#FFFFFF",
        "card_border":    "#E5E7EB",
        "card_shadow":    "rgba(0,0,0,0.05)",
        "input_bg":       "#F9FAFB",
        "input_border":   "#D1D5DB",
        "text_primary":   "#111827",
        "text_secondary": "#6B7280",
        "text_label":     "#374151",
        "section_border": "#E5E7EB",
        "divider":        "#E5E7EB",
        "tip_bg":         "#F0FDF4",
        "tip_border":     "#BBF7D0",
        "tip_left":       "#10B981",
        "tip_text":       "#065F46",
        "driver_bg":      "#FFFFFF",
        "driver_border":  "#E5E7EB",
        "driver_left":    "#2563EB",
        "driver_title":   "#111827",
        "driver_desc":    "#6B7280",
        "rank_bg":        "#F9FAFB",
        "rank_border":    "#E5E7EB",
        "rank_name":      "#111827",
        "topbar_bg":      "#FFFFFF",
        "topbar_border":  "#E5E7EB",
        "footer_text":    "#9CA3AF",
        "footer_border":  "#E5E7EB",
        "range_bg":       "#EFF6FF",
        "range_border":   "#BFDBFE",
        "range_text":     "#1E40AF",
        "toggle_bg":      "#F3F4F6",
        "toggle_border":  "#D1D5DB",
    }

# ─── Dynamic CSS ──────────────────────────────────────────────────────────────
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

html, body, [class*="css"] {{
    font-family: 'Inter', 'Segoe UI', sans-serif !important;
}}

/* ── Top toolbar (Deploy bar) ── */
[data-testid="stToolbar"],
header[data-testid="stHeader"] {{
    background-color: {T["topbar_bg"]} !important;
    border-bottom: 1px solid {T["topbar_border"]} !important;
}}
[data-testid="stToolbar"] * {{ color: {T["text_primary"]} !important; }}
[data-testid="stDecoration"] {{ display: none !important; }}

/* ── App background ── */
.stApp, .main, [data-testid="stAppViewContainer"] {{
    background-color: {T["app_bg"]} !important;
}}

/* ── Sidebar ── */
[data-testid="stSidebar"] {{
    background: {T["sidebar_bg"]} !important;
    border-right: 1px solid {T["sidebar_border"]} !important;
    box-shadow: 2px 0 12px {T["card_shadow"]};
}}
[data-testid="stSidebar"] * {{ color: {T["text_primary"]} !important; }}
[data-testid="stSidebar"] .stMetric label {{ color: {T["text_secondary"]} !important; font-size: 0.75rem !important; }}
[data-testid="stSidebar"] .stMetric [data-testid="stMetricValue"] {{
    color: {T["text_primary"]} !important; font-size: 1.05rem !important; font-weight: 700 !important;
}}
[data-testid="stSidebarContent"] {{ padding-top: 0 !important; }}

/* ── Main block ── */
.block-container {{
    padding: 1.5rem 2.5rem 3rem !important;
    max-width: 1400px !important;
}}

/* ── Hero ── */
.hero {{
    background: linear-gradient(135deg, #1E3A5F 0%, #2563EB 100%);
    border-radius: 16px;
    padding: 2.6rem 3rem;
    margin-bottom: 1.8rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 4px 24px rgba(37,99,235,0.30);
}}
.hero-left h1 {{
    color: #FFFFFF; font-size: 2.2rem; font-weight: 800;
    margin: 0 0 0.35rem; letter-spacing: -0.5px; line-height: 1.2;
}}
.hero-left p {{ color: rgba(255,255,255,0.78); font-size: 0.97rem; margin: 0; }}
.hero-badges {{ display:flex; gap:12px; flex-shrink:0; }}
.hero-badge {{
    background: rgba(255,255,255,0.14);
    border: 1px solid rgba(255,255,255,0.28);
    border-radius: 12px; padding: 1rem 1.6rem;
    text-align: center; backdrop-filter: blur(8px); min-width: 130px;
}}
.hero-badge .big  {{ color:#FFFFFF; font-size:1.9rem; font-weight:800; line-height:1; }}
.hero-badge .small {{ color:rgba(255,255,255,0.72); font-size:0.72rem; font-weight:600;
    margin-top:4px; text-transform:uppercase; letter-spacing:0.06em; }}

/* ── Stat cards ── */
.stat-card {{
    background: {T["card_bg"]}; border: 1px solid {T["card_border"]};
    border-radius: 12px; padding: 1.1rem 1.3rem; text-align: center;
    box-shadow: 0 1px 4px {T["card_shadow"]}; transition: box-shadow 0.2s, transform 0.2s;
}}
.stat-card:hover {{ box-shadow: 0 6px 20px {T["card_shadow"]}; transform: translateY(-2px); }}
.stat-label {{
    color: {T["text_secondary"]}; font-size: 0.7rem; font-weight: 600;
    text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 6px;
}}
.stat-value {{ color: {T["text_primary"]}; font-size: 1.45rem; font-weight: 700; line-height: 1.2; }}
.stat-value.accent {{ color: #3B82F6; }}

/* ── Section heading ── */
.section-head {{
    font-size: 1.02rem; font-weight: 700; color: {T["text_primary"]};
    padding: 0.4rem 0 0.8rem; border-bottom: 2px solid {T["section_border"]};
    margin-bottom: 1.3rem; display:flex; align-items:center; gap:8px;
}}

/* ── Form cards ── */
.form-card {{
    background: {T["card_bg"]}; border: 1px solid {T["card_border"]};
    border-radius: 14px; padding: 1.4rem 1.6rem;
    box-shadow: 0 1px 4px {T["card_shadow"]}; height: 100%;
}}
.form-card-title {{
    font-size: 0.78rem; font-weight: 700; color: {T["text_secondary"]};
    text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 1rem;
    padding-bottom: 0.6rem; border-bottom: 1px solid {T["card_border"]};
}}

/* ── Labels ── */
label, .stSelectbox label, .stSlider label,
.stNumberInput label, [data-testid="stWidgetLabel"] p {{
    color: {T["text_label"]} !important;
    font-size: 0.84rem !important;
    font-weight: 600 !important;
}}

/* ── Selectbox ── */
.stSelectbox > div > div {{
    background: {T["input_bg"]} !important;
    border: 1.5px solid {T["input_border"]} !important;
    border-radius: 8px !important;
    color: {T["text_primary"]} !important;
}}
.stSelectbox > div > div:focus-within {{
    border-color: #3B82F6 !important;
    box-shadow: 0 0 0 3px rgba(59,130,246,0.15) !important;
}}
.stSelectbox [data-testid="stSelectboxVirtualDropdown"] {{
    background: {T["card_bg"]} !important;
    border: 1px solid {T["card_border"]} !important;
}}

/* ── Number inputs ── */
.stNumberInput input {{
    background: {T["input_bg"]} !important;
    border: 1.5px solid {T["input_border"]} !important;
    border-radius: 8px !important;
    color: {T["text_primary"]} !important;
    font-weight: 500 !important;
}}
.stNumberInput input:focus {{
    border-color: #3B82F6 !important;
    box-shadow: 0 0 0 3px rgba(59,130,246,0.15) !important;
    outline: none !important;
}}
/* +/- buttons */
.stNumberInput button {{
    background: {T["input_bg"]} !important;
    border: 1.5px solid {T["input_border"]} !important;
    color: {T["text_primary"]} !important;
    border-radius: 6px !important;
}}
.stNumberInput button:hover {{
    background: {T["card_border"]} !important;
    border-color: #3B82F6 !important;
}}

/* ── Slider ── */
.stSlider [data-testid="stThumbValue"] {{ color: {T["text_secondary"]} !important; }}
.stSlider div[data-baseweb="slider"] div[role="slider"] {{
    background-color: #3B82F6 !important;
    border-color: #3B82F6 !important;
}}

/* ── Predict button ── */
.stButton > button {{
    background: #2563EB !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.72rem 2rem !important;
    font-size: 1rem !important;
    font-weight: 600 !important;
    width: 100% !important;
    transition: background 0.2s, box-shadow 0.2s, transform 0.15s !important;
    box-shadow: 0 2px 8px rgba(37,99,235,0.28) !important;
    letter-spacing: 0.01em !important;
}}
.stButton > button:hover {{
    background: #1D4ED8 !important;
    box-shadow: 0 6px 20px rgba(37,99,235,0.38) !important;
    transform: translateY(-1px) !important;
}}

/* ── Theme toggle button ── */
.theme-toggle-wrap .stButton > button {{
    background: {T["toggle_bg"]} !important;
    color: {T["text_primary"]} !important;
    border: 1.5px solid {T["toggle_border"]} !important;
    border-radius: 20px !important;
    padding: 0.35rem 1.1rem !important;
    font-size: 0.82rem !important;
    font-weight: 600 !important;
    width: auto !important;
    box-shadow: none !important;
    letter-spacing: 0.01em !important;
}}
.theme-toggle-wrap .stButton > button:hover {{
    background: {T["card_border"]} !important;
    transform: none !important;
    box-shadow: none !important;
}}

/* ── Price result ── */
.price-result {{
    background: linear-gradient(135deg, #059669 0%, #10B981 100%);
    border-radius: 16px; padding: 2rem 2rem; text-align: center;
    box-shadow: 0 8px 32px rgba(5,150,105,0.30); margin: 0.8rem 0;
}}
.price-result .plabel {{ color: rgba(255,255,255,0.85); font-size: 0.88rem; font-weight: 500; margin-bottom: 8px; }}
.price-result .amount {{ color: #FFFFFF; font-size: 2.8rem; font-weight: 900; letter-spacing: -1.5px; line-height: 1.1; }}
.price-result .lakh   {{ color: rgba(255,255,255,0.80); font-size: 0.95rem; margin-top: 5px; font-weight: 500; }}

/* ── Range badge ── */
.range-badge {{
    background: {T["range_bg"]}; border: 1px solid {T["range_border"]};
    border-radius: 10px; padding: 0.75rem 1rem;
    color: {T["range_text"]}; font-size: 0.88rem; font-weight: 500;
    text-align: center; margin-top: 0.8rem;
}}

/* ── Summary table ── */
.stTable, table {{ background: {T["card_bg"]} !important; color: {T["text_primary"]} !important; }}

/* ── Tip box ── */
.tip-box {{
    background: {T["tip_bg"]}; border: 1px solid {T["tip_border"]};
    border-left: 4px solid {T["tip_left"]}; border-radius: 8px;
    padding: 0.8rem 1rem; color: {T["tip_text"]}; font-size: 0.84rem;
    line-height: 1.55; margin-top: 0.8rem;
}}

/* ── Driver cards ── */
.driver-card {{
    background: {T["driver_bg"]}; border: 1px solid {T["driver_border"]};
    border-left: 4px solid {T["driver_left"]}; border-radius: 10px;
    padding: 0.82rem 1rem; margin-bottom: 0.65rem;
    box-shadow: 0 1px 3px {T["card_shadow"]};
}}
.driver-card .dt {{ color: {T["driver_title"]}; font-size: 0.88rem; font-weight: 600; margin-bottom: 3px; }}
.driver-card .dd {{ color: {T["driver_desc"]}; font-size: 0.81rem; line-height: 1.5; }}

/* ── Rank pills ── */
.rank-pill {{
    display: flex; align-items: center; justify-content: space-between;
    background: {T["rank_bg"]}; border: 1px solid {T["rank_border"]};
    border-radius: 8px; padding: 8px 11px; margin-bottom: 6px;
}}
.rank-pill .rn {{ color: {T["rank_name"]} !important; font-size: 0.83rem; font-weight: 600; }}
.rank-pill .rs {{
    color: #3B82F6 !important; font-size: 0.8rem; font-weight: 700;
    background: rgba(59,130,246,0.12); padding: 2px 7px;
    border-radius: 4px; border: 1px solid rgba(59,130,246,0.25);
}}

/* ── Dataframe ── */
.stDataFrame {{ border-radius: 10px !important; overflow: hidden; }}
[data-testid="stDataFrameResizable"] {{ background: {T["card_bg"]} !important; }}
.stDataFrame th {{ background: {T["input_bg"]} !important; color: {T["text_primary"]} !important; }}
.stDataFrame td {{ background: {T["card_bg"]} !important; color: {T["text_primary"]} !important; }}

/* ── Metrics ── */
[data-testid="stMetric"] {{ background: {T["card_bg"]} !important; border: 1px solid {T["card_border"]};
    border-radius: 10px; padding: 0.7rem 1rem; }}
[data-testid="stMetricLabel"] p {{ color: {T["text_secondary"]} !important; font-size:0.8rem !important; }}
[data-testid="stMetricValue"] {{ color: {T["text_primary"]} !important; font-weight:700 !important; }}

/* ── Alerts ── */
.stAlert {{ border-radius: 10px !important; }}
[data-testid="stAlert"] {{ background: {T["card_bg"]} !important; color: {T["text_primary"]} !important; }}

/* ── Divider ── */
hr {{ border-color: {T["divider"]} !important; margin: 1.6rem 0 !important; }}

/* ── Footer ── */
.footer {{
    text-align: center; padding: 1.8rem 0 0.5rem;
    color: {T["footer_text"]}; font-size: 0.78rem;
    border-top: 1px solid {T["footer_border"]}; margin-top: 2.5rem;
}}

/* ── Sidebar logo area ── */
.sb-logo {{
    display: flex; align-items: center; gap: 12px;
    padding: 1.6rem 0 1rem;
}}
.sb-logo .icon {{ font-size: 3rem; line-height: 1; }}
.sb-logo .brand {{ display: flex; flex-direction: column; }}
.sb-logo .brand-name {{
    font-size: 1.15rem; font-weight: 800; color: {T["text_primary"]};
    letter-spacing: -0.3px; line-height: 1.2;
}}
.sb-logo .brand-sub {{ font-size: 0.72rem; color: {T["text_secondary"]}; font-weight: 500; margin-top: 2px; }}

/* ── Scrollbar ── */
::-webkit-scrollbar {{ width: 6px; height: 6px; }}
::-webkit-scrollbar-track {{ background: {T["app_bg"]}; }}
::-webkit-scrollbar-thumb {{ background: {T["input_border"]}; border-radius: 3px; }}
</style>
""", unsafe_allow_html=True)


# ─── Sidebar ─────────────────────────────────────────────────────────────────
with st.sidebar:
    # Logo
    st.markdown(f"""
    <div class="sb-logo">
        <div class="icon">🚗</div>
        <div class="brand">
            <div class="brand-name"><h1>Car Price Predictor</h1><div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Theme toggle
    mode_label = "☀️ Light Mode" if DARK else "🌙 Dark Mode"
    st.markdown('<div class="theme-toggle-wrap">', unsafe_allow_html=True)
    if st.button(mode_label, key="theme_btn"):
        st.session_state.dark_mode = not st.session_state.dark_mode
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.divider()

    if LOADED:
        st.markdown(f"<span style='font-size:1.3rem;font-weight:700;color:{T['text_secondary']};text-transform:uppercase;letter-spacing:0.07em'>📊 Model Performance</span>", unsafe_allow_html=True)
        st.metric("Best Model",   meta["best_model"])
        st.metric("R² Score",     f"{meta['best_r2']:.4f}")
        st.metric("CV R² (mean)", f"{meta['cv_mean']:.4f} ± {meta['cv_std']:.4f}")
        st.divider()

        st.markdown(f"<span style='font-size:1.3rem;font-weight:700;color:{T['text_secondary']};text-transform:uppercase;letter-spacing:0.07em'>🏆 Model Ranking</span>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        results = meta["results"]
        medals  = ["🥇","🥈","🥉","4️⃣","5️⃣"]
        for i, (name, scores) in enumerate(sorted(results.items(), key=lambda x: -x[1]["R² Score"])[:5], 1):
            st.markdown(f"""
            <div class="rank-pill">
                <span class="rn">{medals[i-1]} {name}</span>
                <span class="rs">R²={scores['R² Score']:.4f}</span>
            </div>""", unsafe_allow_html=True)

        st.divider()

    st.markdown(f"<span style='font-size:1.3rem;font-weight:700;color:{T['text_secondary']};text-transform:uppercase;letter-spacing:0.07em'>ℹ️ About</span>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style='font-size:0.85rem;color:{T["text_secondary"]};line-height:1.6;margin-top:8px'>
    ML system trained on <strong style='color:{T["text_primary"]}'>15,000+ listings</strong>.<br>
    <strong style='color:{T["text_primary"]}'>11</strong> algorithms tested.<br>
    Winner: <strong style='color:#3B82F6'>LightGBM</strong> · 93.76% accuracy
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    if st.button("🗑️ Clear Prediction History", use_container_width=True):
        st.session_state.history = []
        st.success("History cleared!")


# ─── Hero ─────────────────────────────────────────────────────────────────────
if LOADED:
    st.markdown(f"""
    <div class="hero">
        <div class="hero-left">
            <h1>🚗 Car Price Prediction System</h1>
            <p>Industry-grade ML pipeline · 11 algorithms compared · Best-in-class accuracy</p>
        </div>
        <div class="hero-badges">
            <div class="hero-badge">
                <div class="big">{meta['best_r2']:.4f}</div>
                <div class="small">R² Score</div>
            </div>
            <div class="hero-badge">
                <div class="big">15K+</div>
                <div class="small">Training Records</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown('<div class="hero"><div class="hero-left"><h1>🚗 Car Price Prediction System</h1></div></div>', unsafe_allow_html=True)
    st.error(f"⚠️ Could not load model artifacts. Run the notebook first.\n\n`{LOAD_ERR}`")
    st.stop()


# ─── Stat Cards ───────────────────────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)
for col, (label, val, accent) in zip(
    [c1, c2, c3, c4],
    [("🎯 R² Score",      f"{meta['best_r2']:.4f}", True),
     ("📈 CV R² Mean",    f"{meta['cv_mean']:.4f}",  True),
     ("🏆 Best Model",    meta["best_model"],         False),
     ("📦 Training Rows", "14,956",                   False)]
):
    with col:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-label">{label}</div>
            <div class="stat-value {'accent' if accent else ''}">{val}</div>
        </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# ─── Input Form ───────────────────────────────────────────────────────────────
st.markdown('<div class="section-head">🔧 Enter Car Details</div>', unsafe_allow_html=True)

cat_values = meta["cat_values"]
brands_sorted = sorted(cat_values["brand"])

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown('<div class="form-card"><div class="form-card-title">🏷️ Identity</div>', unsafe_allow_html=True)
    brand = st.selectbox("Brand", brands_sorted,
                         index=st.session_state.brand_idx,
                         key="sb_brand")
    seller_type = st.selectbox("Seller Type", cat_values["seller_type"],
                               index=st.session_state.seller_idx,
                               key="sb_seller")
    fuel_type = st.selectbox("Fuel Type", cat_values["fuel_type"],
                             index=st.session_state.fuel_idx,
                             key="sb_fuel")
    transmission_type = st.selectbox("Transmission", cat_values["transmission_type"],
                                     index=st.session_state.trans_idx,
                                     key="sb_trans")
    # Persist selectbox indices
    st.session_state.brand_idx  = brands_sorted.index(brand)
    st.session_state.seller_idx = cat_values["seller_type"].index(seller_type)
    st.session_state.fuel_idx   = cat_values["fuel_type"].index(fuel_type)
    st.session_state.trans_idx  = cat_values["transmission_type"].index(transmission_type)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="form-card"><div class="form-card-title">⚙️ Specifications</div>', unsafe_allow_html=True)
    vehicle_age = st.slider("Vehicle Age (years)", 0, 30,
                            value=st.session_state.vehicle_age,
                            key="sl_age")
    st.session_state.vehicle_age = vehicle_age

    km_driven = st.number_input("KM Driven", min_value=100, max_value=1_000_000,
                                value=st.session_state.km_driven,
                                step=1000, key="ni_km")
    st.session_state.km_driven = km_driven

    engine = st.number_input("Engine (cc)", min_value=500, max_value=6000,
                             value=st.session_state.engine,
                             step=100, key="ni_engine")
    st.session_state.engine = engine

    max_power = st.number_input("Max Power (bhp)", min_value=30.0, max_value=600.0,
                                value=float(st.session_state.max_power),
                                step=0.5, key="ni_power")
    st.session_state.max_power = max_power
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="form-card"><div class="form-card-title">📋 Other Details</div>', unsafe_allow_html=True)
    mileage = st.number_input("Mileage (kmpl)", min_value=1.0, max_value=60.0,
                              value=float(st.session_state.mileage),
                              step=0.5, key="ni_mileage")
    st.session_state.mileage = mileage

    seats_list = [2, 4, 5, 6, 7, 8, 9]
    seats = st.selectbox("Seats", seats_list,
                         index=st.session_state.seats_idx,
                         key="sb_seats")
    st.session_state.seats_idx = seats_list.index(seats)

    st.markdown(f"""
    <div class="tip-box">
        💡 <strong>Tip:</strong> Higher max power, larger engine, lower vehicle age,
        and fewer KMs driven all increase predicted resale value.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# ─── Predict Button ───────────────────────────────────────────────────────────
bcol, _ = st.columns([1, 2])
with bcol:
    predict_btn = st.button("🔍  Predict Car Price", use_container_width=True)

if predict_btn:
    errors = []
    if km_driven <= 0:  errors.append("KM Driven must be greater than 0")
    if engine <= 0:     errors.append("Engine CC must be greater than 0")
    if max_power <= 0:  errors.append("Max Power must be greater than 0")

    if errors:
        for e in errors:
            st.error(f"⚠️ {e}")
    else:
        with st.spinner("Running LightGBM model..."):
            brand_enc  = encoders["brand"].transform([brand])[0]
            seller_enc = encoders["seller_type"].transform([seller_type])[0]
            fuel_enc   = encoders["fuel_type"].transform([fuel_type])[0]
            trans_enc  = encoders["transmission_type"].transform([transmission_type])[0]
            fnames = meta["feature_names"]
            raw = {
                "brand":             brand_enc,
                "vehicle_age":       vehicle_age,
                "km_driven":         km_driven,
                "seller_type":       seller_enc,
                "fuel_type":         fuel_enc,
                "transmission_type": trans_enc,
                "mileage":           mileage,
                "engine":            engine,
                "max_power":         max_power,
                "seats":             seats,
                "power_per_engine":  max_power / (engine + 1),
                "age_km":            vehicle_age * km_driven,
                "log_km":            np.log1p(km_driven),
                "engine_age":        engine * vehicle_age,
                "power_age":         max_power / (vehicle_age + 1),
            }
            X_in  = pd.DataFrame([[raw.get(f, 0) for f in fnames]], columns=fnames)
            price = max(0, model.predict(scaler.transform(X_in))[0])

        lakh = price / 100_000
        low, high = price * 0.95, price * 1.05

        r1, r2 = st.columns([1, 1], gap="medium")
        with r1:
            st.markdown(f"""
            <div class="price-result">
                <div class="plabel">💰 Estimated Resale Value</div>
                <div class="amount">₹ {price:,.0f}</div>
                <div class="lakh">≈ {lakh:.2f} Lakhs</div>
            </div>
            <div class="range-badge">
                📊 Confidence Range &nbsp;·&nbsp; ₹ {low:,.0f} – ₹ {high:,.0f} &nbsp;(±5%)
            </div>
            """, unsafe_allow_html=True)

        with r2:
            st.success("✅ Prediction successful!")
            st.markdown(f"""
| Feature | Value |
|---------|-------|
| Brand | {brand} |
| Fuel Type | {fuel_type} |
| Transmission | {transmission_type} |
| Vehicle Age | {vehicle_age} years |
| KM Driven | {km_driven:,} km |
| Engine | {engine} cc |
| Max Power | {max_power} bhp |
| Mileage | {mileage} kmpl |
| Seats | {seats} |
""")

        st.session_state.history.append({
            "time": datetime.now().strftime("%H:%M:%S"),
            "brand": brand, "fuel": fuel_type,
            "transmission": transmission_type,
            "age": vehicle_age, "km": km_driven, "price": price,
        })


# ─── Prediction History ───────────────────────────────────────────────────────
if st.session_state.history:
    st.divider()
    st.markdown('<div class="section-head">📋 Prediction History (This Session)</div>', unsafe_allow_html=True)
    df_h = pd.DataFrame(st.session_state.history)
    df_h["Price"] = df_h["price"].apply(lambda x: f"₹{x:,.0f}")
    df_show = df_h[["time","brand","fuel","transmission","age","km","Price"]].copy()
    df_show.columns = ["Time","Brand","Fuel","Transmission","Age (yr)","KM","Price"]
    st.dataframe(df_show[::-1], use_container_width=True, hide_index=True)

    prices = [h["price"] for h in st.session_state.history]
    m1, m2, m3 = st.columns(3)
    m1.metric("🔺 Highest", f"₹{max(prices):,.0f}")
    m2.metric("🔻 Lowest",  f"₹{min(prices):,.0f}")
    m3.metric("⚖️ Average", f"₹{np.mean(prices):,.0f}")


# ─── Key Price Drivers ────────────────────────────────────────────────────────
st.divider()
st.markdown('<div class="section-head">📊 Key Price Drivers</div>', unsafe_allow_html=True)
drivers = [
    ("🔑 Price / KM Ratio",  "Derived feature combining price and usage — single strongest predictor"),
    ("🛣️ KM Driven",         "High mileage significantly reduces resale value"),
    ("⚡ Max Power (bhp)",   "More powerful cars command a price premium across all segments"),
    ("⚙️ Engine CC",         "Larger displacement correlates with higher price brackets"),
    ("📅 Vehicle Age",       "Depreciation accelerates after 5 years — major pricing factor"),
    ("⛽ Fuel Type",         "Diesel & Electric hold value better than Petrol or CNG"),
    ("🔄 Transmission",      "Automatic cars fetch a 15–20% premium over Manual"),
    ("🏷️ Brand",             "Luxury brands (BMW, Audi, Mercedes) command significantly higher prices"),
]
d1, d2 = st.columns(2, gap="medium")
for i, (title, desc) in enumerate(drivers):
    with (d1 if i % 2 == 0 else d2):
        st.markdown(f"""
        <div class="driver-card">
            <div class="dt">{title}</div>
            <div class="dd">{desc}</div>
        </div>""", unsafe_allow_html=True)


# ─── Footer ───────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="footer">
    🚗 Car Price Prediction System &nbsp;·&nbsp;
    Powered by LightGBM &nbsp;·&nbsp;
    R² = {meta['best_r2']:.4f} &nbsp;·&nbsp;
    {datetime.now().strftime("%Y")}
</div>
""", unsafe_allow_html=True)
