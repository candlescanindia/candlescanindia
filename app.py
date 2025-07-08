from ui.insight_box import render_insights

def main():
    st.set_page_config(page_title="CandleScan India", layout="wide")
    render_header()
    duration, ptype, pattern, show_filters, scan_clicked = render_top_controls()

    matched_results = []

    if scan_clicked:
        matched_results = scan_stocks(duration, pattern)

    render_scan_results(matched_results)

    # 👇 Always visible insights
    render_insights()


if __name__ == "__main__":
    main()
