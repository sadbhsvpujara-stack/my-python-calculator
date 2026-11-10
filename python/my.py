
# The "Tip & Bill Splitter" Calculator

# When going out to eat with friends, splitting the bill can get messy. Your task is to write a program that calculates how much each person needs to pay, including a custom tip percentage.

# 📋 Requirements

# 1. Ask the user for the total amount of the restaurant bill.
# 2. Ask the user what percentage tip they want to leave (e.g., 10, 15, or 20 percent).
# 3. Ask the user how many people are splitting the bill.
# 4. Calculate the total bill amount (original bill + tip amount).
# 5. Divide that total by the number of people.
# 6. Output the final amount each person owes, rounded nicely to two decimal places

print("---Welcome to the Tip & Bill Splitter Calculator!---")

total_bill = float(input("What was total bill?"))
tip_percent = float(input("What percentage tip would you like to give? 10, 12, or 15?"))
no_of_people = int(input("How many people to split the bill?"))

tip_amount = total_bill * (tip_percent/100)
total_amount = total_bill + tip_amount
amount_per_person = total_amount / no_of_people

print(f"Your total bill is: ${total_amount:.2f}")
print(f"Each person should pay: ${amount_per_person:.2f}")