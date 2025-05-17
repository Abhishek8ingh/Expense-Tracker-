import json
from datetime import datetime

data_file = "expenses.json"

# Load data if file exists, else initialize empty list
def load_expenses():
    try:
        with open(data_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save expenses to file
def save_expenses(expenses):
    with open(data_file, "w") as file:
        json.dump(expenses, file, indent=4)

# Add a new expense
def add_expense():
    try:
        amount = float(input("Enter amount spent: Rs. "))
        category = input("Enter category (Food, Transport, Entertainment, etc.): ").strip()
        description = input("Enter description: ").strip()
        date = input("Enter date (YYYY-MM-DD) or leave blank for today: ").strip()
        if not date:
            date = datetime.today().strftime("%Y-%m-%d")

        expense = {
            "amount": amount,
            "category": category,
            "description": description,
            "date": date
        }

        expenses = load_expenses()
        expenses.append(expense)
        save_expenses(expenses)
        print("Expense added successfully!")
    except ValueError:
        print("Invalid input. Please enter valid data.")

# View summary by category
def view_category_summary():
    expenses = load_expenses()
    summary = {}
    for expense in expenses:
        summary[expense['category']] = summary.get(expense['category'], 0) + expense['amount']
    
    print("\nCategory-wise Expense Summary:")
    for category, total in summary.items():
        print(f"{category}: Rs. {total:.2f}")

# View summary by month
def view_monthly_summary():
    expenses = load_expenses()
    summary = {}
    for expense in expenses:
        month = expense['date'][:7]  # YYYY-MM
        summary[month] = summary.get(month, 0) + expense['amount']

    print("\nMonthly Expense Summary:")
    for month, total in summary.items():
        print(f"{month}: Rs. {total:.2f}")

# Main menu
def main():
    while True:
        print("\n====== Expense Tracker ======")
        print("1. Add New Expense")
        print("2. View Category-wise Summary")
        print("3. View Monthly Summary")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_category_summary()
        elif choice == "3":
            view_monthly_summary()
        elif choice == "4":
            print("Thank you for using the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
