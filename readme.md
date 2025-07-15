# 📈 NSE Stock Tracker & Google Sheets Logger

This project fetches **live stock prices from NSE** for a predefined list of symbols and writes the results to a **Google Sheet**, with **weekly tracking** by column (C, D, E...) starting every Thursday.

---

## 🔧 Features

- ✅ Multithreaded stock price fetching (fast!)
- ✅ Uses `nsepython` for live price data (free, no API key)
- ✅ Automatically rotates the Google Sheets column every Thursday
- ✅ Google Sheets integration using `gspread`
- ✅ Configurable stock list and row range
- ✅ Modular: logic split across `main.py`, `utils.py`, and `nse_price_fetcher.py`

---

## 📁 Project Structure

```bash
project/
├── main.py                # Entry point: runs the full workflow
├── nse_price_fetcher.py   # Contains logic to fetch stock price using nsepython
├── utils.py               # Column rotation helpers (e.g., C2 → D2 → ...)
├── credentials.json       # Google Sheets service account credentials (ignored)
├── .gitignore             # Keeps sensitive files out of Git
└── README.md              # You’re reading this
