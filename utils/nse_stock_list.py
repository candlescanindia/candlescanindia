import requests
import pandas as pd

def fetch_nse_stock_list():
    """
    Fetches a basic list of NSE stocks (symbol and name) from NSE's equity stock list.
    Returns: list of dicts: [{"code": "RELIANCE", "name": "Reliance Industries"}, ...]
    """
    url = "https://www1.nseindia.com/content/equities/EQUITY_L.csv"

    try:
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Referer": "https://www.nseindia.com"
        }

        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        df = pd.read_csv(pd.compat.StringIO(response.text))
        df = df[["SYMBOL", "NAME OF COMPANY"]]

        stock_list = df.rename(columns={"SYMBOL": "code", "NAME OF COMPANY": "name"}).to_dict("records")
        return stock_list

    except Exception as e:
        print("Error fetching NSE stock list:", e)
        return []
