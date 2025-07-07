import streamlit as st
from ui.layout import (
    render_header,
    render_top_controls,
    render_highlights,
    render_results
)

# -------------------- Page Setup --------------------
st.set_page_config(page_title="CandleScan India", layout="wide")

# -------------------- UI Header --------------------
render_header()

# -------------------- Scan Controls --------------------
duration, selected_pattern, show_filters, scan_clicked = render_top_controls()

# -------------------- Placeholder Stock List --------------------
# Start with a static test list (no stock loading for now)
stock_list = [
    "RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFCBANK.NS", "ITC.NS", "ASIANPAINT.NS",
    "WIPRO.NS", "LTIM.NS", "SBIN.NS", "HINDUNILVR.NS"
]

# -------------------- Scan Execution --------------------
if scan_clicked:
    matched_stocks = []

    # Simulated scan logic (replace with actual candle scan function later)
    for symbol in stock_list:
        if symbol.endswith("N.S") or symbol.startswith("H"):  # Dummy filter
            matched_stocks.append(symbol)

    # Show results
    render_highlights(matched_stocks, selected_pattern)
    render_results(matched_stocks, selected_pattern)
