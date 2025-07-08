# utils/nse_stock_list.py

from nsetools import Nse
import pandas as pd

def fetch_nse_stock_list():
    """
    Fetches all NSE stock codes using nsetools.

    Returns:
        List[dict]: Each dict contains 'name' and 'code' of a stock.
    """
    nse = Nse()
    try:
        all_stock_codes = nse.get_stock_codes()
        # Remove the first item, which is a header ("SYMBOL": "Company Name")
        stock_list = [
            {"code": symbol, "name": name}
            for symbol, name in all_stock_codes.items()
            if symbol != "SYMBOL"
        ]
        return stock_list
    except Exception as e:
        print(f"[ERROR] Failed to fetch stock list: {e}")
        return []
