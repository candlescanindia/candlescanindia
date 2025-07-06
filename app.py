import streamlit as st
import pandas as pd
import yfinance as yf

st.set_page_config(page_title="CandleScanIndia", layout="wide")
st.title("📊 CandleScanIndia")
st.caption("Real-Time NSE Candlestick Pattern Scanner")

# --- Sidebar ---
with st.sidebar:
    st.header("ℹ️ About")
    st.markdown("""
    **CandleScanIndia** scans Indian NSE stocks for popular candlestick patterns.
    
    - Uses real-time Yahoo Finance data  
    - Supports filters for volume and market cap  
    """)
    st.markdown("---")

# --- Pattern List ---
patterns = [
    "Hammer", "Inverted Hammer", "Doji", "Bullish Engulfing", "Bearish Engulfing",
    "Shooting Star", "Morning Star", "Evening Star"
]
pattern = st.selectbox("📌 Select Candlestick Pattern", patterns)
min_volume = st.number_input("📈 Min Volume (in millions)", value=1.0)
min_mcap = st.number_input("🏦 Min Market Cap (in crores)", value=10000.0)

# --- NSE Stock List ---
stock_symbols = [
    "RELIANCE.NS", "INFY.NS", "TCS.NS", "HDFCBANK.NS", "ICICIBANK.NS", "SBIN.NS", "LT.NS",
    "AXISBANK.NS", "HINDUNILVR.NS", "ITC.NS", "WIPRO.NS", "TATAMOTORS.NS", "BAJFINANCE.NS",
    "ASIANPAINT.NS", "ADANIENT.NS", "KOTAKBANK.NS", "BHARTIARTL.NS", "HCLTECH.NS", "TECHM.NS",
    "SUNPHARMA.NS", "ULTRACEMCO.NS", "POWERGRID.NS", "NTPC.NS", "JSWSTEEL.NS", "COALINDIA.NS"
]

# --- Pattern Functions ---
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

# --- Run Scan ---
if st.button("🔍 Run Scan"):
    results = []

    with st.spinner("Scanning stocks..."):
        for symbol in stock_symbols:
            try:
                df = yf.download(symbol, period="10d", interval="1d")
                info = yf.Ticker(symbol).info

                if df is None or df.empty or len(df) < 5:
                    continue

                # Scalars for pattern
                latest = df.iloc[-2]
                prev = df.iloc[-3]
                prev2 = df.iloc[-4]

                o = float(latest["Open"])
                h = float(latest["High"])
                l = float(latest["Low"])
                c = float(latest["Close"])
                po = float(prev["Open"])
                pc = float(prev["Close"])

                # Filters
                volume_m = float(latest["Volume"] / 1e6)
                mcap_cr = float(info.get("marketCap", 0) / 1e7)
                if volume_m < min_volume or mcap_cr < min_mcap:
                    continue

                # Match Pattern
                matched = False
                if pattern == "Hammer":
                    matched = is_hammer(o, h, l, c)
                elif pattern == "Inverted Hammer":
                    matched = is_inverted_hammer(o, h, l, c)
                elif pattern == "Doji":
                    matched = is_doji(o, h, l, c)
                elif pattern == "Bullish Engulfing":
                    matched = is_bullish_engulfing(po, pc, o, c)
                elif pattern == "Bearish Engulfing":
                    matched = is_bearish_engulfing(po, pc, o, c)
                elif pattern == "Shooting Star":
                    matched = is_shooting_star(o, h, l, c)
                elif pattern == "Morning Star":
                    matched = is_morning_star(prev2, prev, latest)
                elif pattern == "Evening Star":
                    matched = is_evening_star(prev2, prev, latest)

                if matched:
                    results.append({
                        "Symbol": symbol.replace(".NS", ""),
                        "Volume (M)": round(volume_m, 2),
                        "Market Cap (Cr)": round(mcap_cr, 2)
                    })

            except Exception as e:
                st.warning(f"⚠️ Error with {symbol}: {e}")

    if results:
        st.success(f"✅ Found {len(results)} stock(s) matching '{pattern}'")
        st.dataframe(pd.DataFrame(results))
    else:
        st.info("🙁 No matching stocks found.")
