# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 185
}

portfolio = {}
total_investment = 0

print("================================")
print("    STOCK PORTFOLIO TRACKER")
print("================================")

print("\nAvailable stocks:")
for stock, price in stock_prices.items():
    print(stock, "-> $", price)

print("\nEnter your stock details.")
print("Type 'done' when you finish.\n")

while True:

    stock_name = input("Enter stock name: ").upper().strip()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not available. Please choose from the list.\n")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.\n")
            continue

    except ValueError:
        print("Please enter a valid quantity.\n")
        continue

    # Store portfolio details
    if stock_name in portfolio:
        portfolio[stock_name] += quantity
    else:
        portfolio[stock_name] = quantity

    print("Stock added successfully!\n")

# Calculate total investment
print("\n================================")
print("       YOUR PORTFOLIO")
print("================================")

for stock, quantity in portfolio.items():

    price = stock_prices[stock]
    investment = price * quantity

    total_investment += investment

    print(
        stock,
        "| Quantity:", quantity,
        "| Price: $", price,
        "| Value: $", investment
    )

print("--------------------------------")
print("Total Investment Value: $", total_investment)
print("================================")

# Optional: Save result to a text file
save = input("\nDo you want to save the result? (yes/no): ").lower()

if save == "yes":

    with open("portfolio.txt", "w") as file:

        file.write("STOCK PORTFOLIO REPORT\n")
        file.write("======================\n\n")

        for stock, quantity in portfolio.items():

            price = stock_prices[stock]
            investment = price * quantity

            file.write(
                f"{stock} | Quantity: {quantity} | "
                f"Price: ${price} | Value: ${investment}\n"
            )

        file.write("\n")
        file.write(
            f"Total Investment Value: ${total_investment}\n"
        )

    print("Portfolio saved successfully as portfolio.txt")