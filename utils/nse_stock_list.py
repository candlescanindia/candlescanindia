import requests
import pandas as pd

def fetch_nse_stock_list():
    url = "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%20500"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://www.nseindia.com/"
    }

    try:
        with requests.Session() as s:
            s.headers.update(headers)
            # Make an initial request to establish cookies
            s.get("https://www.nseindia.com", timeout=5)
            response = s.get(url, timeout=10)

        data = response.json()
        stock_list = data.get("data", [])
        return [{"name": stock["symbol"], "code": stock["symbol"]} for stock in stock_list]

    except Exception as e:
        print(f"❌ Error fetching stock list from NSE: {e}")
        return []
