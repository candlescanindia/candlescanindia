import yfinance as yf
import pandas as pd
from utils.nse_stock_list import fetch_nse_stock_list

# Load NSE tickers once
NSE_TICKERS = fetch_nse_stock_list()

# ----------------- Data Fetching -----------------

def fetch_stock_data(ticker: str, duration: str) -> pd.DataFrame | None:
    interval_map = {"15m": "15m", "30m": "30m", "1d": "1d", "1wk": "1wk"}
    period_map = {"15m": "1d", "30m": "2d", "1d": "60d", "1wk": "1y"}

    try:
        df = yf.download(
            tickers=f"{ticker}.NS",
            interval=interval_map[duration],
            period=period_map[duration],
            progress=False
        )
        return df if not df.empty else None
    except Exception:
        return None


# ----------------- RSI Calculation -----------------

def compute_rsi(series: pd.Series, period: int = 14) -> float:
    delta = series.diff()
    gain = delta.where(delta > 0, 0).rolling(period).mean()
    loss = -delta.where(delta < 0, 0).rolling(period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs)).iloc[-1]


# ----------------- Candlestick Pattern Logic -----------------

def is_bullish_engulfing(df): return (
    df.iloc[-2]['Close'] < df.iloc[-2]['Open'] and
    df.iloc[-1]['Close'] > df.iloc[-1]['Open'] and
    df.iloc[-1]['Open'] < df.iloc[-2]['Close'] and
    df.iloc[-1]['Close'] > df.iloc[-2]['Open']
)

def is_bearish_engulfing(df): return (
    df.iloc[-2]['Close'] > df.iloc[-2]['Open'] and
    df.iloc[-1]['Close'] < df.iloc[-1]['Open'] and
    df.iloc[-1]['Open'] > df.iloc[-2]['Close'] and
    df.iloc[-1]['Close'] < df.iloc[-2]['Open']
)

def is_hammer(df):
    last = df.iloc[-1]
    body = abs(last['Close'] - last['Open'])
    lower = min(last['Close'], last['Open']) - last['Low']
    upper = last['High'] - max(last['Close'], last['Open'])
    return lower > 2 * body and upper < body

def is_inverted_hammer(df):
    last = df.iloc[-1]
    body = abs(last['Close'] - last['Open'])
    upper = last['High'] - max(last['Close'], last['Open'])
    lower = min(last['Close'], last['Open']) - last['Low']
    return upper > 2 * body and lower < body

def is_hanging_man(df): return is_hammer(df)
def is_shooting_star(df): return is_inverted_hammer(df)

def is_doji(df):
    last = df.iloc[-1]
    return abs(last['Close'] - last['Open']) < 0.1 * (last['High'] - last['Low'])

def is_dragonfly_doji(df):
    last = df.iloc[-1]
    return abs(last['Open'] - last['Close']) < 0.05 and last['Low'] == min(last['Open'], last['Close'])

def is_gravestone_doji(df):
    last = df.iloc[-1]
    return abs(last['Open'] - last['Close']) < 0.05 and last['High'] == max(last['Open'], last['Close'])

def is_spinning_top(df):
    last = df.iloc[-1]
    body = abs(last['Close'] - last['Open'])
    shadow = last['High'] - last['Low']
    return body < 0.3 * shadow

def is_morning_star(df):
    if len(df) < 3: return False
    a, b, c = df.iloc[-3], df.iloc[-2], df.iloc[-1]
    return (
        a['Close'] < a['Open'] and
        abs(b['Close'] - b['Open']) < 0.3 * (b['High'] - b['Low']) and
        c['Close'] > c['Open'] and
        c['Close'] > (a['Open'] + a['Close']) / 2
    )

def is_evening_star(df):
    if len(df) < 3: return False
    a, b, c = df.iloc[-3], df.iloc[-2], df.iloc[-1]
    return (
        a['Close'] > a['Open'] and
        abs(b['Close'] - b['Open']) < 0.3 * (b['High'] - b['Low']) and
        c['Close'] < c['Open'] and
        c['Close'] < (a['Open'] + a['Close']) / 2
    )

def is_piercing_line(df):
    prev, last = df.iloc[-2], df.iloc[-1]
    return (
        prev['Close'] < prev['Open'] and
        last['Open'] < prev['Low'] and
        last['Close'] > (prev['Open'] + prev['Close']) / 2
    )

def is_dark_cloud_cover(df):
    prev, last = df.iloc[-2], df.iloc[-1]
    return (
        prev['Close'] > prev['Open'] and
        last['Open'] > prev['High'] and
        last['Close'] < (prev['Open'] + prev['Close']) / 2
    )

def is_bullish_harami(df):
    prev, last = df.iloc[-2], df.iloc[-1]
    return (
        prev['Close'] < prev['Open'] and
        last['Open'] > last['Close'] and
        last['Open'] > prev['Close'] and last['Close'] < prev['Open']
    )

def is_bearish_harami(df):
    prev, last = df.iloc[-2], df.iloc[-1]
    return (
        prev['Close'] > prev['Open'] and
        last['Open'] < last['Close'] and
        last['Open'] < prev['Close'] and last['Close'] > prev['Open']
    )

def is_three_white_soldiers(df):
    a, b, c = df.iloc[-3], df.iloc[-2], df.iloc[-1]
    return all(x['Close'] > x['Open'] for x in [a, b, c]) and \
           b['Open'] > a['Open'] and c['Open'] > b['Open']

def is_three_black_crows(df):
    a, b, c = df.iloc[-3], df.iloc[-2], df.iloc[-1]
    return all(x['Close'] < x['Open'] for x in [a, b, c]) and \
           b['Open'] < a['Open'] and c['Open'] < b['Open']

def is_tweezer_top(df):
    prev, last = df.iloc[-2], df.iloc[-1]
    return abs(prev['High'] - last['High']) < 0.1

def is_tweezer_bottom(df):
    prev, last = df.iloc[-2], df.iloc[-1]
    return abs(prev['Low'] - last['Low']) < 0.1


# ----------------- Pattern Registry -----------------

PATTERN_FUNCTIONS = {
    "Bullish Engulfing": is_bullish_engulfing,
    "Bearish Engulfing": is_bearish_engulfing,
    "Hammer": is_hammer,
    "Inverted Hammer": is_inverted_hammer,
    "Hanging Man": is_hanging_man,
    "Shooting Star": is_shooting_star,
    "Doji": is_doji,
    "Dragonfly Doji": is_dragonfly_doji,
    "Gravestone Doji": is_gravestone_doji,
    "Spinning Top": is_spinning_top,
    "Morning Star": is_morning_star,
    "Evening Star": is_evening_star,
    "Piercing Line": is_piercing_line,
    "Dark Cloud Cover": is_dark_cloud_cover,
    "Bullish Harami": is_bullish_harami,
    "Bearish Harami": is_bearish_harami,
    "Three White Soldiers": is_three_white_soldiers,
    "Three Black Crows": is_three_black_crows,
    "Tweezer Top": is_tweezer_top,
    "Tweezer Bottom": is_tweezer_bottom,
}


# ----------------- Main Entry Point -----------------

def run_candlestick_scan(
    duration: str,
    pattern: str,
    min_volume: int = 0,
    min_price: float | None = None,
    max_price: float | None = None,
    min_rsi: float | None = None,
    max_rsi: float | None = None,
    stock_list: list[str] | None = None,
) -> list[dict]:
    """
    Takes parameters from UI and returns matching stocks.
    """
    results = []
    pattern_func = PATTERN_FUNCTIONS.get(pattern)

    if not pattern_func:
        return results

    tickers_to_check = stock_list if stock_list else NSE_TICKERS

    for ticker in tickers_to_check:
        df = fetch_stock_data(ticker, duration)
        if df is None or len(df) < 3:
            continue

        last = df.iloc[-1]

        if min_volume and last["Volume"] < min_volume:
            continue
        if min_price and last["Close"] < min_price:
            continue
        if max_price and last["Close"] > max_price:
            continue

        if min_rsi or max_rsi:
            rsi = compute_rsi(df["Close"])
            if (min_rsi and rsi < min_rsi) or (max_rsi and rsi > max_rsi):
                continue

        try:
            if pattern_func(df):
                results.append({"name": ticker, "code": f"{ticker}.NS"})
        except Exception:
            continue

    return results
