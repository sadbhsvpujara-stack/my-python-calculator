number_of_student=int(input("Enter the total number of student going for picnic:"))
cost_of_bus_hire=float(input("Enter the fixed cost of hiring bus for one day:"))
food_cost_of_the_picnic=float(input("Enter the cost of food per student:"))

total_cost=cost_of_bus_hire+(number_of_student*food_cost_of_the_picnic)

# The school collected Rs.500 from each student.
total_collected=number_of_student*500

print("\n---Picnic Budget Summart---")
print(f"Total cost: Rs. {total_cost:.2f}")
print(f"Total collected: Rs.{total_collected:.2f}")
print("---------------")

if total_collected>=total_cost:
    print("Success! The budget is sufficient.")
else:
    print("Alert! You need more money to cover the costs.")