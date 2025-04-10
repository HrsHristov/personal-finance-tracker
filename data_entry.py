from datetime import datetime

date_format: str = "%d-%m-%Y"
CATEGORIES: dict[str, str] = {"I": "Income", "E": "Expense"}


def get_date(prompt: str, allow_default: bool = False) -> str:
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)

    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format. Please enter the date in dd-mm-yyyy format")
        return get_date(prompt, allow_default)


def get_amount() -> float:
    try:
        amount = float(input("Enter the Amount: "))
        if amount <= 0:
            raise ValueError("Amount must be a non-negative non-zero value")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()


def get_category() -> str:
    category = input("Enter the category ('I' for Income or 'E' for Expense): ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]

    print("Invalid category. Please enter 'I' for Income or 'E' for Expense.")
    return get_category()


def get_description() -> str:
    return input("Enter a description(optional): ")
