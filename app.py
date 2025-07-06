import streamlit as st
import pandas as pd

st.set_page_config(page_title="CandleScanIndia", layout="wide")
st.title("📊 CandleScanIndia")
st.caption("India’s Real-Time NSE Candlestick Pattern Scanner")

# Sidebar info
with st.sidebar:
    st.header("📘 About")
    st.markdown("""
    CandleScanIndia helps you identify popular candlestick patterns in Indian stocks (NSE).

    ✅ Scan entire NSE or filter by index  
    ✅ Real-time pattern detection  
    ✅ Beginner-friendly interface
    """)
    st.markdown("---")
    st.markdown("🔗 [Follow us on Twitter](https://twitter.com)")

# NSE Stocks - Hardcoded
stock_symbols = [
    "RELIANCE.NS", "INFY.NS", "TCS.NS", "HDFCBANK.NS", "ICICIBANK.NS",
    "LT.NS", "SBIN.NS", "AXISBANK.NS", "HINDUNILVR.NS", "ITC.NS",
    "BAJFINANCE.NS", "BHARTIARTL.NS", "ASIANPAINT.NS", "KOTAKBANK.NS", "WIPRO.NS",
    "ONGC.NS", "HCLTECH.NS", "SUNPHARMA.NS", "ULTRACEMCO.NS", "POWERGRID.NS",
    "NTPC.NS", "TECHM.NS", "TITAN.NS", "JSWSTEEL.NS", "ADANIENT.NS",
    "COALINDIA.NS", "DIVISLAB.NS", "NESTLEIND.NS", "HDFCLIFE.NS", "TATAMOTORS.NS",
    "BPCL.NS", "CIPLA.NS", "BRITANNIA.NS", "HEROMOTOCO.NS", "GRASIM.NS"
]

df = pd.DataFrame(stock_symbols, columns=["Symbol"])

# Pattern list
patterns = [
    "Hammer", "Doji", "Inverted Hammer", "Shooting Star", "Bullish Engulfing",
    "Bearish Engulfing", "Morning Star"
