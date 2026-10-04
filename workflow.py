import csv


def load_expenses():
    expenses = []

    with open("data/expenses.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["amount"] = float(row["amount"])
            expenses.append(row)

    return expenses


def calculate_food_total(expenses):
    total = 0

    for expense in expenses:
        if expense["category"] == "Food":
            total += expense["amount"]

    return total


def calculate_category_totals(expenses):
    totals = {}

    for expense in expenses:
        category = expense["category"]

        if category not in totals:
            totals[category] = 0

        totals[category] += expense["amount"]

    return totals


def find_highest_category(totals):
    highest_category = max(
        totals,
        key=totals.get
    )

    return highest_category


# Main program
expenses = load_expenses()

food_total = calculate_food_total(expenses)

category_totals = calculate_category_totals(expenses)

highest_category = find_highest_category(category_totals)


print("================================")
print("RULE-BASED EXPENSE WORKFLOW")
print("================================")

print(f"Total Food Spending: ₹{food_total:.2f}")

print(
    f"Highest Spending Category: "
    f"{highest_category}"
)

print(
    f"Highest Category Amount: "
    f"₹{category_totals[highest_category]:.2f}"
)