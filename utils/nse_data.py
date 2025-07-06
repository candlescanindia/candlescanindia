import pandas as pd

def load_stocks():
    return pd.read_csv("data/nse_stock_list.csv")
