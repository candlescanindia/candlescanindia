# app.py (Full Market Scan)
import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

st.set_page_config(page_title="CandleScanIndia – NSE Candlestick Pattern Scanner", layout="wide")

st.title("📈 CandleScanIndia")
st.markdown("### Scan NSE market for popular candlestick patterns")

# Load all NSE symbols
@st.cache_data
def load_symbols():
    df = pd.read_csv("nse_stocks.csv")
    return df["Symbol"].dropna().tolist()

all_symbols = load_symbols()

# Pattern selection
patterns = [
    "Doji", "Hammer", "Inverted Hammer", "Bullish Engulfing", "Bearish Engulfing",
    "Morning Star", "Evening Star", "Shooting Star", "Hanging Man", "Spinning Top",
    "Marubozu", "Piercing Line", "Dark Cloud Cover"
]
selected_pattern = st.selectbox("🔍 Select Pattern", options=patterns)

# Data fetcher
def fetch_data(symbol):
    try:
        end = datetime.today()
        start = end - timedelta(days=20)
        df = yf.download(symbol, start=start, end=end, progress=False)
        df.dropna(inplace=True)
        return df
    except:
        return pd.DataFrame()

# Pattern functions
def is_doji(row): return abs(row['Open'] - row['Close']) < 0.1 * (row['High'] - row['Low'])
def is_hammer(row): body = abs(row['Close'] - row['Open']); lower = min(row['Open'], row['Close']) - row['Low']; upper = row['High'] - max(row['Open']_
