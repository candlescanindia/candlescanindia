# app.py

import streamlit as st
from ui.layout import render_header, render_top_controls
from scans.candlestick import run_candlestick_scan
from ui.scan_card import render_scan_result  # Optional: card-style result
# If no card layout yet, comment out above and just print raw results

st.set_page_config(page_title="CandleScan India", layout="wide")
render_header()

# Controls
duration, pattern_type, pattern_selected, show_filters, scan_clicked = render_top_controls()

# Filters (if 🧰 clicked)
min_volume = min_price = max_price = min_rsi = max_rsi = None
if show_filters:
    with st.expander("🔧 Additional Filters", expanded=True):
        col1, col2, col3 = st.columns(3)

        with col1:
            min_volume = st.number_input("Min Volume", min_value=0, value=0, step=1000)
        with col2:
            min_price = st.number_input("Min Price", min_value=0.0, value=0.0, step=1.0)
        with col3:
            max_price = st.number_input("Max Price", min_value=0.0, value=10000.0, step=1.0)

        col4, col5 = st.columns(2)
        with col4:
            min_rsi = st.slider("Min RSI", 0, 100, 0)
        with col5:
            max_rsi = st.slider("Max RSI", 0, 100, 100)

# Run scan
if scan_clicked and pattern_selected:
    st.info(f"Scanning for **{pattern_selected}** pattern ({duration})...")
    with st.spinner("Fetching and analyzing stock data..."):
        results = run_candlestick_scan(
            duration=duration,
            pattern=pattern_selected,
            min_volume=min_volume,
            min_price=min_price,
            max_price=max_price,
            min_rsi=min_rsi,
            max_rsi=max_rsi,
        )

    if results:
        st.success(f"✅ Found {len(results)} matching stock(s).")
        for stock in results:
            render_scan_result(stock)  # pretty card
            # st.write(stock)  # uncomment this line instead if no scan_card yet
    else:
        st.warning("⚠️ No matching stocks found. Try adjusting your filters or pattern.")
