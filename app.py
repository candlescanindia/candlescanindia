import streamlit as st
from utils import data_loader
from scans import candlestick
from ui.components import (
    header_section,
    filter_section,
    pattern_selector,
    result_display,
    highlights_box
)

# Load stock list (can be up to 100-500 depending on performance)
df_stocks = data_loader.load_stocks()
stock_list = df_stocks["symbol"].tolist()

# --- Layout Start ---
st.set_page_config(page_title="CandleScan India", layout="wide")
header_section()

# --- Top Filters ---
col1, col2 = st.columns([2, 1])
with col1:
    duration = st.selectbox("Select Chart Duration", ["15m", "30m", "1d", "1wk"], index=2)
with col2:
    show_filters = filter_section()

# --- Pattern Selection ---
selected_pattern = pattern_selector()

# --- Search Field ---
search_stock = st.text_input("🔍 Search stock symbol", placeholder="Type stock symbol (e.g. RELIANCE)", label_visibility="collapsed")

# --- Scan Button ---
if st.button("🔎 Scan Now"):
    matched_stocks = []
    pattern_function = getattr(candlestick, f"scan_{selected_pattern.lower().replace(' ', '_')}", None)

    if pattern_function:
        for symbol in stock_list:
            if search_stock and search_stock.lower() not in symbol.lower():
                continue
            try:
                matched = pattern_function(symbol, period="5d")  # use duration map later
                if matched:
                    matched_stocks.append(symbol)
            except Exception as e:
                print(f"Error with {symbol}: {e}")

        result_display(matched_stocks, selected_pattern)
        highlights_box(matched_stocks, selected_pattern)
    else:
        st.error("Selected pattern is not available yet.")
