data={
    "Aaditya":(1,[60,60,65]),
    "Beast":(2,[40,50,70]),
    "Cat":(3,[50,60,65]),
    "Dog":(4,[60,65,30]),
    "Sunil":(5,[50,60,70]),
    "Zen":(6,[40,45,50])
}

def calculate_average (student_tuple):
    '''This function takes whole tuple as one block in processing and calculates it.'''
    roll_no,scores=student_tuple
    return sum(scores) / len(scores)

def countdown_to_expiry(n):
    if n<=0:
        print("Goodbye!")
        return
    print(f"Closing program in {n}.....")
    countdown_to_expiry(n-1)

user_input=input("what is your name?")

try:
    record=data[user_input]

    average=calculate_average(record)

    for index, name in enumerate (data,start=1):
        if name==user_input:
           print(f"Name:{name} | Roll No:{record[0]} | Average: {average:.2f}")
           break

    match average:
        case average if average>=90:
            print(f"Status:Honors")
        case average if 40<=average<90:
            print(f"Status:Passing")
        case _:
            raise ValueError("Student has failed!")
        
except KeyError:
   print("KeyError: Your input is not listed and not in our record.")

except ValueError as e: 
    print(f"ValueError: {e}")

print("\nHave a Good Day!")
countdown_to_expiry(3)