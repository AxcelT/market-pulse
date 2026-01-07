# Market Snapshot Service

A production-grade Python utility designed to capture and analyze key financial indicators (S&P 500, VIX, 10Y Yield) to provide an instant "Market Volatility" context.

Unlike basic scrapers, this service is engineered for **reliability** and **headless deployment** (e.g., Docker/Raspberry Pi).

## 🚀 Key Features


## 🛠️ Tech Stack

* **Core:** Python 3.10+
* **Data:** `yfinance` (Yahoo Finance API)
* **Data Structures:** Pandas (DataFrames)

## 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/axcelt/market-snapshot.git
cd market-snapshot

```

2. **Set up Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

```
3. **Install Dependencies**
```bash
pip install -r requirements.txt

```

## 🏃 Usage

Run the entry point directly. The service will fetch live data and print a formatted table to the standard output (stdout).

```bash
python main.py

```

**Sample Output:**

```text
--- MARKET SNAPSHOT: 2026-01-05 09:30:01 ---

Metric               | Value          
-----------------------------------
S&P 500              | 4,780.25       
VIX                  | 12.40          
Volatility State     | Low / Complacent
US 10Y Yield         | 4.05%          
USD/PHP              | 55.50          

```

## 🔮 Roadmap

* [ ] **Docker Support:** Containerize the application for "write once, run anywhere" deployment.
* [ ] **API Mode:** Expose data via FastAPI for consumption by dashboards (e.g., Homepage).
* [ ] **Database Integration:** Persist historical VIX states to track trends over time.
