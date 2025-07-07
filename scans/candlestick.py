import yfinance as yf

def _get_recent_candle(symbol, period="5d"):
    try:
        df = yf.download(symbol + ".NS", period=period, interval="1d")
        if df.empty or len(df) < 3:
            return None
        return df.iloc[-3:]  # Last 3 candles
    except Exception as e:
        print(f"Error for {symbol}: {e}")
        return None

def scan_hammer(symbol, period="5d"):
    df = _get_recent_candle(symbol, period)
    if df is None:
        return False
    last = df.iloc[-1]
    body = abs(last["Close"] - last["Open"])
    lower_wick = min(last["Open"], last["Close"]) - last["Low"]
    upper_wick = last["High"] - max(last["Open"], last["Close"])
    return lower_wick > 2 * body and upper_wick < body

def scan_inverted_hammer(symbol, period="5d"):
    df = _get_recent_candle(symbol, period)
    if df is None:
        return False
    last = df.iloc[-1]
    body = abs(last["Close"] - last["Open"])
    upper_wick = last["High"] - max(last["Open"], last["Close"])
    lower_wick = min(last["Open"], last["Close"]) - last["Low"]
    return upper_wick > 2 * body and lower_wick < body

def scan_doji(symbol, period="5d"):
    df = _get_recent_candle(symbol, period)
    if df is None:
        return False
    last = df.iloc[-1]
    return abs(last["Open"] - last["Close"]) <= 0.1 * (last["High"] - last["Low"])

def scan_bullish_engulfing(symbol, period="5d"):
    df = _get_recent_candle(symbol, period)
    if df is None:
        return False
    prev, last = df.iloc[-2], df.iloc[-1]
    return (
        prev["Close"] < prev["Open"] and
        last["Close"] > last["Open"] and
        last["Close"] > prev["Open"] and
        last["Open"] < prev["Close"]
    )

def scan_bearish_engulfing(symbol, period="5d"):
    df = _get_recent_candle(symbol, period)
    if df is None:
        return False
    prev, last = df.iloc[-2], df.iloc[-1]
    return (
        prev["Close"] > prev["Open"] and
        last["Close"] < last["Open"] and
        last["Open"] > prev["Close"] and
        last["Close"] < prev["Open"]
    )

def scan_morning_star(symbol, period="5d"):
    df = _get_recent_candle(symbol, period)
    if df is None:
        return False
    a, b, c = df.iloc[-3], df.iloc[-2], df.iloc[-1]
    return (
        a["Close"] < a["Open"] and
        b["Close"] < b["Open"] and
        c["Close"] > c["Open"] and
        c["Close"] > a["Open"]
    )

def scan_evening_star(symbol, period="5d"):
    df = _get_recent_candle(symbol, period)
    if df is None:
        return False
    a, b, c = df.iloc[-3], df.iloc[-2], df.iloc[-1]
    return (
        a["Close"] > a["Open"] and
        b["Close"] > b["Open"] and
        c["Close"] < c["Open"] and
        c["Close"] < a["Open"]
    )

def scan_shooting_star(symbol, period="5d"):
    df = _get_recent_candle(symbol, period)
    if df is None:
        return False
    last = df.iloc[-1]
    body = abs(last["Close"] - last["Open"])
    upper_wick = last["High"] - max(last["Close"]()_
