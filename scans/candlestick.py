import pandas as pd
from datetime import datetime
import random

# Mocked sample stock list for scanning
stock_list = [
    {"stock_name": "Infosys", "symbol": "INFY", "exchange": "NSE"},
    {"stock_name": "Reliance Industries", "symbol": "RELIANCE", "exchange": "BSE"},
    {"stock_name": "Tata Consultancy Services", "symbol": "TCS", "exchange": "NSE"},
    {"stock_name": "HDFC Bank", "symbol": "HDFCBANK", "exchange": "NSE"},
    {"stock_name": "ICICI Bank", "symbol": "ICICIBANK", "exchange": "NSE"},
    {"stock_name": "State Bank of India", "symbol": "SBIN", "exchange": "BSE"},
    {"stock_name": "Wipro", "symbol": "WIPRO", "exchange": "NSE"},
]

# Mock pattern detection based on hash for variation
def detect_pattern(symbol: str, duration: str, pattern: str) -> bool:
    # Simulate randomness — in real case this would analyze OHLC data
    return (hash(symbol + duration + pattern) % 3 == 0)

# Main candlestick scan function
def run_candlestick_scan(duration: str, pattern: str) -> list:
    matched = []

    for stock in stock_list:
        if detect_pattern(stock["symbol"], duration, pattern):
            matched.append({
                "stock_name": stock["stock_name"],
                "symbol": stock["symbol"],
                "exchange": stock["exchange"],
                "price": round(random.uniform(100, 3000), 2),  # Simulated price
                "pattern": pattern,
                "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "duration": duration
            })

    return matched

