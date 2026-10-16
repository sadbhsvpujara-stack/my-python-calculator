print("===Simple Calculator===")
a=float(input("enter any number"))
operator=input("enter any operator")
b=float(input("enter any number"))
if operator=="+":
    print(a+b)
elif operator=="-":
    print(a-b)
elif operator=="*":
    print(a*b)
elif operator=="/":
    print(a/b)