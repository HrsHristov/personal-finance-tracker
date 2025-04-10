from datetime import datetime


class Transaction:
    def __init__(self, date: str, amount: float, category: str, description: str = ""):
        self.date = datetime.strptime(date, "%d-%m-%Y")
        self.amount = amount
        self.category = category
        self.description = description

    def to_dict(self) -> dict[str, str]:
        return {
            "date": self.date.strftime("%d-%m-%Y"),
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
        }
