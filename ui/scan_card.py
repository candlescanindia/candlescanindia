# ui/scan_card.py

import streamlit as st

def render_scan_card(stock):
    """
    Displays a stock scan result in a card-style layout.

    :param stock: Dictionary with keys:
        - symbol (str)
        - name (str)
        - pattern (str)
        - price (float)
        - exchange (str)
        - time (str)
        - duration (str)
    """
    st.markdown(
        f"""
        <div style="border: 1px solid #e0e0e0; border-radius: 12px; padding: 16px; margin-bottom: 12px; background-color: #f9f9f9;">
            <div style="font-size: 1.1rem; font-weight: 600; color: #1a237e;">{stock['symbol']} <span style="color: #555;">({stock['name']})</span></div>
            <div style="margin-top: 6px;">
                <strong>📊 Pattern:</strong> {stock['pattern']} <br>
                <strong>⏱ Duration:</strong> {stock['duration']} &nbsp;&nbsp; 
                <strong>🕒 Time:</strong> {stock['time']} <br>
                <strong>💰 LTP:</strong> ₹{stock['price']} &nbsp;&nbsp; 
                <strong>🏦 Exchange:</strong> {stock['exchange']}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
