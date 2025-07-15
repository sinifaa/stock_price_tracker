# main.py

from nse_price_fetcher import get_stock_price
from concurrent.futures import ThreadPoolExecutor, as_completed

stocks = [
    "GRSE", "INDIANB", "UNIONBANK", "VOLTAS", "MOTHERSON",
    "JKTYRE", "DATAPATTNS", "ULTRACEMCO", "ICICIPRULI",
    "CUMMINSIND", "HINDUNILVR", "CONCOR", "BHEL"
]

# Use dictionary to maintain order
results = {}

# Thread pool for concurrent fetching
with ThreadPoolExecutor(max_workers=10) as executor:
    # Submit all tasks
    future_to_symbol = {executor.submit(get_stock_price, symbol): symbol for symbol in stocks}

    # Collect results as they complete
    for future in as_completed(future_to_symbol):
        symbol = future_to_symbol[future]
        try:
            price = future.result()
            results[symbol] = price if price is not None else "NA"
        except Exception as e:
            results[symbol] = "NA"

# Print results in same order as original list
for symbol in stocks:
    print(results[symbol])
