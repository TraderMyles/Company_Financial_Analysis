import yfinance as yf

ticker_symbol = input("Enter ticker symbol (e.g. AAPL, SAP, SIE.DE): ").strip().upper()
ticker = yf.Ticker(ticker_symbol)

income = ticker.income_stmt.iloc[:, :4]
income.to_csv(f"{ticker_symbol}_income_statement_annual.csv")

balance = ticker.balance_sheet.iloc[:, :4]
balance.to_csv(f"{ticker_symbol}_balance_sheet_annual.csv")

print(f"Saved {ticker_symbol}_income_statement_annual.csv")
print(f"Saved {ticker_symbol}_balance_sheet_annual.csv")
