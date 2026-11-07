
import csv
import os


def calculate_profit_loss(buy_price, current_price, quantity):
    investment = buy_price * quantity
    current_value = current_price * quantity
    profit_loss = current_value - investment

    if investment > 0:
        percentage = (profit_loss / investment) * 100
    else:
        percentage = 0

    return investment, current_value, profit_loss, percentage


def main():

    portfolio = []

    print("===== STOCK PORTFOLIO TRACKER =====")

    while True:

        print("\n1. Add Stock")
        print("2. View Portfolio")
        print("3. Save Portfolio to CSV")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":

            try:
                ticker = input("Enter stock ticker: ").strip().upper()

                if not ticker:
                    print("Ticker cannot be empty!")
                    continue

                buy_price = float(input("Enter buy price: "))
                current_price = float(input("Enter current price: "))
                quantity = int(input("Enter number of shares: "))

                if buy_price <= 0 or current_price < 0 or quantity <= 0:
                    print("Please enter valid positive values!")
                    continue

                investment, current_value, profit_loss, percentage = calculate_profit_loss(
                    buy_price, current_price, quantity
                )

                stock = {
                    "Ticker": ticker,
                    "Buy Price": buy_price,
                    "Current Price": current_price,
                    "Quantity": quantity,
                    "Investment": investment,
                    "Current Value": current_value,
                    "Profit/Loss": profit_loss,
                    "Percentage": percentage
                }

                portfolio.append(stock)

                print("\nStock added successfully!")

            except ValueError:
                print("Invalid input! Please enter numbers correctly.")

        elif choice == "2":

            if not portfolio:
                print("Portfolio is empty!")
                continue

            print("\n===== PORTFOLIO SUMMARY =====")

            total_investment = 0
            total_value = 0

            for stock in portfolio:

                print("\nStock:", stock["Ticker"])
                print("Investment:", round(stock["Investment"], 2))
                print("Current Value:", round(stock["Current Value"], 2))
                print("Profit/Loss:", round(stock["Profit/Loss"], 2))
                print("Return:", round(stock["Percentage"], 2), "%")

                total_investment += stock["Investment"]
                total_value += stock["Current Value"]

            total_profit = total_value - total_investment

            print("\nTotal Investment:", round(total_investment, 2))
            print("Total Current Value:", round(total_value, 2))
            print("Overall Profit/Loss:", round(total_profit, 2))

        elif choice == "3":

            if not portfolio:
                print("No stock data available to save!")
                continue

            file_exists = os.path.exists("portfolio_summary.csv")

            with open("portfolio_summary.csv", "w", newline="") as file:

                fieldnames = portfolio[0].keys()

                writer = csv.DictWriter(file, fieldnames=fieldnames)

                writer.writeheader()
                writer.writerows(portfolio)

            print("Portfolio saved successfully to portfolio_summary.csv!")

        elif choice == "4":

            print("Thank you for using Stock Portfolio Tracker!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
    