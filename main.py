# Expense Tracker

total_spent = 0
count = 0

print("Expense Tracker")
print("Type 0 to finish.\n")

while True:
    expense = float(input("Enter expense amount: "))

    if expense == 0:
        break

    total_spent += expense
    count += 1

print("\n===== Expense Report =====")
print("Number of Expenses:", count)
print("Total Spent:", total_spent)