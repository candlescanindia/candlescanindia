# app.py
import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

# --- UI HEADER ---
st.set_page_config(page_title="CandleScanIndia – Candlestick Pattern Scanner", layout="wide")
st.title("📈 CandleScanIndia – Scan NSE Stocks for Candlestick Patterns")
st.markdown("Scan Indian stocks for classic candlestick patterns like Doji, Hammer, Engulfing and more.")

# --- PATTERN DROPDOWN ---
patterns = ["Doji", "Hammer", "Bullish Engulfing", "Bearish Engulfing"]
selected_patterns = st.multiselect("Select Candlestick Pattern(s):", patterns, default=["Doji"])

# --- STOCK LIST ---
nifty_50_symbols = [
    "RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFCBANK.NS", "ICICIBANK.NS",
    "KOTAKBANK.NS", "HINDUNILVR.NS", "SBIN.NS", "AXISBANK.NS", "LT.NS"
]  # Add more later

# --- HELPER: Download historical data ---
def fetch_data(symbol):
    end = datetime.today()
    start = end - timedelta(days=20)
    df = yf.download(symbol, start=start, end=end)
    df.dropna(inplace=True)
    return df

# --- HELPER: Detect Doji (simple version) ---
def is_doji(row):
    return abs(row['Open'] - row['Close']) < 0.1 * (row['High'] - row['Low'])

# --- SCAN BUTTON ---
if st.button("🔍 Scan Stocks"):
    results = []
    for symbol in nifty_50_symbols:
        try:
            df = fetch_data(symbol)
            last_candle = df.iloc[-1]
            match = []

            if "Doji" in selected_patterns and is_doji(last_candle):
                match.append("Doji")
            # Add more pattern conditions here

            if match:
                results.append({
                    "Stock": symbol.replace(".NS", ""),
                    "Matched Pattern(s)": ", ".join(match),
                    "Date": last_candle.name.date()
                })
        except Exception as e:
            st.warning(f"Error fetching {symbol}: {e}")

    if results:
        df_result = pd.DataFrame(results)
        st.success(f"Found {len(df_result)} matching stock(s).")
        st.dataframe(df_result)
    else:
        st.info("No matching stocks found today.")