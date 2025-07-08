# ui/scan_card.py

import streamlit as st

def render_scan_results(results):
    if not results:
        st.warning("No matching stocks found.")
        return

    st.markdown("### 📋 Scan Results")

    # Use a responsive grid layout: two cards per row on wide screens, one on narrow
    num_cols = 2 if st.columns([1, 1])[0].width > 400 else 1
    for i in range(0, len(results), num_cols):
        cols = st.columns(num_cols)
        for j in range(num_cols):
            if i + j < len(results):
                with cols[j]:
                    render_stock_card(results[i + j])


def render_stock_card(stock):
    st.markdown(
        f"""
        <div style="border: 1px solid #ccc; border-radius: 12px; padding: 1rem; margin-bottom: 1rem; background-color: #f9f9f9;">
            <div style="font-size: 1.2rem; font-weight: 700; color: #1f4e79;">{stock['stock_name']}</div>
            <div style="font-size: 0.9rem; color: #555;">Symbol: {stock['symbol']}</div>
            <hr style="margin: 0.5rem 0;">
            <div><strong>Price:</strong> ₹{stock['ltp']}</div>
            <div><strong>Exchange:</strong> {stock['exchange']}</div>
            <div><strong>Pattern Time:</strong> {stock['pattern_time']}</div>
            <div><strong>Duration:</strong> {stock['duration']}</div>
        </div>
        """,
        unsafe_allow_html=True
    )
