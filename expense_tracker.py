import json
import os

EXPENSE_FILE = "expenses.json"

def load_expenses():
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, 'r') as file:
            return json.load(file)
    return []

def save_expenses(expenses):
    with open(EXPENSE_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Transport): ")
    amount = float(input("Enter amount: "))
    expense = {"date": date, "category": category, "amount": amount}
    expenses.append(expense)
    print("Expense added successfully!")

def view_expenses(expenses):
    if not expenses:
        print("No expenses to display!")
        return
    print(f"{'Date':<15}{'Category':<15}{'Amount':<10}")
    print("-" * 40)
    for expense in expenses:
        print(f"{expense['date']:<15}{expense['category']:<15}{expense['amount']:<10}")

def view_total(expenses):
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total Expenses: {total:.2f}")

def filter_expenses_by_category(expenses, category):
    filtered = [expense for expense in expenses if expense["category"].lower() == category.lower()]
    return filtered

def main():
    expenses = load_expenses()
    
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Expenses")
        print("4. View Expenses by Category")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            view_total(expenses)
        elif choice == '4':
            category = input("Enter category to filter by: ")
            filtered_expenses = filter_expenses_by_category(expenses, category)
            view_expenses(filtered_expenses)
        elif choice == '5':
            save_expenses(expenses)
            print("Exiting. Data saved.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
