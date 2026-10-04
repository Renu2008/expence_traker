import csv


def load_expenses():
    expenses = []

    with open("data/expenses.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["amount"] = float(row["amount"])
            expenses.append(row)

    return expenses


def calculate_category_total(category):
    expenses = load_expenses()

    total = 0

    for expense in expenses:

        if expense["category"].lower() == category.lower():
            total += expense["amount"]

    return total


def get_highest_spending_category():
    expenses = load_expenses()

    category_totals = {}

    for expense in expenses:

        category = expense["category"]

        if category not in category_totals:
            category_totals[category] = 0

        category_totals[category] += expense["amount"]

    highest_category = max(
        category_totals,
        key=category_totals.get
    )

    return {
        "category": highest_category,
        "amount": category_totals[highest_category]
    }


def get_monthly_summary():
    expenses = load_expenses()

    category_totals = {}

    for expense in expenses:

        category = expense["category"]

        if category not in category_totals:
            category_totals[category] = 0

        category_totals[category] += expense["amount"]

    return category_totals