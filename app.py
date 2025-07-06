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

# NSE Stocks - Hardcoded symbols for now
stock_symbols = [
    "RELIANCE.NS", "INFY.NS", "TCS.NS", "HDFCBANK.NS", "ICICIBANK.NS",
    "LT.NS", "SBIN.NS", "AXISBANK.NS", "HINDUNILVR.NS", "ITC.NS",
