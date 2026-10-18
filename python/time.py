import time
a=time.strftime("%H:%M:%S")
print(a)
hour = int(time.strftime("%H"))
print(hour)
a=int(time.strftime("%M"))
print(a)
a=int(time.strftime("%S"))
print(a)
if hour < 12:
    print("Good Morning")
elif hour < 16:
    print("Good Afternoon")
elif hour < 20:
    print("Good Evening")
else:
    print("Good Night") 