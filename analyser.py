"""Summarise a small CSV of expenses using only standard Python libraries."""

import argparse
import csv
from datetime import date
from decimal import Decimal, InvalidOperation


def summarise(path):
    totals = {}
    count = 0
    with open(path, newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        required = {'date', 'category', 'amount'}
        if not required.issubset(reader.fieldnames or []):
            raise ValueError('CSV must contain date, category and amount columns.')
        for line, row in enumerate(reader, start=2):
            try:
                date.fromisoformat(row['date'])
                category = row['category'].strip().lower()
                amount = Decimal(row['amount'])
                if not category or not amount.is_finite() or amount < 0:
                    raise ValueError
                if amount != amount.quantize(Decimal('0.01')):
                    raise ValueError
            except (ValueError, InvalidOperation, TypeError, AttributeError):
                raise ValueError(f'Invalid expense on CSV line {line}.') from None
            totals[category] = totals.get(category, Decimal('0.00')) + amount
            count += 1
    return count, totals


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('file', help='CSV file to summarise')
    args = parser.parse_args()
    try:
        count, totals = summarise(args.file)
    except (OSError, ValueError) as error:
        parser.exit(1, f'Error: {error}\n')
    print(f'Expenses: {count}')
    for category, amount in sorted(totals.items()):
        print(f'{category}: GBP {amount:.2f}')
    print(f'Total: GBP {sum(totals.values(), Decimal("0.00")):.2f}')


if __name__ == '__main__':
    main()
