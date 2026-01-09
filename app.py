from flask import Flask, jsonify, render_template
from main import fetch_market_snapshot

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/snapshot')
def get_snapshot():
    """
    Returns the market snapshot as JSON.
    """
    data = fetch_market_snapshot()
    return jsonify(data)

if __name__ == '__main__':
    # reliable dev server
    app.run(host='0.0.0.0', port=5000, debug=True)