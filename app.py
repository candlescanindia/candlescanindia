# app.py
import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

# --- PAGE CONFIG ---
st.set_page_config(page_title="CandleScanIndia – Indian Candlestick Pattern Scanner", layout="wide")
st.markdown("## 📊 CandleScanIndia – Identify Candlestick Patterns in Indian Stocks")
st.markdown("Scan NSE stocks for common candlestick reversal and continuation patterns using live market data.")

# --- PATTERN SELECTION ---
pattern_list = [
    "Doji", "Hammer", "Inverted Hammer", "Bullish Engulfing", "Bearish Engulfing",
    "Morning Star", "Evening Star", "Shooting Star", "Hanging Man", "Spinning Top"
]
selected_pattern = st.radio("Choose a Candlestick Pattern to Scan:", pattern_list)

# --- STOCK LIST (NIFTY 50 Sample Subset) ---
nifty_50_symbols = [
    "RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFCBANK.NS", "ICICIBANK.NS",
    "KOTAKBANK.NS", "HINDUNILVR.NS", "SBIN.NS", "AXISBANK.NS", "LT.NS"
]

# --- FETCH DATA FUNCTION ---
def fetch_data(symbol):
    end = datetime.today()
    start = end - timedelta(days=20)
    df = yf.download(symbol, start=start, end=end)
    df.dropna(inplace=True)
    return df

# --- PATTERN FUNCTIONS ---

def is_doji(row):
    return bool(abs(row['Open'] - row['Close']) < 0.1 * (row['High'] - row['Low']))

def is_hammer(row):
    body = abs(row['Close'] - row['Open'])
    lower = min(row['Open'], row['Close']) - row['Low']
    upper = row['High'] - max(row['Open'], row['Close'])
    return bool(lower > 2 * body and upper < body)

def is_inverted_hammer(row):
    body = abs(row['Close'] - row['Open'])
    lower = min(row['Open'], row['Close']) - row['Low']
    upper = row['High'] - max(row['Open'], row['Close'])
    return bool(upper > 2 * body and lower < body)

def is_bullish_engulfing(prev, curr):
    return bool(prev['Close'] < prev['Open'] and curr['Close'] > curr['Open'] and
                curr['Open'] < prev['Close'] and curr['Close'] > prev['Open'])

def is_bearish_engulfing(prev, curr):
    return bool(prev['Close'] > prev['Open'] and curr['Close'] < curr['Open'] and
                curr['Open'] > prev['Close'] and curr['Close'] < prev['Open'])

def is_morning_star(df):
    try:
        a, b, c = df.iloc[-3], df.iloc[-2], df.iloc[-1]
        return bool(a['Close'] < a['Open'] and abs(b['Close'] - b['Open']) < 0.2 * (b['High'] - b['Low']) and c['Close'] > c['Open'] and c['Close'] > (a['Open'] + a['Close'])/2)
    except:
        return False

def is_evening_star(df):
    try:
        a, b, c = df.iloc[-3], df.iloc[-2], df.iloc[-1]
        return bool(a['Close'] > a['Open'] and abs(b['Close'] - b['Open']) < 0.2 * (b['High'] - b['Low']) and c['Close'] < c['Open'] and c['Close'] < (a['Open'] + a['Close'])/2)
    except:
        return False

def is_shooting_star(row):
    body = abs(row['Close'] - row['Open'])
    upper = row['High'] - max(row['Open'], row['Close'])
    lower = min(row['Open'], row['Close']) - row['Low']
    return bool(upper > 2 * body and lower < body)

def is_hanging_man(row):
    return is_hammer(row)

def is_spinning_top(row):
    body = abs(row['Close'] - row['Open'])
    total_range = row['High'] - row['Low']
    return bool(body < 0.3 * total_range and (row['High'] - row['Close'] > body and row['Open'] - row['Low'] > body))

# --- SCAN ---
if st.button("🔍 Start Scan"):
    matches = []
    for symbol in nifty_50_symbols:
        try:
            df = fetch_data(symbol)
            if len(df) < 3:
                continue
            last = df.iloc[-1]
            prev = df.iloc[-2]

            matched = False
            if selected_pattern == "Doji" and is_doji(last):
                matched = True
            elif selected_pattern == "Hammer" and is_hammer(last):
                matched = True
            elif selected_pattern == "Inverted Hammer" and is_inverted_hammer(last):
                matched = True
            elif selected_pattern == "Bullish Engulfing" and is_bullish_engulfing(prev, last):
                matched = True
            elif selected_pattern == "Bearish Engulfing" and is_bearish_engulfing(prev, last):
                matched = True
            elif selected_pattern == "Morning Star" and is_morning_star(df):
                matched = True
            elif selected_pattern == "Evening Star" and is_evening_star(df):
                matched = True
            elif selected_pattern == "Shooting Star" and is_shooting_star(last):
                matched = True
            elif selected_pattern == "Hanging Man" and is_hanging_man(last):
                matched = True
            elif selected_pattern == "Spinning Top" and is_spinning_top(last):
                matched = True

            if matched:
                matches.append({
                    "Stock": symbol.replace(".NS", ""),
                    "Pattern": selected_pattern,
                    "Date": last.name.date()
                })
        except Exception as e:
            st.warning(f"⚠️ Could not process {symbol}: {e}")

    if matches:
        st.success(f"✅ Found {len(matches)} match(es) for {selected_pattern}")
        st.dataframe(pd.DataFrame(matches))
    else:
        st.info("No matching stocks found today.")
