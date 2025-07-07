# data_loader.py
import pandas as pd

def load_stocks(csv_path="data/scans/nse_stock_list.csv"):
    """
    Load the NSE stock list from CSV.
    The CSV must have a 'Symbol' column.
    """
    try:
        df = pd.read_csv(csv_path)
        if "Symbol" not in df.columns:
            raise KeyError("CSV must contain a 'Symbol' column.")
        return df
    except Exception as e:
        raise Exception(f"❌ Failed to load stock list: {e}")
