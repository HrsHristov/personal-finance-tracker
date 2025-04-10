import pandas as pd
import csv
from datetime import datetime


class CSVHandler:
    def __init__(self, filename: str, date_format: str = "%d-%m-%Y"):
        self.filename = filename
        self.date_format = date_format
        self.columns = ["date", "amount", "category", "description"]

    def initialize(self) -> None:
        try:
            pd.read_csv(self.filename)
        except FileNotFoundError:
            df = pd.DataFrame(columns=self.columns)
            df.to_csv(self.filename, index=False)

    def add_transaction(self, transaction) -> None:
        with open(self.filename, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.columns)
            writer.writerow(transaction.to_dict())

    def get_transactions(self, start_date: str, end_date: str) -> pd.DataFrame:
        df = pd.read_csv(self.filename)
        df["date"] = pd.to_datetime(df["date"], format=self.date_format)
        start = datetime.strptime(start_date, self.date_format)
        end = datetime.strptime(end_date, self.date_format)

        mask = (df["date"] >= start) & (df["date"] <= end)
        return df.loc[mask]
