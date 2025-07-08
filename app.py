# app.py

import streamlit as st
from ui.layout import render_header, render_top_controls
from ui.scan_card import render_scan_results
from ui.insight_box import render_insights  # ⬅️ NEW

# Simulated scan logic
def perform_scan(duration, pattern):
    if pattern == "Doji":
        return [
            {
                "name": "Infosys Ltd",
                "symbol": "INFY",
                "price": 1520.30,
                "exchange": "NSE",
                "timestamp": "2025-07-08 13:00",
                "duration": "15m",
                "pattern": "Doji"
            },
            {
                "name": "Wipro",
                "symbol": "WIPRO",
                "price": 440.00,
                "exchange": "NSE",
                "timestamp": "2025-07-08 13:00",
                "duration": "15m",
                "pattern": "Doji"
            }
        ]
    elif pattern == "Hammer":
        return [
            {
                "name": "Tata Motors",
                "symbol": "TATAMOTORS",
                "price": 980.50,
                "exchange": "BSE",
                "timestamp": "2025-07-08 15:30",
                "duration": "1d",
                "pattern": "Hammer"
            },
            {
                "name": "HDFC Bank",
                "symbol": "HDFCBANK",
                "price": 1740.70,
                "exchange": "NSE",
                "timestamp": "2025-07-08 15:30",
                "duration": "1d",
                "pattern": "Hammer"
            },
            {
                "name": "ICICI Bank",
                "symbol": "ICICIBANK",
                "price": 980.30,
                "exchange": "NSE",
                "timestamp": "2025-07-08 15:30",
                "duration": "1d",
                "pattern": "Hammer"
            }
        ]
    return []

def main():
    st.set_page_config(page_title="CandleScan India", layout="wide")

    render_header()

    duration, pattern_type, pattern, show_filters, scan_clicked = render_top_controls()

    if scan_clicked:
        if pattern:
            matched_results = perform_scan(duration, pattern)
            if matched_results:
                render_scan_results(matched_results)
                render_insights(matched_results)  # ⬅️ Insert below results
            else:
                st.warning("⚠️ No matching stock found for the selected pattern.")
        else:
            st.info("ℹ️ Please select a candlestick pattern to start scanning.")
    else:
        st.info("🔍 Use the filters above and click **Scan Now** to find matching stocks.")

if __name__ == "__main__":
    main()
