import json
from collections import defaultdict
import os
import matplotlib.pyplot as plt


# -----------------------------
# Load & Save Data
# -----------------------------
def load_data():
    if not os.path.exists("data.json"):
        with open("data.json", "w") as f:
            json.dump({"transactions": []}, f)

    with open("data.json", "r") as f:
        return json.load(f)


def save_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)


# -----------------------------
# Add Transaction
# -----------------------------
def add_transaction():
    data = load_data()

    print("\n--- Add Transaction ---")
    t_type = input("Enter type (income/expense): ").lower()

    while t_type not in ["income", "expense"]:
        t_type = input("Type must be 'income' or 'expense': ").lower()

    amount = float(input("Amount: "))
    category = input("Category: ")
    date = input("Date (YYYY-MM-DD): ")
    description = input("Description: ")

    transaction = {
        "type": t_type,
        "amount": amount,
        "category": category,
        "date": date,
        "description": description
    }

    data["transactions"].append(transaction)
    save_data(data)

    print("Transaction saved successfully!")


# -----------------------------
# Summary
# -----------------------------
def show_summary():
    data = load_data()

    income = 0
    expense = 0

    for t in data["transactions"]:
        if t["type"] == "income":
            income += t["amount"]
        elif t["type"] == "expense":
            expense += t["amount"]

    savings = income - expense

    print("\n----- Summary -----")
    print("Total Income: ₹", income)
    print("Total Expense: ₹", expense)
    print("Savings: ₹", savings)


# -----------------------------
# Category Breakdown (text)
# -----------------------------
def show_category_breakdown():
    data = load_data()
    categories = {}

    for t in data["transactions"]:
        if t["type"] == "expense":
            category = t["category"]
            amount = t["amount"]

            if category not in categories:
                categories[category] = 0

            categories[category] += amount

    print("\n---- Category Breakdown ----")
    if not categories:
        print("No expenses found.")
        return

    for cat, amt in categories.items():
        print(f"{cat}: ₹{amt}")


# -----------------------------
# Category Chart (Pie Chart)
# -----------------------------
def show_category_chart():
    data = load_data()
    categories = {}

    # Collect expenses by category
    for t in data["transactions"]:
        if t["type"] == "expense":
            cat = t["category"]
            amt = t["amount"]

            if cat not in categories:
                categories[cat] = 0

            categories[cat] += amt

    # If no expenses, exit
    if not categories:
        print("\nNo expenses found to show chart.")
        return

    labels = list(categories.keys())
    values = list(categories.values())

    plt.pie(values, labels=labels, autopct="%1.1f%%")
    plt.title("Expense Breakdown by Category")
    plt.show()


# -----------------------------
# Menu
# -----------------------------
def menu():
    while True:
        print("\n----- Personal Finance Tracker -----")
        print("1. Add Transaction")
        print("2. Show Summary")
        print("3. Show Category Breakdown")
        print("4. Show Category Chart")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_transaction()
        elif choice == "2":
            show_summary()
        elif choice == "3":
            show_category_breakdown()
        elif choice == "4":
            show_category_chart()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


# -----------------------------
# Start Program
# -----------------------------
menu()
