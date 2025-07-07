# app.py

import streamlit as st
from ui.layout import (
    render_header,
    render_top_controls,
    render_highlights,
    render_results
)

# Sample static scan result – replace with real logic later
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

# ----------------- Streamlit Config -----------------
st.set_page_config(page_title="CandleScan India", layout="wide")

# ----------------- Header -----------------
render_header()

# ----------------- Controls -----------------
duration, selected_pattern, show_filters, scan_now = render_top_controls()

# ----------------- Optional Filter Section -----------------
if show_filters:
    with st.expander("Filter Options", expanded=True):
        st.warning("Coming soon: Sector, Volume, Price Range, etc.")

# ----------------- Scan Action -----------------
if scan_now:
    # You would replace this with filtered results based on selection
    matched_stocks = sample_scan_results
    render_highlights(matched_stocks, selected_pattern)

    # Show as table
    st.markdown("### 📋 Scan Results")
    st.dataframe(
        [{
            "Stock Name": s["name"],
            "Symbol": s["symbol"],
            "LTP (₹)": s["price"],
            "Exchange": s["exchange"],
            "Time": s["time"],
            "Duration": s["duration"],
            "Pattern": s["pattern"]
        } for s in matched_stocks],
        use_container_width=True
    )
