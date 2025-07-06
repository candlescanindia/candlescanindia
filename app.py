import streamlit as st
from utils import nse_data
from scans import candlestick, volume_scans, price_scans, trend_scans, combo_scanner

st.set_page_config(page_title="CandleScan India", layout="wide")

# Load stock data
df_stocks = nse_data.load_stocks()

st.title("🇮🇳 CandleScan India - Indian Stock Market Scanner")
st.success(f"Scanning {len(df_stocks)} stocks from NSE")

# Sections
st.header("🕯️ Candlestick Pattern Scanner")
candlestick.display(df_stocks)

st.header("📊 Volume Based Scans")
volume_scans.display(df_stocks)

st.header("📈 Price Action Scans")
price_scans.display(df_stocks)

st.header("🔥 Trending Stocks")
trend_scans.display()

st.header("🧠 Combine Multiple Scans")
combo_scanner.display(df_stocks)
