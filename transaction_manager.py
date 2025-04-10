from transaction import Transaction
from data_entry import get_date, get_amount, get_category, get_description


def add_transaction(handler) -> None:
    date = get_date(
        "Enter the date of the transaction (dd-mm-yyyy) or leave blank for today: ",
        allow_default=True,
    )
    amount = get_amount()
    category = get_category()
    description = get_description()
    txn = Transaction(date, amount, category, description)
    handler.add_transaction(txn)
    print("Transaction added successfully.")


def display_transactions(handler, start_date: str, end_date: str):
    df = handler.get_transactions(start_date, end_date)
    if df.empty:
        print("No transactions found in the given date range.")
    else:
        print(f"\nTransactions from {start_date} to {end_date}:\n")
        print(df.to_string(index=False))

        total_income = df[df["category"] == "Income"]["amount"].sum()
        total_expense = df[df["category"] == "Expense"]["amount"].sum()
        print("\nSummary:")
        print(f"Total Income: ${total_income:.2f}")
        print(f"Total Expense: ${total_expense:.2f}")
        print(f"Net Savings: ${(total_income - total_expense):.2f}")

    return df
