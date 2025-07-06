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
    """)
    st.markdown("---")

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

# Pattern Logic
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

def is_bullish_engulfing(po, pc, o, c):
    return pc < po and c > o and o < pc and c > po

def is_bearish_engulfing(po, pc, o, c):
    return pc > po and c < o and o > pc and c < po

def is_shooting_star(o, h, l, c):
    body = abs(c - o)
    upper = h - max(o, c)
    lower = min(o, c) - l
    return upper > 2 * body and lower < body

def is_morning_star(p1, p2, p3):
    return (
        p1["Close"] < p1["Open"] and
        p2["Close"] < p2["Open"] and
        p3["Close"] > p3["Open"] and
        p3["Close"] > ((p1["Close"] + p1["Open"]) / 2)
    )

def is_evening_star(p1, p2, p3):
    return (
        p1["Close"] > p1["Open"] and
        p2["Close"] > p2["Open"] and
        p3["Close"] < p3["Open"] and
        p3["Close"] < ((p1["Close"] + p1["Open"]) / 2)
    )

# Button Action
if st.button("🔍 Run Scan"):
    matched = []
    with st.spinner("Scanning NSE..."):
        for symbol in stock_symbols:
            try:
                df = yf.download(symbol, period="10d", interval="1d")
                info = yf.Ticker(symbol).info

                if df is None or df.empty or len(df) < 5:
                    continue

                latest = df.iloc[-2]
                prev = df.iloc[-3]
                prev2 = df.iloc[-4]

                o = latest["Open"]
                h = latest["High"]
                l = latest["Low"]
                c = latest["Close"]
                po = prev["Open"]
                pc = prev["Close"]

                # Filters
                vol_million = latest["Volume"] / 1e6
                mcap_crore = info.get("marketCap", 0) / 1e7
                if vol_million < min_volume or mcap_crore < min_market_cap:
                    continue

                # Pattern checks
                match = (
                    (pattern == "Hammer" and is_hammer(o, h, l, c)) or
                    (pattern == "Inverted Hammer" and is_inverted_hammer(o, h, l, c)) or
                    (pattern == "Doji" and is_doji(o, h, l, c)) or
                    (pattern == "Bullish Engulfing" and is_bullish_engulfing(po, pc, o, c)) or
                    (pattern == "Bearish Engulfing" and is_bearish_engulfing(po, pc, o, c)) or
                    (pattern == "Shooting Star" and is_shooting_star(o, h, l, c)) or
                    (pattern == "Morning Star" and is_morning_star(prev2, prev, latest)) or
                    (pattern == "Evening Star" and is_evening_star(prev2, prev, latest))
                )

                if match:
                    matched.append({
                        "Symbol": symbol,
                        "Volume (M)": round(vol_million, 2),
                        "Market Cap (Cr)": round(mcap_crore, 2)
                    })

            except Exception as e:
                st.warning(f"⚠️ {symbol}: {e}")

    if matched:
        st.success(f"✅ {len(matched)} stocks matched")
        st.dataframe(pd.DataFrame(matched))
    else:
        st.info("🙁 No stocks matched your criteria.")
