# nse_price_fetcher.py

from nsepython import nse_eq
import nsepython

# Set headers to avoid 403 errors
nsepython.headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-US,en;q=0.9"
}

def get_stock_price(symbol):
    """
    Returns the latest price of a single NSE stock symbol.
    If there's an error, returns None.
    """
    try:
        stock_data = nse_eq(symbol)
        return stock_data['priceInfo']['lastPrice']
    except Exception as e:
        print(f"Error for {symbol}: {e}")
        return None
