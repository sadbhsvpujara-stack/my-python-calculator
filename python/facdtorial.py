n=int(input("Enter a number up to which you want to find factorial: "))
factorial=1
a=n
for i in range(1, n+1):
    factorial=factorial*i
print("The factorial of", n, "is", factorial)
