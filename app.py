import streamlit as st
from utils import data_loader
from scans import candlestick
from ui.layout import (
    header_section,
    filter_section,
    pattern_selector,
    highlights_box
)
from ui.scan_card import result_display

# ------------------------ Setup ------------------------
st.set_page_config(page_title="CandleScan India", layout="wide")

# Header
header_section()

# Load stock list
df_stocks = data_loader.load_stocks()
stock_list = df_stocks["Symbol"].unique().tolist()

# ------------------------ Top Layout ------------------------
col1, col2 = st.columns([2, 1])

# Chart duration selector
with col1:
    duration = st.selectbox("🕒 Chart Duration", ["15m", "30m", "1d", "1wk"], index=2)

# Optional Filters
with col2:
    show_filters = filter_section()  # You can expand this later

# Pattern Selector
selected_pattern = pattern_selector()

# Search Box
search_stock = st.text_input("🔍 Search stock symbol", placeholder="Type symbol (e.g., INFY)", label_visibility="collapsed")

# ------------------------ Scan Action ------------------------
if st.button("🔎 Scan Now", use_container_width=True):
    matched_stocks = []
    pattern_func = getattr(candlestick, f"scan_{selected_pattern.lower().replace(' ', '_')}", None)

    if pattern_func:
        with st.spinner("Scanning market..."):
            for symbol in stock_list:
                if search_stock and search_stock.lower() not in symbol.lower():
                    continue
                try:
                    if pattern_func(symbol, period=duration):
                        matched_stocks.append(symbol)
                except Exception as e:
                    st.warning(f"Error scanning {symbol}: {e}")

        if matched_stocks:
            highlights_box(matched_stocks, selected_pattern)
            result_display(matched_stocks, selected_pattern)
        else:
            st.info("No matching stocks found.")
    else:
        st.error("Selected pattern is not supported.")
