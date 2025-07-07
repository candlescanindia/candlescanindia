# app.py

import streamlit as st
from ui.layout import (
    render_header,
    render_top_controls,
    render_highlights,
    render_results_table
)
import pandas as pd
from datetime import datetime

# -------------- Streamlit App Configuration --------------
st.set_page_config(page_title="CandleScan India", layout="wide")


# -------------- Render Header --------------
render_header()

# -------------- Render Controls --------------
duration, pattern_type, selected_pattern, show_filters, scan_clicked = render_top_controls()

# -------------- Placeholder: Simulated Stock Match Logic --------------
def dummy_scan(pattern, duration):
    # This should be replaced with real scan logic using stock data
    sample_data = [
        {"Symbol": "RELIANCE", "Name": "Reliance Industries", "LTP": 2850.45, "Exchange": "NSE"},
        {"Symbol": "TCS", "Name": "Tata Consultancy", "LTP": 3921.10, "Exchange": "BSE"},
        {"Symbol": "INFY", "Name": "Infosys", "LTP": 1523.30, "Exchange": "NSE"},
    ]
    for stock in sample_data:
        stock["Pattern"] = pattern
        stock["Detected On"] = duration
        stock["Detected At"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return pd.DataFrame(sample_data)

# -------------- Run Scan --------------
if scan_clicked:
    results_df = dummy_scan(selected_pattern, duration)
    matched_symbols = results_df["Symbol"].tolist()

    # Show Highlights
    render_highlights(matched_symbols, selected_pattern, duration)

    # Show Result Table
    render_results_table(results_df)
