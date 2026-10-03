# Spending Analyser

A small Python command-line project that reads expenses from a CSV file and shows spending by category. It practises loops, functions, dictionaries, file handling and input validation.

## Run

Requires Python 3.10 or later. No packages need installing. Open a terminal in this folder:

```sh
python analyser.py sample_expenses.csv
```

On Windows, use `py` instead of `python` if needed; on macOS/Linux, try `python3`.

Expected output:

```text
Expenses: 4
food: GBP 9.75
study: GBP 12.00
travel: GBP 3.20
Total: GBP 24.95
```

## Input

The CSV needs `date`, `category` and `amount` columns. Dates use YYYY-MM-DD. Amounts are non-negative GBP expenses with no more than two decimal places. Categories are trimmed and converted to lowercase. Blank categories, invalid dates and invalid amounts stop the program with a line number.

All sample data is fictional. The program reads a local file and does not connect to a bank. It handles expenses only, so refunds and income are outside its scope. It assumes one currency and does not perform currency conversion.

## How it works

1. `csv.DictReader` turns each row into a dictionary.
2. Each row is checked before being added to the totals.
3. A dictionary keeps one running total for each category.
4. `Decimal` handles decimal money amounts without binary floating-point rounding errors.
5. The main function prints the categories alphabetically and the grand total.

## Try changing it

- Add another expense to the sample and predict the new total.
- Add a monthly filter using the date column.
- Add a budget and print how much remains.

## Development

This initial version was generated with ChatGPT as a beginner learning project. Suggested extensions above are not implemented. Before presenting it, run it, understand each function and make your own improvements.
