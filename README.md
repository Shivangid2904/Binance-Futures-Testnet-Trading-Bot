# Binance Futures Testnet Trading Bot

## Setup Steps

1. Clone the repository:

```
git clone <your-repo-url>
cd Binance-Futures-Testnet-Trading-Bot
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory:

```
API_KEY=your_api_key
API_SECRET=your_api_secret
```

⚠️ Do not upload `.env` to GitHub.

---

## How to Run

### Market Order

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
```

### Limit Order

```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 70000
```

### Stop-Limit Order (Bonus)

```
python cli.py --symbol BTCUSDT --side SELL --type STOP_LIMIT --quantity 0.002 --price 70000 --stop_price 69000
```

---

## Assumptions

* The bot uses **Binance Futures Testnet (USDT-M / Demo Trading)**.
* API keys are generated from the testnet environment.
* Minimum order notional must be ≥ 100 USDT.
* Testnet may have low liquidity, so some orders (especially MARKET) may not execute immediately.
* STOP-LIMIT orders are conditional and will only trigger when the stop price is reached.

---
