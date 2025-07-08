# utils/nse_stock_list.py

import pandas as pd
import os

def fetch_nse_stock_list(csv_path="data/EQUITY_L.csv"):
    """
    Load stock list from the local NSE CSV file.
    Returns: List of dicts with 'symbol' and 'name'.
    """
    try:
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"CSV file not found at {csv_path}")

        df = pd.read_csv(csv_path)
        df = df[["SYMBOL", "NAME OF COMPANY"]].dropna()
        df.columns = ["symbol", "name"]

        return df.to_dict(orient="records")

    except Exception as e:
        print("❌ Failed to load local stock list:", e)
        return []
