import csv
import os

expenses = []
budget = 0
file_name = "expenses.csv"


# ---------------- LOAD EXPENSES ----------------
def load_expenses():
    global expenses
    if os.path.exists(file_name):
        with open(file_name, mode='r') as file:
            reader = csv.DictReader(file)
            expenses = list(reader)
            for exp in expenses:
                exp['amount'] = float(exp['amount'])
        print("Previous expenses loaded successfully!")
    else:
        print("No previous expense file found.")


# ---------------- ADD EXPENSE ----------------
def add_expense():
    date = input("Enter Date (YYYY-MM-DD): ")
    category = input("Enter Category (Food/Travel/etc): ")
    amount = float(input("Enter Amount: "))
    description = input("Enter Description: ")

    expense = {
        'date': date,
        'category': category,
        'amount': amount,
        'description': description
    }

    expenses.append(expense)
    print("Expense added successfully!")


# ---------------- VIEW EXPENSES ----------------
def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    for exp in expenses:
        if all(exp.values()):
            print(f"Date: {exp['date']}, Category: {exp['category']}, "
                  f"Amount: {exp['amount']}, Description: {exp['description']}")
        else:
            print("Incomplete expense entry found.")


# ---------------- SET BUDGET ----------------
def set_budget():
    global budget
    budget = float(input("Enter Monthly Budget: "))
    print("Budget set successfully!")


# ---------------- TRACK BUDGET ----------------
def track_budget():
    total = sum(exp['amount'] for exp in expenses)
    print(f"Total Expenses: {total}")

    if total > budget:
        print("Warning! You have exceeded your budget!")
    else:
        print(f"You have {budget - total} left for the month.")


# ---------------- SAVE EXPENSES ----------------
def save_expenses():
    with open(file_name, mode='w', newline='') as file:
        fieldnames = ['date', 'category', 'amount', 'description']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for exp in expenses:
            writer.writerow(exp)

    print("Expenses saved successfully!")


# ---------------- MENU ----------------
def menu():
    load_expenses()

    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Set Budget")
        print("4. Track Budget")
        print("5. Save Expenses")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            set_budget()
        elif choice == '4':
            track_budget()
        elif choice == '5':
            save_expenses()
        elif choice == '6':
            save_expenses()
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


menu()