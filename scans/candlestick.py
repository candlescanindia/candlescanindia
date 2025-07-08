import yfinance as yf
import pandas as pd
import talib

# Mapping user-friendly names to TA-Lib functions
PATTERN_FUNCTIONS = {
    "Bullish Engulfing": talib.CDLENGULFING,
    "Hammer": talib.CDLHAMMER,
    "Inverted Hammer": talib.CDLINVERTEDHAMMER,
    "Morning Star": talib.CDLMORNINGSTAR,
    "Bearish Engulfing": talib.CDLENGULFING,
    "Evening Star": talib.CDLEVENINGSTAR,
    "Hanging Man": talib.CDLHANGINGMAN,
    "Shooting Star": talib.CDLSHOOTINGSTAR,
    "Doji": talib.CDLDOJI,
    "Spinning Top": talib.CDLSPINNINGTOP,
}

# Sample list of NSE stock tickers for testing — ideally replace with full list
NSE_TICKERS = [
    "RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFCBANK.NS", "ICICIBANK.NS",
    "ITC.NS", "LT.NS", "SBIN.NS", "AXISBANK.NS", "KOTAKBANK.NS"
]

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
        data = yf.download(
            tickers=ticker,
            interval=interval_map[duration],
            period=period_map[duration],
            progress=False
        )
        return data if not data.empty else None
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None

def run_candlestick_scan(duration, pattern):
    results = []

    if pattern not in PATTERN_FUNCTIONS:
        return results

    pattern_func = PATTERN_FUNCTIONS[pattern]

    for ticker in NSE_TICKERS:
        df = fetch_stock_data(ticker, duration)
        if df is None or len(df) < 10:
            continue

        signal = pattern_func(df['Open'], df['High'], df['Low'], df['Close'])

        if signal.iloc[-1] != 0:  # last candle formed the pattern
            results.append({
                "name": ticker.replace(".NS", "").upper(),
                "code": ticker
            })

    return results
