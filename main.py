import logging
import yfinance as yf
from datetime import datetime
from typing import Optional
from utils import safe_fmt

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
    try:
        logging.info(f"Fetching data for {ticker_symbol}...")
        ticker = yf.Ticker(ticker_symbol)
        
        # Using period="5d" is safer to ensure that at least one trading day is captured
        history = ticker.history(period="5d")
        
        if history.empty:
            logging.warning(f"No data found for {ticker_symbol}")
            return None
            
        return history['Close'].iloc[-1]
        
    except Exception as e:
        logging.error(f"Error fetching {ticker_symbol}: {e}")
        return None
    
def determine_volatility_state(vix_value: float) -> str:
    """
    Returns a string description of the market state based on VIX value.
    """
    if vix_value < 15:
        return "Low / Complacent"
    elif 15 <= vix_value <= 25:
        return "Normal / Watchful"
    else:
        return "High / Volatile"
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
    # Logic check: if VIX is None, we cannot determine state
    if vix_val is not None:
        vol_state = determine_volatility_state(vix_val)
    else:
        vol_state = "Unknown (Data Missing)"

    # Display Results
    print(f"{'Metric':<20} | {'Value':<15}")
    print("-" * 35)

    print(f"{'S&P 500':<20} | {safe_fmt(data_store.get('S&P 500'))}")
    print(f"{'VIX':<20} | {safe_fmt(data_store.get('VIX'))}")
    print(f"{'Volatility State':<20} | {vol_state}")

# The code passes the percentage sign as a suffix argument
    print(f"{'US 10Y Yield':<20} | {safe_fmt(data_store.get('10Y Yield'), suffix='%')}")
    print(f"{'USD/PHP':<20} | {safe_fmt(data_store.get('USD/PHP'))}")

if __name__ == "__main__":
    main()