# app.py

import streamlit as st
from ui.layout import (
    render_header,
    render_top_controls,
    render_filters,
    render_results,
    render_highlights
)

# -------------------- Page Config --------------------
st.set_page_config(page_title="CandleScan India", layout="wide")

# -------------------- Header --------------------
render_header()

# -------------------- Controls (Duration + Pattern + Filter Icon) --------------------
duration, selected_pattern, show_filters = render_top_controls()

# -------------------- Optional Filters --------------------
if show_filters:
    render_filters()

# -------------------- Placeholder for Scan Button + Logic --------------------
if st.button("🔍 Scan Now"):
    # Placeholder scan logic
    matched_stocks = ["RELIANCE.NS", "TCS.NS", "INFY.NS"]  # Replace with real logic
    render_highlights(matched_stocks, selected_pattern)
    render_results(matched_stocks, selected_pattern)
else:
    st.info("Click 'Scan Now' to start scanning for candlestick patterns.")
