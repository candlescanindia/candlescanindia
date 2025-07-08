from requests_html import HTMLSession

def fetch_nse_stock_list():
    session = HTMLSession()
    url = "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%20500"

    try:
        # Visit homepage to establish cookies
        session.get("https://www.nseindia.com", headers={"User-Agent": "Mozilla/5.0"})

        # Now hit API
        response = session.get(url, headers={"User-Agent": "Mozilla/5.0"})
        data = response.json()
        return [item["symbol"] + ".NS" for item in data.get("data", [])]
    except Exception as e:
        print("Error fetching NSE list:", e)
        return []
