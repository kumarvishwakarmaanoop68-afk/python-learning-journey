"""Day 9 - Expense Tracker"""

import json
from datetime import date

FILE_NAME = "transactions.json"


class ExpenseTracker:
    def __init__(self, file_name=FILE_NAME):
        self.file_name = file_name
        self.transactions = []
        self.load_data()

    def load_data(self):
        try:
            with open(self.file_name, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.transactions = data if isinstance(data, list) else []
        except (FileNotFoundError, json.JSONDecodeError):
            self.transactions = []

    def save_data(self):
        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump(self.transactions, file, indent=4)

    def add_transaction(self, transaction_type):
        while True:
            try:
                amount = float(input("Enter amount: ").strip())
                if amount <= 0:
                    print("Amount must be greater than 0.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")

        category = input("Enter category: ").strip().title()
        note = input("Enter note (optional): ").strip()

        transaction = {
            "type": transaction_type,
            "amount": round(amount, 2),
            "category": category or "Other",
            "note": note,
            "date": date.today().isoformat()
        }

        self.transactions.append(transaction)
        self.save_data()
        print(f"{transaction_type.title()} added successfully.")

    def view_transactions(self):
        if not self.transactions:
            print("No transactions found.")
            return

        print("\n--- Transactions ---")
        for index, item in enumerate(self.transactions, start=1):
            print(
                f"{index}. {item['date']} | "
                f"{item['type'].title():7} | "
                f"₹{item['amount']:.2f} | "
                f"{item['category']} | "
                f"{item['note'] or '-'}"
            )

    def filter_by_category(self):
        if not self.transactions:
            print("No transactions found.")
            return

        category = input("Enter category: ").strip().lower()
        found = False

        print("\n--- Category Results ---")
        for item in self.transactions:
            if item["category"].lower() == category:
                print(
                    f"{item['date']} | {item['type'].title()} | "
                    f"₹{item['amount']:.2f} | {item['note'] or '-'}"
                )
                found = True

        if not found:
            print("No transactions found for this category.")

    def total_by_type(self, transaction_type):
        return sum(
            item["amount"]
            for item in self.transactions
            if item["type"] == transaction_type
        )

    def show_summary(self):
        income = self.total_by_type("income")
        expense = self.total_by_type("expense")
        balance = income - expense

        print("\n--- Summary ---")
        print(f"Total Income : ₹{income:.2f}")
        print(f"Total Expense: ₹{expense:.2f}")
        print(f"Balance      : ₹{balance:.2f}")


def show_menu():
    print("\n===== Expense Tracker =====")
    print("1. Add income")
    print("2. Add expense")
    print("3. View transactions")
    print("4. Filter by category")
    print("5. Show summary")
    print("6. Exit")


def main():
    tracker = ExpenseTracker()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            tracker.add_transaction("income")
        elif choice == "2":
            tracker.add_transaction("expense")
        elif choice == "3":
            tracker.view_transactions()
        elif choice == "4":
            tracker.filter_by_category()
        elif choice == "5":
            tracker.show_summary()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()
