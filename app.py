import streamlit as st
from utils import data_loader
from scans import candlestick
from ui.layout import (
    render_header,
    render_filters,
    render_pattern_selector,
    render_search_bar,
    render_results,
    render_highlights
)

# -------------------- Page Config --------------------
st.set_page_config(page_title="CandleScan India", layout="wide")

# -------------------- Header Section --------------------
render_header()

# -------------------- Load Stock List --------------------
try:
    df_stocks = data_loader.load_stocks()
    stock_list = df_stocks["Symbol"].unique().tolist()  # Ensures uniqueness
except Exception as e:
    st.error(f"Error loading stock list: {e}")
    st.stop()

# -------------------- UI Layout --------------------
col1, col2 = st.columns([2, 1])
with col1:
    duration = st.selectbox("Select Chart Duration", ["15m", "30m", "1d", "1wk"], index=2)
with col2:
    show_filters = render_filters()

selected_pattern = render_pattern_selector()
search_stock = render_search_bar()

# -------------------- Scan Trigger --------------------
if st.button("🔎 Scan Now"):
    with st.spinner("Scanning the market..."):
        matched_stocks = []

        # Dynamically resolve function
        pattern_function_name = f"scan_{selected_pattern.lower().replace(' ', '_')}"
        pattern_function = getattr(candlestick, pattern_function_name, None)

        if pattern_function:
            for symbol in stock_list:
                if search_stock and search_stock.lower() not in symbol.lower():
                    continue
                try:
                    matched = pattern_function(symbol, period="5d")  # Update this for real-time later
                    if matched:
                        matched_stocks.append({
                            "symbol": symbol,
                            "matched_at": matched.get("timestamp") if isinstance(matched, dict) else "Just now"
                        })
                except Exception as e:
                    st.warning(f"⚠️ Error scanning {symbol}: {e}")

            render_results(matched_stocks, selected_pattern)
            render_highlights(matched_stocks, selected_pattern)
        else:
            st.error("❌ Selected pattern is not implemented yet.")
