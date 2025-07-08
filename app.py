import streamlit as st
from layout.top_controls import render_top_controls
from scans.candlestick import run_candlestick_scan
from ui.scan_card import display_scan_results
from ui.insight_box import show_insight_box

def main():
    st.set_page_config(page_title="CandleScan India", layout="wide")
    
    st.markdown(
        "<h1 style='text-align: center;'>🕯️ CandleScan India</h1>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='text-align: center; color: gray;'>Scan Indian stocks based on candlestick patterns</p>",
        unsafe_allow_html=True
    )
    
    # Top control panel (modular)
    duration, pattern_type, pattern_selected, show_filters, scan_clicked = render_top_controls()
    
    # Show general insights
    show_insight_box()
    
    # Run scan if button clicked
    if scan_clicked and pattern_selected:
        with st.spinner("🔍 Scanning stocks..."):
            matching_stocks = run_candlestick_scan(
                duration=duration,
                pattern_type=pattern_type,
                pattern=pattern_selected,
                filters_enabled=show_filters
            )
        display_scan_results(matching_stocks, pattern_selected)
    elif scan_clicked:
        st.warning("Please select a pattern before scanning.")

if __name__ == "__main__":
    main()
