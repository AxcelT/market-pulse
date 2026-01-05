from flask import Flask, jsonify
from main import fetch_market_snapshot

app = Flask(__name__)

@app.route('/')
def index():
    return {
        "status": "online", 
        "service": "Market Snapshot API", 
        "usage": "GET /snapshot"
    }

@app.route('/snapshot')
def get_snapshot():
    """
    Returns the market snapshot as JSON.
    """
    # 1. Fetch the data using your shared logic
    data = fetch_market_snapshot()
    
    # 2. Return as JSON (Flask does this automatically for dicts, 
    # but jsonify is explicit and good practice)
    return jsonify(data)

if __name__ == '__main__':
    # reliable dev server
    app.run(host='0.0.0.0', port=5000, debug=True)