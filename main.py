import logging
import yfinance as yf
from datetime import datetime
from typing import Optional, Any
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
    
def fetch_market_snapshot() -> dict[str, Any]:
    """
    Fetches all market data and returns it as a raw dictionary.
    """
    data_store = {}
    
    # 1. Fetch raw prices
    for tName, tSymbol in TICKERS.items():
        data_store[tName] = get_latest_price(tSymbol)

    # 2. Calculate Derived State
    vix_val = data_store.get("VIX")
    if vix_val is not None:
        data_store["Volatility State"] = determine_volatility_state(vix_val)
    else:
        data_store["Volatility State"] = "Unknown"
        
    # 3. Add Timestamp
    data_store["generated_at"] = datetime.now().isoformat()
    
    return data_store

# ---------------------------------------------------------
# MAIN EXECUTION
# ---------------------------------------------------------

def main():
    snapshot = fetch_market_snapshot()
    
    # Extract the timestamp from the data
    current_date = snapshot.get("generated_at", "Unknown Date")

    print(f"\n--- MARKET SNAPSHOT: {current_date} ---\n")
    print(f"{'Metric':<20} | {'Value':<15}")
    print("-" * 35)

    print(f"{'S&P 500':<20} | {safe_fmt(snapshot.get('S&P 500'))}")
    print(f"{'VIX':<20} | {safe_fmt(snapshot.get('VIX'))}")
    print(f"{'Volatility State':<20} | {snapshot.get('Volatility State')}")
    print(f"{'US 10Y Yield':<20} | {safe_fmt(snapshot.get('10Y Yield'), suffix='%')}")
    print(f"{'USD/PHP':<20} | {safe_fmt(snapshot.get('USD/PHP'))}")

if __name__ == "__main__":
    main()