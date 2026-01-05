import yfinance as yf
from datetime import datetime

# ---------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------
TICKERS = {
    "S&P 500": "^GSPC",        
    "VIX": "^VIX",            
    "10Y Yield": "^TNX",      
    "USD/PHP": "PHP=X"         
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
    
    ticker = yf.Ticker(ticker_symbol)
    history = ticker.history(period="5d")
    close_price = history.Close[-1]
    return close_price

def determine_volatility_state(vix_value):
    """
    Returns a string description of the market state based on VIX value.
    Example: "High Volatility" if VIX > 20.
    """
    if vix_value < 15:
        return "Low / Complacent"
    elif 15 <= vix_value <= 25:
        return "Normal / Watchful"
    else:
        return "High / Volatile"    
    
    return "Unknown State"

# ---------------------------------------------------------
# MAIN EXECUTION
# ---------------------------------------------------------

def main():
    # Get the current date
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n--- MARKET SNAPSHOT: {current_date} ---\n")

    # Fetch Data
    data_store = {}
    
    for tName, tSymbol in TICKERS.items():
        price = get_latest_price(tSymbol)
        data_store[tName] = price

    # specific logic for Volatility State
    vix_val = data_store.get("VIX", 0)
    vol_state = determine_volatility_state(vix_val)

    # Display Results
    print(f"{'Metric':<20} | {'Value':<15}")
    print("-" * 35)
    print(f"{'S&P 500':<20} | {data_store['S&P 500']:.2f}")
    print(f"{'VIX':<20} | {data_store['VIX']:.2f}")
    print(f"{'Volatility State':<20} | {vol_state}")
    print(f"{'US 10Y Yield':<20} | {data_store['10Y Yield']:.2f}%")
    print(f"{'USD/PHP':<20} | {data_store['USD/PHP']:.2f}")

if __name__ == "__main__":
    main()