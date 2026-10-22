def div(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
div(10, 2)
print(div(10, 2)) 

def avg(*numbers):
    if len(numbers) == 0:
        raise ValueError("At least one number is required to calculate the average.")
    return sum(numbers) / len(numbers)
avg(1, 2, 3, 4, 5)
print(avg(1, 2, 3, 4, 5))

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
factorial(5)
print(factorial(5))