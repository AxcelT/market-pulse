/**
 * It fetches the snapshot data from the internal API endpoint
 * and updates the DOM elements with the new values.
 */
async function loadMarketData() {
    try {
        const response = await fetch('/snapshot');
        const data = await response.json();

        // It updates the DOM elements with the fetched data
        updateCard('sp500-val', data['S&P 500'], '', 2);
        updateCard('vix-val', data['VIX'], '', 2);
        updateCard('yield-val', data['10Y Yield'], '%', 2);
        updateCard('usd-php-val', data['USD/PHP'], ' ₱', 2);
        
        // It handles the textual volatility state separately for color coding
        const volStateElement = document.getElementById('vol-state');
        const volState = data['Volatility State'];
        volStateElement.textContent = volState;
        
        // It removes old classes and applies new ones based on the state string
        volStateElement.className = 'card-value'; 
        if (volState.includes("Low")) volStateElement.classList.add('state-low');
        else if (volState.includes("High")) volStateElement.classList.add('state-high');
        else volStateElement.classList.add('state-normal');

        // It formats the timestamp for display
        const date = new Date(data['generated_at']);
        document.getElementById('last-updated').textContent = 'Updated: ' + date.toLocaleTimeString();

    } catch (error) {
        console.error('Error fetching market data:', error);
        document.getElementById('last-updated').textContent = 'Error connecting to service';
    }
}

/**
 * It formats numbers with fixed decimal places and optional suffixes.
 * If the value is null or undefined, it displays 'N/A'.
 */
function updateCard(elementId, value, suffix, decimals) {
    const el = document.getElementById(elementId);
    if (value === null || value === undefined) {
        el.textContent = 'N/A';
    } else {
        el.textContent = parseFloat(value).toFixed(decimals) + suffix;
    }
}

// It triggers the data load immediately when the page loads
window.addEventListener('DOMContentLoaded', loadMarketData);