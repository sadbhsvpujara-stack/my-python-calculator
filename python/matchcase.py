s=int(input("enter value:"))
match s:
    case 0:
        print("zero")
    case 1:
        print("one")
    case _ if s > 1:
        print("greater than one")
    case _ if s < 0:
        print("negative number")
