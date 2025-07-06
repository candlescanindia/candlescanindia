import pandas as pd

def load_stocks():
    try:
        df = pd.read_csv("data/nse_stock_list.csv")
        return df
    except FileNotFoundError:
        raise FileNotFoundError("📂 data/nse_stock_list.csv not found. Please add it.")