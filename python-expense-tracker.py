# expense_tracker.py
# A simple expense tracker — my first GitHub project!

import json
import os

FILENAME = "expenses.json"

def load_expenses():
    """Load expenses from file, or return empty list if none exist."""
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    """Save the expenses list to a file."""
    with open(FILENAME, "w") as f:
        json.dump(expenses, f, indent=2)

def add_expense(expenses):
    """Prompt user to add a new expense."""
    description = input("What did you spend on? ")
    amount = float(input("How much did you spend? ₹"))
    category = input("Category (food/travel/bills/other): ")
    expense = {
        "description": description,
        "amount": amount,
        "category": category
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f"✓ Added ₹{amount} for {description}")

def view_expenses(expenses):
    """Display all recorded expenses."""
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\n--- Your Expenses ---")
    total = 0
    for i, e in enumerate(expenses, 1):
        print(f"{i}. {e['description']} — ₹{e['amount']} [{e['category']}]")
        total += e['amount']
    print(f"\nTotal spent: ₹{total:.2f}")

def view_by_category(expenses):
    """Show total spending grouped by category."""
    if not expenses:
        print("No expenses recorded yet.")
        return
    summary = {}
    for e in expenses:
        cat = e['category']
        summary[cat] = summary.get(cat, 0) + e['amount']
    print("\n--- Spending by Category ---")
    for cat, total in summary.items():
        print(f"  {cat}: ₹{total:.2f}")

def main():
    expenses = load_expenses()
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. View by category")
        print("4. Exit")
        choice = input("Choose (1-4): ")
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_by_category(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
