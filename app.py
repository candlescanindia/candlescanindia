import streamlit as st
from ui.layout import (
    render_header,
    render_pattern_selector,
    render_chart_duration_selector,
    render_filters,
    render_highlights
)

# -------------------- Page Setup --------------------
st.set_page_config(page_title="CandleScan India", layout="wide")

# -------------------- Header --------------------
render_header()

# -------------------- Chart Duration & Filters --------------------
col1, col2 = st.columns([2, 1])
with col1:
    selected_duration = render_chart_duration_selector()
with col2:
    filters_applied = render_filters()

# -------------------- Pattern Selection --------------------
selected_pattern = render_pattern_selector()

# -------------------- Scan Button --------------------
if st.button("🔎 Scan Market"):
    st.info(f"Scanning Indian stock market for **{selected_pattern}** pattern using **{selected_duration}** chart...")

    # 🔧 Replace this placeholder with actual pattern scan logic
    matched_stocks = ["RELIANCE", "TCS", "HDFCBANK"]  # Example results

    # -------------------- Highlights Output --------------------
    render_highlights(matched_stocks, selected_pattern)
