import pandas as pd

def load_stocks():
    try:
        df = pd.read_csv("data/nse_stock_list.csv")
        df.columns = df.columns.str.strip().str.lower()  # normalize column headers
        df.rename(columns={"symbol": "Symbol"}, inplace=True)  # ensure exact match
        return df
    except Exception as e:
        raise Exception(f"Failed to load stock list: {e}")
