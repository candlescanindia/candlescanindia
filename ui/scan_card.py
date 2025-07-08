import streamlit as st

def render_scan_results(results, scan_clicked):
    st.markdown("### 📋 Scan Results")

    if not scan_clicked:
        st.info("Please click '🔎 Scan Now' to start scanning.")
        return

    if not results:
        st.warning("No matching stocks found for the selected pattern.")
        return

    # Display results in two-column layout for better space utilization
    num_cols = 2
    rows = [results[i:i + num_cols] for i in range(0, len(results), num_cols)]

    for row in rows:
        cols = st.columns(num_cols)
        for idx, stock in enumerate(row):
            with cols[idx]:
                render_stock_card(stock)

def render_stock_card(stock):
    """
    Renders a single stock card. Expects `stock` to be a dictionary with at least:
    - 'name': Stock name
    - 'code': Stock symbol or NSE/BSE code
    """
    st.markdown(f"""
        <div style="border: 1px solid #ddd; border-radius: 10px; padding: 1rem; margin-bottom: 1rem;">
            <div style="font-size: 1.3rem; font-weight: 600; color: #1a1a1a;">{stock.get('name')}</div>
            <div style="font-size: 0.9rem; color: #666;">{stock.get('code')}</div>
        </div>
    """, unsafe_allow_html=True)
