n=int(input("Enter a number: "))
rev=0
a=n
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(a==rev):
    print("The number is a palindrome!")
else:
    print("The number is not a palindrome!")

# Now for Armstrong number check:
sum=0
c=n
while(n>0):
    dig=n%10
    sum+=dig**3
    n//=10
if(c==sum):
    print("The number is an Armstrong number!")
else:
    print("The number is not an Armstrong number!")