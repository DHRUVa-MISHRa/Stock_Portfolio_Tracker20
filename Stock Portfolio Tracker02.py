def main():
    # Hardcoded stock prices
    stock_prices = {
        "AAPL": 180.25,
        "TSLA": 250.50,
        "MSFT": 315.75,
        "GOOGL": 140.80,
        "AMZN": 168.95,
        "META": 350.20,
        "NVDA": 420.60,
        "NFLX": 480.35,
        "INTC": 42.85,
        "AMD": 95.40
    }

    portfolio = {}

    print("Stock Portfolio Tracker")
    print("-----------------------")
    print("Available stock symbols:", ", ".join(stock_prices.keys()))
    print("Enter 'done' when finished adding stocks.\n")

    while True:
        # Get user input
        symbol = input("Enter stock symbol: ").upper()
        
        if symbol == 'DONE':
            break
            
        if symbol not in stock_prices:
            print(f"Warning: {symbol} not in our price list. Using default price of $100.00.")
            price = 100.00
        else:
            price = stock_prices[symbol]

        try:
            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                print("Quantity must be positive.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Add to portfolio
        if symbol in portfolio:
            portfolio[symbol]['quantity'] += quantity
            portfolio[symbol]['value'] += quantity * price
        else:
            portfolio[symbol] = {
                'quantity': quantity,
                'price': price,
                'value': quantity * price
            }

        print(f"Added {quantity} shares of {symbol} at ${price:.2f}\n")

    # Calculate totals
    total_investment = sum(stock['value'] for stock in portfolio.values())
    print("\nPortfolio Summary:")
    print("-----------------")
    for symbol, data in portfolio.items():
        print(f"{symbol}: {data['quantity']} shares @ ${data['price']:.2f} = ${data['value']:.2f}")
    
    print(f"\nTotal Investment: ${total_investment:.2f}")

    # Export option
    export = input("\nExport to CSV file? (y/n): ").lower()
    if export == 'y':
        filename = input("Enter filename (without extension): ") + ".csv"
        with open(filename, 'w') as f:
            f.write("Stock,Quantity,Price Per Share,Total Value\n")
            for symbol, data in portfolio.items():
                f.write(f"{symbol},{data['quantity']},{data['price']:.2f},{data['value']:.2f}\n")
        print(f"Portfolio saved to {filename}")

if __name__ == "__main__":
    main()
