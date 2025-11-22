# List of all Expense
expensesList = []

print("Welcome to Expense Tracker")

while True:
    print("===Menu===")
    print("1. Add Expense")
    print("2. View All Expense")
    print("3. View Total Expense")
    print("4. Exit")

    choice = int(input("Please Enter Your Choice: "))

    # Add expense
    if choice == 1:
        date = input("Enter Your Date: ")
        expense_type = input("Enter Expense Type: ")
        details = input("Enter a short detail: ")
        amount = float(input("Enter The Amount: "))

        expense = {
            "date": date,
            "type": expense_type,
            "details": details,
            "amount": amount
        }
        expensesList.append(expense)
        print("\nExpense Added Successfully!")

    # View All Expense
    elif choice == 2:
        if len(expensesList) == 0:
            print("No Expense Added")
        else:
            print("\nHere are your Expenses:")
            count = 1
            for everyExpense in expensesList:
                print(f"{count}: {everyExpense['date']}, {everyExpense['type']}, {everyExpense['details']}, {everyExpense['amount']}")
                count += 1

    # View Total Expense
    elif choice == 3:
        total = 0
        for everyExpense in expensesList:
            total += everyExpense["amount"]

        print("\nTotal Expense is:", total)

    # Exit
    elif choice == 4:
        print("Thanks for visiting our website")
        break

    else:
        print("Invalid choice Try Again")
