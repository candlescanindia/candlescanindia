# ui/scan_card.py

import streamlit as st

def render_scan_results(matched_data: list):
    """
    Display scanned stock results in a card-style layout.

    matched_data: List of dicts, each with keys:
        - stock_name
        - symbol
        - ltp (last traded price)
        - exchange
        - pattern_time
        - duration
    """
    st.markdown("### 📋 Scan Results")

    if not matched_data:
        st.warning("No matching stocks found for the selected pattern.")
        return

    for stock in matched_data:
        with st.container():
            st.markdown(
                f"""
                <div style="border: 1px solid #ddd; border-radius: 10px; padding: 15px; margin-bottom: 10px; background-color: #f9f9f9;">
                    <h4 style="margin: 0; color: #1f4e79;">{stock['stock_name']} ({stock['symbol']})</h4>
                    <p style="margin: 5px 0;">💹 <b>LTP:</b> ₹{stock['ltp']} — <b>Exchange:</b> {stock['exchange']}</p>
                    <p style="margin: 5px 0;">🕒 <b>Pattern Time:</b> {stock['pattern_time']} | <b>Duration:</b> {stock['duration']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
