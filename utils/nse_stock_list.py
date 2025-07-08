# utils/nse_stock_list.py

import requests
import pandas as pd

def fetch_nse_stock_list():
    url = "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%20500"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.nseindia.com/",
    }

    try:
        session = requests.Session()
        session.headers.update(headers)
        session.get("https://www.nseindia.com", timeout=5)  # Set cookies

        response = session.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()
        stocks = data["data"]

        stock_list = []
        for stock in stocks:
            symbol = stock.get("symbol")
            company = stock.get("meta", {}).get("companyName", symbol)
            if symbol:
                stock_list.append({"code": symbol, "name": company})

        return stock_list

    except Exception as e:
        print(f"[ERROR] Failed to fetch stock list: {e}")
        return []
