# Company Financial Analysis

Fetches the last 4 years of annual financial data for any ticker from Yahoo Finance and saves it as CSV files.

## Setup

1. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install yfinance
   ```

## Usage

Run the script and enter a ticker symbol when prompted:

```bash
python fetch_financials.py
```

```
Enter ticker symbol (e.g. AAPL, SAP, SIE.DE): AAPL
```

## Output

Two CSV files are saved in the current directory:

| File | Contents |
|------|----------|
| `{TICKER}_income_statement_annual.csv` | Revenue, Net Income, EBITDA, etc. |
| `{TICKER}_balance_sheet_annual.csv` | Assets, Liabilities, Equity, etc. |

Columns are fiscal year-end dates (most recent first). Rows are financial line items.

## Ticker Formats

| Exchange | Format | Example |
|----------|--------|---------|
| US (NYSE/NASDAQ) | Ticker as-is | `AAPL`, `MSFT` |
| DAX (Germany) | Append `.DE` | `SAP.DE`, `SIE.DE`, `BMW.DE` |
