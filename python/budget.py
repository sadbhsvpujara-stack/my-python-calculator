print("---Welcome to the Target Budget Expense Tracker!---")

budget = 100.0
expenses = []
total_expenses = 0.0
while total_expenses <= budget:
    user_input = input("Enter an expense amount (or type 'exit' to stop): ")
    if user_input.lower() == "exit":
        break
    try:
        expense_amount = float(user_input)
        expenses.append(expense_amount)
        total_expenses += expense_amount
        left_budget = budget - total_expenses
        print(f"You have only Rs. {left_budget}")
        if total_expenses > budget:
            print("Warning: You have exceeded your budget!")
            break

    except ValueError:
        print("Please enter a valid number.")


l_budget = budget - total_expenses
print(f"You spent Rs. {total_expenses} total.")
print(f"You have only Rs. {l_budget}")
print(f"Your expenses are {expenses}")
