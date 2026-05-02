
# ==============================TASK 2 STOCK PORTFOLIO TRACKER ================================
import csv
import os
from datetime import datetime

STOCK_PRICES = {
    "AAPL":  182.50,   # Apple
    "TSLA":  248.00,   # Tesla
    "GOOGL": 175.30,   # Alphabet / Google
    "MSFT":  415.80,   # Microsoft
    "AMZN":  185.60,   # Amazon
    "NVDA":  875.00,   # NVIDIA
    "META":  505.40,   # Meta
    "NFLX":  628.00,   # Netflix
}


def print_separator(char: str = "─", width: int = 52):
    print(char * width)


def show_available_stocks():
    print_separator("═")
    print(f"  {'TICKER':<10} {'COMPANY':<20} {'PRICE (USD)':>12}")
    print_separator()
    names = {
        "AAPL": "Apple", "TSLA": "Tesla", "GOOGL": "Google",
        "MSFT": "Microsoft", "AMZN": "Amazon", "NVDA": "NVIDIA",
        "META": "Meta", "NFLX": "Netflix",
    }
    for ticker, price in STOCK_PRICES.items():
        print(f"  {ticker:<10} {names.get(ticker,''):<20} ${price:>10,.2f}")
    print_separator("═")


def get_portfolio() -> dict:
    portfolio = {}
    print("\n  Enter your stocks (type 'done' when finished):")
    print_separator()

    while True:
        ticker = input("  Stock ticker (e.g. AAPL): ").strip().upper()

        if ticker == "DONE":
            if not portfolio:
                print("   Please add at least one stock.\n")
                continue
            break

        if ticker not in STOCK_PRICES:
            print(f"   '{ticker}' not found. Available: "
                  f"{', '.join(STOCK_PRICES.keys())}\n")
            continue

        try:
            qty_str = input(f"  Quantity of {ticker}: ").strip()
            qty = float(qty_str)
            if qty <= 0:
                raise ValueError
        except ValueError:
            print("    Please enter a positive number.\n")
            continue

        if ticker in portfolio:
            portfolio[ticker] += qty
            print(f"  ✅  Updated {ticker}: total {portfolio[ticker]} shares\n")
        else:
            portfolio[ticker] = qty
            print(f"  ✅  Added {ticker} × {qty}\n")

    return portfolio


def calculate_portfolio(portfolio: dict) -> list:
    rows = []
    for ticker, qty in portfolio.items():
        price = STOCK_PRICES[ticker]
        value = qty * price
        rows.append((ticker, qty, price, value))
    return rows


def display_results(rows: list):
    total = sum(r[3] for r in rows)

    print("\n")
    print_separator("═")
    print("          📊  PORTFOLIO SUMMARY  📊")
    print_separator("═")
    print(f"  {'TICKER':<8} {'QTY':>6} {'PRICE':>12} {'VALUE':>14}")
    print_separator()
    for ticker, qty, price, value in rows:
        print(f"  {ticker:<8} {qty:>6.2f} ${price:>10,.2f} ${value:>12,.2f}")
    print_separator()
    print(f"  {'TOTAL INVESTMENT VALUE':>34}  ${total:>12,.2f}")
    print_separator("═")


def save_to_csv(rows: list, total: float):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"portfolio_{timestamp}.csv"
    filepath = os.path.join(os.getcwd(), filename)

    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Ticker", "Quantity", "Price (USD)", "Value (USD)"])
        for ticker, qty, price, value in rows:
            writer.writerow([ticker, qty, f"{price:.2f}", f"{value:.2f}"])
        writer.writerow([])
        writer.writerow(["", "", "TOTAL", f"{total:.2f}"])

    return filepath


def save_to_txt(rows: list, total: float):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"portfolio_{timestamp}.txt"
    filepath = os.path.join(os.getcwd(), filename)

    with open(filepath, "w") as f:
        f.write("=" * 52 + "\n")
        f.write("       STOCK PORTFOLIO REPORT\n")
        f.write(f"       Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 52 + "\n")
        f.write(f"{'Ticker':<8} {'Qty':>6} {'Price':>12} {'Value':>14}\n")
        f.write("-" * 52 + "\n")
        for ticker, qty, price, value in rows:
            f.write(f"{ticker:<8} {qty:>6.2f} ${price:>10,.2f} ${value:>12,.2f}\n")
        f.write("-" * 52 + "\n")
        f.write(f"{'TOTAL':>34}  ${total:>12,.2f}\n")
        f.write("=" * 52 + "\n")

    return filepath


def main():
    print("\n" + "═" * 52)
    print("     📈  STOCK PORTFOLIO TRACKER  📈")
    print("         CodeAlpha Python Internship")
    print("═" * 52)

    # Show available stocks
    print("\n  Available Stocks:\n")
    show_available_stocks()

    # Collect portfolio
    portfolio = get_portfolio()
    rows = calculate_portfolio(portfolio)
    total = sum(r[3] for r in rows)

    # Display results
    display_results(rows)

    # Offer to save
    print("\n  Save results?")
    print("  [1] Save as CSV")
    print("  [2] Save as TXT")
    print("  [3] Both")
    print("  [4] Don't save")
    choice = input("\n  Your choice (1-4): ").strip()

    if choice in ("1", "3"):
        path = save_to_csv(rows, total)
        print(f"\n  ✅  CSV saved → {path}")

    if choice in ("2", "3"):
        path = save_to_txt(rows, total)
        print(f"  ✅  TXT saved → {path}")

    if choice == "4":
        print("  ℹ  Results not saved.")

    print("\n  Thanks for using Stock Portfolio Tracker! 📊\n")


if __name__ == "__main__":
    main()
