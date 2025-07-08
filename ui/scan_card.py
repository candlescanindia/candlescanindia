# ui/scan_card.py

import streamlit as st

def render_scan_results(results):
    if not results:
        st.warning("No matching stocks found.")
        return

    st.markdown("""
        <style>
        .sticky-results {
            position: -webkit-sticky;
            position: sticky;
            top: 90px;
            background: #ffffff;
            z-index: 99;
            padding-top: 0.5rem;
        }
        .results-wrapper {
            max-height: 500px;
            overflow-y: auto;
        }
        @media (max-width: 768px) {
            .sticky-results {
                position: static;
                padding-top: 0;
            }
            .results-wrapper {
                max-height: none;
                overflow-y: visible;
            }
        }
        </style>
        <div class="sticky-results">
            <h4>📋 Scan Results</h4>
            <div class="results-wrapper">
    """, unsafe_allow_html=True)

    # Render the cards inside the sticky container
    for i in range(0, len(results), 2):
        cols = st.columns(2)
        for j in range(2):
            if i + j < len(results):
                with cols[j]:
                    render_stock_card(results[i + j])

    st.markdown("</div></div>", unsafe_allow_html=True)


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
