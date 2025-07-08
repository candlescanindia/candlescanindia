# ui/scan_card.py

import streamlit as st

def render_scan_results(results: list):
    st.markdown("## 🔍 Scan Results")

    if not results:
        st.info("No scan has been run yet. Click 'Scan Now' to start.")
        return

    cols = st.columns(2)  # 2-column layout

    for idx, stock in enumerate(results):
        with cols[idx % 2]:
            st.markdown(f"""
                <div style='padding: 12px; border: 1px solid #ddd; border-radius: 8px; margin-bottom: 12px; background-color: #fafafa;'>
                    <h4 style='margin: 0 0 5px 0;'>{stock['name']}</h4>
                    <p style='margin: 0; font-size: 0.9rem; color: #666;'>{stock['code']}</p>
                </div>
            """, unsafe_allow_html=True)
