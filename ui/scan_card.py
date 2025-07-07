import streamlit as st
from datetime import datetime

def result_display(matched_stocks, selected_pattern):
    st.markdown("## 📋 Scan Results")

    if not matched_stocks:
        st.warning("No stocks matched the selected candlestick pattern.")
        return

    for symbol in matched_stocks:
        with st.container():
            st.markdown(f"""
                <div style="
                    border: 1px solid #e0e0e0;
                    padding: 1rem;
                    border-radius: 10px;
                    background-color: #f9f9f9;
                    margin-bottom: 1rem;
                    box-shadow: 1px 1px 5px rgba(0,0,0,0.05);
                ">
                    <h4 style="margin: 0;">{symbol}</h4>
                    <p style="margin: 0; color: #555;">
                        📌 Pattern: <strong>{selected_pattern}</strong><br/>
                        🕒 Detected: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                    </p>
                </div>
            """, unsafe_allow_html=True)
