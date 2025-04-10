from csv_handler import CSVHandler
from transaction_manager import add_transaction, display_transactions
from plotting import plot_transactions
from data_entry import get_date


CSV_FILE: str = "finance_data.csv"
DATE_FORMAT: str = "%d-%m-%Y"


def main():
    handler = CSVHandler(CSV_FILE, DATE_FORMAT)
    handler.initialize()

    while True:
        print("\n1. Add transaction\n2. View transactions\n3. Exit")
        choice = input("Enter choice (1-3): ")
        if choice == "1":
            add_transaction(handler)
        elif choice == "2":
            start_date = get_date("Enter the start date (dd-mm-yyyy): ")
            end_date = get_date("Enter the end date (dd-mm-yyyy): ")
            df = display_transactions(handler, start_date, end_date)
            if (
                not df.empty
                and input("Do you want to see a plot? (y/n): ").lower() == "y"
            ):
                plot_transactions(df, DATE_FORMAT)
        elif choice == "3":
            break
        else:
            print("Invalid selection.")


if __name__ == "__main__":
    main()
