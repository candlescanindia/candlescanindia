# app.py

import streamlit as st
from ui.layout import (
    render_header,
    render_top_controls,
    render_highlights,
    render_results_table
)
from datetime import datetime

# ---------------- Streamlit Config ----------------
st.set_page_config(page_title="CandleScan India", layout="wide", page_icon="📈")

# ---------------- Header ----------------
render_header()

# ---------------- Scan Controls ----------------
duration, pattern, show_filters, scan_clicked = render_top_controls()

# ---------------- Fake Scanning Logic (replace this later) ----------------
matched_stocks = []

if scan_clicked:
    # This is a stub. Replace with your actual scanner logic.
    matched_stocks = [
        {
            "Stock Name": "Reliance Industries",
            "Symbol": "RELIANCE",
            "Last Price": "₹2850.25",
            "Exchange": "NSE",
            "Pattern Time": datetime.now().strftime('%Y-%m-%d %H:%M'),
            "Duration": duration
        },
        {
            "Stock Name": "Infosys Ltd",
            "Symbol": "INFY",
            "Last Price": "₹1570.50",
            "Exchange": "BSE",
            "Pattern Time": datetime.now().strftime('%Y-%m-%d %H:%M'),
            "Duration": duration
        }
    ]

# ---------------- Highlights ----------------
if scan_clicked:
    render_highlights([s["Symbol"] for s in matched_stocks], pattern)

# ---------------- Results Table ----------------
if scan_clicked:
    render_results_table(matched_stocks)
