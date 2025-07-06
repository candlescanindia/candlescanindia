import streamlit as st
import pandas as pd
import yfinance as yf

st.set_page_config(page_title="CandleScanIndia", layout="wide")
st.title("📊 CandleScanIndia")
st.caption("India’s Real-Time NSE Candlestick Pattern Scanner")

# Sidebar
with st.sidebar:
    st.header("📘 About")
    st.markdown("""
    **CandleScanIndia** scans NSE stocks for popular candlestick patterns using real-time Yahoo Finance data.
    
    - Real-time pattern detection  
    - Filter by volume and market cap  
    - Mobile-friendly and fast  
    """)
    st.markdown("---")
    st.markdown("🔗 [Follow us](https://twitter.com)")

# User Inputs
patterns = [
    "Hammer", "Inverted Hammer", "Doji", "Bullish Engulfing", "Bearish Engulfing",
    "Shooting Star", "Morning Star", "Evening Star"
]

pattern = st.selectbox("📌 Select Candlestick Pattern", patterns)
min_volume = st.number_input("📈 Min Volume (in millions)", value=1.0)
min_market_cap = st.number_input("🏦 Min Market Cap (in crores)", value=10000.0)

# Stocks
stock_symbols = [
    "RELIANCE.NS", "INFY.NS", "TCS.NS", "HDFCBANK.NS", "ICICIBANK.NS", "SBIN.NS", "LT.NS",
    "AXISBANK.NS", "HINDUNILVR.NS", "ITC.NS", "WIPRO.NS", "TATAMOTORS.NS", "BAJFINANCE.NS",
    "ASIANPAINT.NS", "ADANIENT.NS", "KOTAKBANK.NS", "BHARTIARTL.NS", "HCLTECH.NS", "TECHM.NS",
    "SUNPHARMA.NS", "ULTRACEMCO.NS", "POWERGRID.NS", "NTPC.NS", "JSWSTEEL.NS", "COALINDIA.NS"
]

# Pattern Logic Functions
def is_hammer(o, h, l, c):
    body = abs(c - o)
    lower = min(o, c) - l
    upper = h - max(o, c)
    return lower > 2 * body and upper < body

def is_inverted_hammer(o, h, l, c):
    body = abs(c - o)
    upper = h - max(o, c)
    lower = min(o, c) - l
    return upper > 2 * body and lower < body

def is_doji(o, h, l, c):
    return abs(c - o) <= 0.1 * (h - l)

def is_bullish_engulfing(prev_o, prev_c, o, c):
    return prev_c < prev_o and c > o and o < prev_c and c > prev_o

def is_bearish_engulfing(prev_o, prev_c, o, c):
    return prev_c > prev_o and c < o and o > prev_c and c < prev_o

def is_shooting_star(o, h, l, c):
    body = abs(c - o)
    upper = h - max(o, c)
    lower = min(o, c) - l
    return upper > 2 * body and lower < body

def is_morning_star(prv, mid, cur):
    return prv['Close'] < prv['Open'] and \
           mid['Close'] < mid['Open'] and \
           cur['Close'] > cur['Open'] and \
           cur['Close'] > (prv['Close'] + prv['Open']) / 2

def is_evening_star(prv, mid, cur):
    return prv['Close'] > prv['Open'] and \
           mid['Close'] > mid['Open'] and \
           cur['Close'] < cur['Open'] and \
           cur['Close'] < (prv['Close'] + prv['Open']) / 2

# Button
if st.button("🔍 Run Scan"):
    matched = []
    with st.spinner("Scanning..."):
        for symbol in stock_symbols:
            try:
                df = yf.download(symbol, period="10d", interval="1d")
                info = yf.Ticker(symbol).info

                if df is None or len(df) < 4:
                    continue

                # Filter
                vol_million = df['Volume'].iloc[-1] / 1e6
                mcap_crore = info.get('marketCap', 0) / 1e7

                if vol_million < min_volume or mcap_crore < min_market_cap:
                    continue

                o, h, l, c = df.iloc[-2][['Open', 'High', 'Low', 'Close']]
                prev = df.iloc[-3]
                cur = df.iloc[-2]
                mid = df.iloc[-3]

                if (
                    (pattern == "Hammer" and is_hammer(o, h, l, c)) or
                    (pattern == "Inverted Hammer" and is_inverted_hammer(o, h, l, c)) or
                    (pattern == "Doji" and is_doji(o, h, l, c)) or
                    (pattern == "Bullish Engulfing" and is_bullish_engulfing(prev['Open'], prev['Close'], o, c)) or
                    (pattern == "Bearish Engulfing" and is_bearish_engulfing(prev['Open'], prev['Close'], o, c)) or
                    (pattern == "Shooting Star" and is_shooting_star(o, h, l, c)) or
                    (pattern == "Morning Star" and is_morning_star(df.iloc[-4], df.iloc[-3], df.iloc[-2])) or
                    (pattern == "Evening Star" and is_evening_star(df.iloc[-4], df.iloc[-3], df.iloc[-2]))
                ):
                    matched.append(symbol)

            except Exception as e:
                st.error(f"⚠️ Error with {symbol}: {e}")

    if matched:
        st.success(f"✅ {len(matched)} stocks matched: {pattern}")
        st.dataframe(pd.DataFrame(matched, columns=["Matching Stocks"]))
    else:
        st.warning("No matches found.")
