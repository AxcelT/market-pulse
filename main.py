import yfinance as yf
from datetime import datetime

# ---------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------
# TODO: Fill in the correct Yahoo Finance Ticker symbols here
TICKERS = {
    "S&P 500": "",        # Hint: Starts with ^
    "VIX": "",            # Hint: Starts with ^
    "10Y Yield": "",      # Hint: Starts with ^
    "USD/PHP": ""         # Hint: Ends with =X
}

# ---------------------------------------------------------
# HELPER FUNCTIONS
# ---------------------------------------------------------

def get_latest_price(ticker_symbol):
    """
    Takes a ticker symbol (e.g., "AAPL"), fetches data,
    and returns the most recent closing price.
    """
    print(f"Fetching data for {ticker_symbol}...")
    
    # TODO: Use yfinance to get the Ticker object
    # ticker = yf.Ticker(...)
    
    # TODO: Get historical data for the last few days (period="5d")
    # history = ticker.history(...)
    
    # TODO: Extract the last available 'Close' price from the history
    # last_price = ...
    
    # Placeholder return (Replace this with actual logic)
    return 0.00

def determine_volatility_state(vix_value):
    """
    Returns a string description of the market state based on VIX value.
    Example: "High Volatility" if VIX > 20.
    """
    # TODO: Write your if/else logic here
    if vix_value < 15:
        return "Low / Complacent"
    # elif ...
    
    return "Unknown State"

# ---------------------------------------------------------
# MAIN EXECUTION
# ---------------------------------------------------------

def main():
    # 1. Get the current date
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n--- MARKET SNAPSHOT: {current_date} ---\n")

    # 2. Fetch Data
    # Note: We are looping through the TICKERS dictionary we made at the top
    data_store = {}
    
    for friendly_name, symbol in TICKERS.items():
        price = get_latest_price(symbol)
        data_store[friendly_name] = price

    # 3. specific logic for Volatility State
    # We pull the VIX value specifically to calculate the state
    vix_val = data_store.get("VIX", 0)
    vol_state = determine_volatility_state(vix_val)

    # 4. Display Results
    print(f"{'Metric':<20} | {'Value':<15}")
    print("-" * 35)
    print(f"{'S&P 500':<20} | {data_store['S&P 500']:.2f}")
    print(f"{'VIX':<20} | {data_store['VIX']:.2f}")
    print(f"{'Volatility State':<20} | {vol_state}")
    print(f"{'US 10Y Yield':<20} | {data_store['10Y Yield']:.2f}%")
    print(f"{'USD/PHP':<20} | {data_store['USD/PHP']:.2f}")

if __name__ == "__main__":
    main()