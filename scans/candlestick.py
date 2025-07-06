import yfinance as yf
import pandas as pd

def is_hammer(df):
    body = abs(df['Close'] - df['Open'])
    lower_shadow = df[['Open', 'Close']].min(axis=1) - df['Low']
    upper_shadow = df['High'] - df[['Open', 'Close']].max(axis=1)
    return (lower_shadow > 2 * body) & (upper_shadow < body)

def scan_hammer(stock_symbol):
    try:
        df = yf.download(stock_symbol, period="5d", interval="1d")
        if df.empty:
            return False
        return is_hammer(df).iloc[-1]  # Check latest candle only
    except Exception as e:
        return False
