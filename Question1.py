# Sample Data
meal_data = [
    ("John", "Pizza", 2500),
    ("Sarah", "Burger", 2000),
    ("Mike", "Pasta", 2200),
    ("Grace", "Chicken and Rice", 3500),
    ("Peter", "Pizza", 2500),
]


def generate_cafeteria_report(records):
    """This function takes meal records and prints a report."""
    student_spending = {}  # stores {"John": 12500, ...}
    meal_revenue = {}      # stores {"Pizza": 5000, ...}
    meal_count = {}        # stores {"Pizza": 2, ...}

    for student, meal, price in records:
        weekly_cost = price * 5

        student_spending[student] = student_spending.get(student, 0) + weekly_cost
        meal_revenue[meal] = meal_revenue.get(meal, 0) + weekly_cost
        meal_count[meal] = meal_count.get(meal, 0) + 1

    most_popular = max(meal_count, key=meal_count.get) if meal_count else None
    big_spenders = [student for student, total in student_spending.items() if total > 15000]

    print("=" * 50)
    print("CAFETERIA WEEKLY REPORT")
    print("=" * 50)
    print("\nSTUDENT WEEKLY SPENDING:")
    for student, total in student_spending.items():
        print(f" {student}: {total} UGX")

    print("\nREVENUE PER MEAL TYPE:")
    for meal, revenue in meal_revenue.items():
        print(f" {meal}: {revenue} UGX")

    if most_popular is not None:
        print(f"\nMOST POPULAR MEAL: {most_popular} (chosen by {meal_count[most_popular]} students)")
    else:
        print("\nMOST POPULAR MEAL: N/A")

    if big_spenders:
        print(f"\nBIG SPENDERS (>15000 UGX): {', '.join(big_spenders)}")
    else:
        print("\nNo big spenders found.")

    return student_spending, meal_revenue, meal_count


print("Testing with sample data:")
generate_cafeteria_report(meal_data)

print("\n" + "=" * 50)
print("Testing with additional data:")
print("=" * 50)
extra_data = [
    ("Diana", "Pizza", 2500),
    ("Francis", "Burger", 2000),
    ("Rehema", "Pizza", 2500),
    ("Adrian", "Salad", 1500),
]
generate_cafeteria_report(extra_data)
