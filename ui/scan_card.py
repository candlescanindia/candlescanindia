# ui/scan_card.py

import streamlit as st
from datetime import datetime

def render_scan_result(stock: dict, pattern: str, duration: str):
    """
    Renders a detailed stock scan result card.

    stock: dict with keys 'name', 'code', 'price', 'rsi', 'timestamp'
    pattern: string pattern name (e.g., 'Hammer')
    duration: string chart timeframe (e.g., '15m', '1d')
    """
    name = stock.get("name", "")
    code = stock.get("code", "")
    price = stock.get("price", None)
    rsi = stock.get("rsi", None)
    timestamp = stock.get("timestamp", None)

    dt_str = datetime.strftime(timestamp, "%d %b %Y, %I:%M %p") if timestamp else "N/A"
    price_str = f"₹{price:.2f}" if price else "N/A"
    rsi_str = f"{rsi:.1f}" if rsi else "N/A"

    with st.container():
        st.markdown(
            f"""
            <div style="
                border-radius: 12px;
                padding: 1.25rem 1.5rem;
                margin-bottom: 1.25rem;
                background: #f8f9fa;
                box-shadow: 0 2px 6px rgba(0,0,0,0.08);
            ">
                <div style="font-size: 1.2rem; font-weight: 600; color: #1f4e79;">
                    📌 {name} ({code})
                </div>
                <div style="margin-top: 0.5rem;">
                    <b>Pattern:</b> {pattern} <br/>
                    <b>Timeframe:</b> {duration} <br/>
                    <b>Detected on:</b> {dt_str} <br/>
                    <b>Last Traded Price:</b> {price_str} <br/>
                    <b>RSI:</b> {rsi_str}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
