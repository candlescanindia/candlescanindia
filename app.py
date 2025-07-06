import streamlit as st
from scans import candlestick
from utils import nse_data

st.set_page_config(page_title="CandleScan India", layout="wide")

st.title("🕯️ CandleScan India")
st.caption("Smart scanner for Indian stocks based on candlestick patterns")

# Load stock symbols (you can hardcode or use live fetch from NSE)
df_stocks = nse_data.load_stocks()

# Define available candlestick scans
pattern_map = {
    "Hammer": candlestick.scan_hammer,
    "Inverted Hammer": candlestick.scan_inverted_hammer,
    "Bullish Engulfing": candlestick.scan_bullish_engulfing,
    "Bearish Engulfing": candlestick.scan_bearish_engulfing,
    "Morning Star": candlestick.scan_morning_star,
    "Evening Star": candlestick.scan_evening_star,
    "Doji": candlestick.scan_doji,
    "Shooting Star": candlestick.scan_shooting_star,
    "Hanging Man": candlestick.scan_hanging_man,
    "Spinning Top": candlestick.scan_spinning_top
}

# UI selection
with st.container():
    st.markdown("### 🔍 Select a Candlestick Pattern")
    pattern_name = st.selectbox("Choose pattern", list(pattern_map.keys()))
    selected_pattern = pattern_map.get(pattern_name)

# Trigger scan
if st.button("🚀 Scan for Pattern"):
    if selected_pattern:
        results = []
        with st.spinner("Scanning stocks..."):
            for symbol in df_stocks["Symbol"]:
                try:
                    if selected_pattern(symbol):
                        results.append(symbol)
                except Exception as e:
                    st.warning(f"⚠️ Error with {symbol}: {e}")
        st.success(f"✅ Found {len(results)} stocks matching pattern: {pattern_name}")
        st.dataframe(results)
    else:
        st.warning("Please select a valid pattern.")
