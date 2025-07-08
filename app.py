# app.py

import streamlit as st
from ui.layout import render_header, render_top_controls
from ui.scan_card import render_scan_results
from scans.candlestick import run_candlestick_scan

def main():
    st.set_page_config(page_title="CandleScan India", layout="wide")

    render_header()

    try:
        duration, pattern_type, pattern, _, scan_clicked = render_top_controls()
    except Exception as e:
        st.error(f"Error in top controls: {e}")
        return

    matched_results = []
    try:
        if scan_clicked:
            matched_results = run_candlestick_scan(duration, pattern)
    except Exception as e:
        st.error(f"Error during scanning: {e}")
        return

    try:
        render_scan_results(matched_results)
    except Exception as e:
        st.error(f"Error while rendering results: {e}")

if __name__ == "__main__":
    main()
