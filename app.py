import streamlit as st
from scans import candlestick
from utils import data_loader
import pandas as pd

# ------------------ Page Setup ------------------ #
st.set_page_config(page_title="CandleScan India", layout="wide")

st.markdown("<h1 style='text-align: center;'>📊 CandleScan India</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Smart scanner for Indian stocks based on candlestick patterns</p>", unsafe_allow_html=True)
st.divider()

# ------------------ Load Stock Data ------------------ #
with st.spinner("🔄 Loading stock list..."):
    df_stocks = data_loader.load_stocks()  # Load from utils/data_loader.py
    stock_list = df_stocks["symbol"].tolist()

# ------------------ Pattern Dropdown ------------------ #
st.markdown("### 🕯️ Select Candlestick Pattern")

# Pattern mapping to function
candlestick_patterns = {
    "Hammer": candlestick.scan_hammer,
    "Inverted Hammer": candlestick.scan_inverted_hammer,
    "Doji": candlestick.scan_doji,
    "Bullish Engulfing": candlestick.scan_bullish_engulfing,
    "Bearish Engulfing": candlestick.scan_bearish_engulfing,
    "Morning Star": candlestick.scan_morning_star,
    "Evening Star": candlestick.scan_evening_star,
    "Shooting Star": candlestick.scan_shooting_star,
    "Spinning Top": candlestick.scan_spinning_top,
    "Marubozu": candlestick.scan_marubozu
}

selected_pattern = st.selectbox(
    label="",
    options=list(candlestick_patterns.keys()),
    index=0,
    placeholder="Type or select pattern",
    label_visibility="collapsed"
)

# ------------------ Scan Button ------------------ #
if st.button("🔎 Scan Stocks"):
    with st.spinner(f"Scanning {len(stock_list)} stocks for {selected_pattern}..."):
        scan_function = candlestick_patterns[selected_pattern]
        results = []

        for symbol in stock_list:
            try:
                result = scan_function(symbol)
                if result is not None:
                    results.append(result)
            except Exception as e:
                st.warning(f"⚠️ Error with {symbol}: {e}")

        if results:
            st.success(f"✅ Found {len(results)} stocks matching {selected_pattern}")
            result_df = pd.concat(results).reset_index(drop=True)
            st.dataframe(result_df, use_container_width=True)
        else:
            st.info("No matching stocks found.")

# ------------------ Footer ------------------ #
st.divider()
st.markdown("<p style='text-align:center;'>Made with ❤️ for Indian stock traders</p>", unsafe_allow_html=True)
