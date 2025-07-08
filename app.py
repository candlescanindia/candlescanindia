# app.py

import streamlit as st
from ui.layout import (
    render_header,
    render_top_controls
)
from ui.highlights import render_highlights
from ui.results import render_results
from utils.patterns import PATTERN_TYPE_MAP

# Set Streamlit page config
st.set_page_config(
    page_title="CandleScan India",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------- UI Header ----------------------
render_header()

# ---------------------- Scan Controls ----------------------
pattern_type, pattern, scan_clicked = render_top_controls()

# ---------------------- Data Simulation ----------------------
# Replace with your real scanning logic
def get_sample_matches(pattern_selected, duration):
    sample = [
        {
            "Symbol": "RELIANCE",
            "Name": "Reliance Industries",
            "LTP": "2820.55",
            "Exchange": "NSE",
            "Pattern": pattern_selected,
            "Time": "2025-07-08 15:30",
            "Duration": duration
        },
        {
            "Symbol": "INFY",
            "Name": "Infosys Ltd",
            "LTP": "1512.90",
            "Exchange": "BSE",
            "Pattern": pattern_selected,
            "Time": "2025-07-08 15:30",
            "Duration": duration
        }
    ]
    return sample

# ---------------------- Pattern Matching Logic ----------------------
matched_stocks = []

if scan_clicked and pattern:
    matched_stocks = get_sample_matches(pattern, duration="1d")
    render_highlights(matched_stocks, pattern)
    render_results(matched_stocks)

