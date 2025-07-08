import yfinance as yf
import pandas as pd

# Sample NSE stock tickers — replace with full list for production
NSE_TICKERS = [
    "RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFCBANK.NS", "ICICIBANK.NS",
    "ITC.NS", "LT.NS", "SBIN.NS", "AXISBANK.NS", "KOTAKBANK.NS"
]

# --- Fetch data using yfinance ---
def fetch_stock_data(ticker, duration):
    interval_map = {
        "15m": "15m",
        "30m": "30m",
        "1d": "1d",
        "1wk": "1wk"
    }
    period_map = {
        "15m": "1d",
        "30m": "2d",
        "1d": "30d",
        "1wk": "3mo"
    }

    try:
        df = yf.download(
            tickers=ticker,
            interval=interval_map[duration],
            period=period_map[duration],
            progress=False
        )
        return df if not df.empty else None
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None

# --- Pattern detection logic ---
def is_bullish_engulfing(df):
    prev = df.iloc[-2]
    last = df.iloc[-1]
    return (
        prev['Close'] < prev['Open'] and
        last['Close'] > last['Open'] and
        last['Open'] < prev['Close'] and
        last['Close'] > prev['Open']
    )

def is_bearish_engulfing(df):
    prev = df.iloc[-2]
    last = df.iloc[-1]
    return (
        prev['Close'] > prev['Open'] and
        last['Close'] < last['Open'] and
        last['Open'] > prev['Close'] and
        last['Close'] < prev['Open']
    )

def is_hammer(df):
    last = df.iloc[-1]
    body = abs(last['Close'] - last['Open'])
    lower_shadow = min(last['Open'], last['Close']) - last['Low']
    upper_shadow = last['High'] - max(last['Open'], last['Close'])
    return (
        lower_shadow > 2 * body and
        upper_shadow < body
    )

def is_doji(df):
    last = df.iloc[-1]
    body = abs(last['Close'] - last['Open'])
    range_ = last['High'] - last['Low']
    return body < 0.1 * range_

# --- Pattern registry ---
PATTERN_FUNCTIONS = {
    "Bullish Engulfing": is_bullish_engulfing,
    "Bearish Engulfing": is_bearish_engulfing,
    "Hammer": is_hammer,
    "Doji": is_doji,
    # Add more patterns here
}

# --- Main scan function ---
def run_candlestick_scan(duration, pattern_type=None, pattern=None, filters_enabled=False):
    results = []

    if not pattern or pattern not in PATTERN_FUNCTIONS:
        return results

    pattern_func = PATTERN_FUNCTIONS[pattern]

    for ticker in NSE_TICKERS:
        df = fetch_stock_data(ticker, duration)
        if df is None or len(df) < 3:
            continue

        try:
            if pattern_func(df):
                results.append({
                    "name": ticker.replace(".NS", ""),
                    "code": ticker
                })
        except Exception as e:
            print(f"Error checking {pattern} for {ticker}: {e}")
            continue

    return results
