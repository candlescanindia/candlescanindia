import pandas as pd

def load_stocks():
    try:
        df = pd.read_csv("data/nse_stock_list.csv")
        return df
    except Exception as e:
        raise Exception(f"Failed to load stock list: {e}")
