# app.py

import streamlit as st
from datetime import datetime
from ui.layout import (
    render_header,
    render_filters_icon,
    render_highlights_section
)
from ui.scan_card import render_scan_card

# Sample scan result for now — this should come from actual scan logic
sample_scan_results = [
    {
        "symbol": "RELIANCE.NS",
        "name": "Reliance Industries",
        "pattern": "Bullish Engulfing",
        "price": 2825.50,
        "exchange": "NSE",
        "time": "2025-07-07 14:45",
        "duration": "15m"
    },
    {
        "symbol": "TCS.NS",
        "name": "Tata Consultancy Services",
        "pattern": "Hammer",
        "price": 3812.75,
        "exchange": "NSE",
        "time": "2025-07-07 14:45",
        "duration": "15m"
    }
]

# ------------------ Streamlit Page Config ------------------
st.set_page_config(page_title="CandleScan India", layout="wide")

# ------------------ UI Sections ------------------
render_header()
render_filters_icon()

# Scan Controls Section
st.markdown("### 🔍 Scan for Candlestick Patterns")
st.markdown("*Choose your settings and scan across Indian markets.*")

with st.container():
    col1, col2, col3 = st.columns([1.2, 2.5, 1])
    with col1:
        chart_duration = st.selectbox("Chart Duration", ["15m", "30m", "1d", "1wk"], index=0)
    with col2:
        selected_pattern = st.selectbox("Candlestick Pattern", [
            "Bullish Engulfing", "Bearish Engulfing", "Doji",
            "Hammer", "Inverted Hammer", "Morning Star", "Evening Star"
        ])
    with col3:
        st.markdown("<br>", unsafe_allow_html=True)
        scan_now = st.button("🔎 Scan Now")

# ------------------ Scan Results ------------------
if scan_now:
    matched_stocks = sample_scan_results  # Replace with real scan logic
    render_highlights_section(matched_stocks, selected_pattern)

    st.markdown("### 📋 Scan Results")

    # Optional: Display as table
    st.dataframe(
        [{
            "Stock Name": stock["name"],
            "Symbol": stock["symbol"],
            "LTP (₹)": stock["price"],
            "Exchange": stock["exchange"],
            "Time": stock["time"],
            "Duration": stock["duration"],
            "Pattern": stock["pattern"]
        } for stock in matched_stocks],
        use_container_width=True
    )

    # Optional: Render Card View too (uncomment if needed)
    # for stock in matched_stocks:
    #     render_scan_card(stock)
