# Finance Tracker CLI

Finance Tracker CLI is a simple command-line application that allows you to track your income and expenses. The application reads and writes transaction data to a CSV file, provides summaries over specified date ranges, and offers visualization of your data with plots.

## Table of Contents

-   [Features](#features)
-   [Project Structure](#project-structure)
-   [Prerequisites](#Prerequisites)
-   [Installation](#installation)
-   [Usage](#usage)
-   [Testing](#testing)
-   [Contributing](#contributing)
-   [License](#license)

## Features

-   **Add Transactions:**  
    Record income and expenses with details such as date, amount, category, and description.

-   **View Transactions:**  
    Filter transactions by date range and view summaries that include total income, expense, and net savings.

-   **Data Visualization:**  
    Generate plots displaying income and expense trends over time using Matplotlib.

-   **CSV Persistence:**  
    Transactions are stored in a CSV file, making the data easy to back up or integrate with other tools.

## Project Structure

The project is organized into a single folder:

```plaintext
/
├── main.py
├── transaction.py
├── csv_handler.py
├── transaction_manager.py
├── plotting.py
└── data_entry.py
```

### Explanation:

-   **`transaction.py`** defines the `Transaction` class that encapsulates the details for each transaction.
-   **`csv_handler.py`** contains the `CSVHandler` class used for reading and writing the CSV file.
-   **`transaction_manager.py`** manages the core business logic, such as adding new transactions and displaying transactions.
-   **`plotting.py`** includes functions to generate visual plots of the transaction data.
-   **`data_entry.py`** provides helper functions to safely capture and validate user input.

## Prerequisites

-   **Python 3.8+**
-   **pandas**
-   **matplotlib**

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/HrsHristov/personal-finance-tracker
    cd personal-finance-tracker
    ```

2. **(Optional) Create a Virtual Environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Install Dependencies
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the expense tracker, execute the main module:

    python main.py

You will see a menu similar to the following:

```sql
-- Expense Tracker Menu:
-- 1. Add a new transaction
-- 2. View transactions and summary within a date range
-- 3. Exit
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
