import streamlit as st
import pandas as pd

st.set_page_config(page_title="CandleScanIndia", layout="wide")
st.title("📊 CandleScanIndia - NSE Candlestick Pattern Scanner")

# Show detailed error messages
st.set_option('client.showErrorDetails', True)

# 🔧 Hardcoded NSE stock symbols
stock_symbols = [
    "RELIANCE.NS", "INFY.NS", "TCS.NS", "HDFCBANK.NS", "ICICIBANK.NS",
    "LT.NS", "SBIN.NS", "AXISBANK.NS", "HINDUNILVR.NS", "ITC.NS",
    "BAJFINANCE.NS", "BHARTIARTL.NS", "ASIANPAINT.NS", "KOTAKBANK.NS", "WIPRO.NS",
    "ONGC.NS", "HCLTECH.NS", "SUNPHARMA.NS", "ULTRACEMCO.NS", "POWERGRID.NS",
    "NTPC.NS", "TECHM.NS", "TITAN.NS", "JSWSTEEL.NS", "ADANIENT.NS",
    "COALINDIA.NS", "DIVISLAB.NS", "NESTLEIND.NS", "HDFCLIFE.NS", "TATAMOTORS.NS",
    "BPCL.NS", "CIPLA.NS", "BRITANNIA.NS", "HEROMOTOCO.NS", "GRASIM.NS"
]

df = pd.DataFrame(stock_symbols, col_
