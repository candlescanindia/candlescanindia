import streamlit as st
import pandas as pd
import yfinance as yf

st.set_page_config(page_title="CandleScanIndia", layout="wide")
st.title("📊 CandleScanIndia")
st.caption("India’s Real-Time NSE Candlestick Pattern Scanner")

# Sidebar info
with st.sidebar:
    st.header("📘 About")
    st.markdown("""
    **CandleScanIndia** helps you identify candlestick patterns across Indian NSE stocks.

    - 🔍 Real-time scanning with Yahoo Finance
    - 📈 Supports multiple patterns (Hammer, Doji, Engulfing, etc.)
    - 🇮🇳 Focused on Indian Market
    """)
    st.markdown("🔗 [Twitter](https://twitter.com) | [Privacy](#) | [Contact](#)")

# Supported Patterns
patterns = [
    "Hammer", "Doji", "Bullish Engulfing", "Bearish Engulfing"
]

# Hardcoded NSE symbols for MVP
stock_symbols = [
    "RELIANCE.NS", "INFY.NS", "TCS.NS", "HDFCBANK.NS", "ICICIBANK.NS",
    "LT.NS", "SBIN.NS", "AXISBANK.NS", "HINDUNILVR.NS", "ITC.NS",
    "BAJFINANCE.NS", "BHARTIARTL.NS", "ASIANPAINT.NS", "KOTAKBANK.NS", "WIPRO.NS",
    "ONGC.NS", "HCLTECH.NS", "SUNPHARMA.NS", "ULTRACEMCO.NS", "POWERGRID.NS",
    "NTPC.NS", "TECHM.NS", "TITAN.NS", "JSWSTEEL.NS", "ADANIENT.NS",
    "COALINDIA.NS", "DIVISLAB.NS", "NESTLEIND.NS", "HDFCLIFE.NS", "TATAMOTORS.NS",
    "BPCL.NS", "CIPLA.NS", "BRITANNIA.NS", "HEROMOTOCO.NS", "GRASIM.NS"
]

# Pattern selection
selected_pattern = st.selectbox("📌 Select a Candlestick Pattern", patterns)

# Scan trigger
if st.button("🔍 Run Scan"):
    result = []
    with st.spinner("Scanning selected stocks..."):
        for symbol in stock_symbols:
            try:
                data = yf.download(symbol, period="7d", interval="1d")
                if len(data) < 2:
                    continue

                row = data.iloc[-2]  # Use previous day’s candle
                o, h, l, c = row['Open'], row['High'], row['Low'], row['Close']

                # Pattern detection logic
                match = False

                if selected_pattern == "Hammer":
                    body = abs(c - o)
                    lower_shadow = min(o, c) - l
                    upper_shadow = h - max(o, c)
                    match = lower_shadow > 2 * body and upper_shadow < body

                elif selected_pattern == "Doji":
                    match = abs(c - o) <= 0.1 * (h - l)

                elif selected_pattern == "Bullish Engulfing":
                    prev = data.iloc[-3]
                    match = prev['Close'] < prev['Open'] and c > o and o < prev['Close'] and c > prev['Open']

                elif selected_pattern == "Bearish Engulfing":
                    prev = data.iloc[-3]
                    match = prev['Close'] > prev['Open'] and c < o and o > prev['Close'] and c < prev['Open']

                if match:
                    result.append(symbol)

            except Exception as e:
                st.error(f"Error with {symbol}: {str(e)}")

    if result:
        st.success(f"✅ {len(result)} stocks matched {selected_pattern} pattern")
        st.dataframe(pd.DataFrame(result, columns=["Matching Stocks"]))
    else:
        st.warning("No matching patterns found.")
