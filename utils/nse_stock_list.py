# utils/nse_stock_list.py

import pandas as pd
import requests
from io import StringIO

def fetch_nse_stock_list():
    url = "https://www1.nseindia.com/content/equities/EQUITY_L.csv"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://www.nseindia.com/market-data/securities-available-for-trading"
    }

    try:
        # Setup session to fetch NSE cookies
        session = requests.Session()
        session.headers.update(headers)
        session.get("https://www.nseindia.com")  # needed to set cookies

        response = session.get(url, timeout=10)
        response.raise_for_status()  # raise if failed

        df = pd.read_csv(StringIO(response.text))
        df = df[["SYMBOL", "NAME OF COMPANY"]].dropna()
        df.columns = ["symbol", "name"]

        return df.to_dict(orient="records")

    except Exception as e:
        print("❌ Failed to fetch NSE stock list:", e)
        return []
