print("----Welcome to Adventure Simulator----")
print("Developed by Sadbhav Pujara")
print("🏔️-Welcome to Himalaya trek-🏔️")
print("Loading......\n")


backpack=[]
for i in range(3):
    user_input=input("Enter the item you want:")
    backpack.append(user_input)
    i=i+1
    print(f'Item added:{backpack}')
    if len(backpack)==3:
        print(f"You have sufficent item for Trekking in Himalayas!")
        print(f"The items in your backpack is {backpack}")

path=["A","B"]
print("There are two paths in your route.Where will you go?\n1.Path A goes through one of brutal landscape and hardest terrain with no animal fear.\n2.Path B has easier terrain but lot of animal moves through that path. ")

user_path=input("Enter your chosen path:")
print(f"Your chsoen path is {user_path}")
if user_path in path:
    print("Continue")
    if user_path=="A":
        print("Be safe. No Animal threat.")
    else:
        user=input("Did you encounter any animal(Yes/NO)?")
        if user=="Yes":
            if "torch" in backpack or "knife" in backpack or "rope" in backpack:
                print(f"You have tools to survive.They are{backpack}")
            else:
                 print(f"You have not carried survival tools.")
        elif user=="No":
                print(f"Have a good trekking experience in Himalayas! Be careful.")


    

