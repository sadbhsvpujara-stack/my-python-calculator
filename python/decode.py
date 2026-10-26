# importing module for random number in decoding
import random

def consent():
  # asking for if user wants to encode code
  consent=input("DO you want to code your string(Yes/No)?")

  # using exception handling if user inputs any statements that is outside
  try:
      if consent.lower() == 'yes':

          # taking string from user
          a=input("Enter a string: ")

          # making variable for all alphabet to take from this for given if condition
          alphabet="abcdefghijklmnopqrstuvwxyz"

          # using if else statement to check length of variable
          if len(a) <=3:
          
          #    intializing the value of both front lettter and back letters to be added in it
            front=""
            back=""

          #    using loop for front and back letters to add in encoded string
            for i in range(3):
              position=random.randint(0,25)
              front=front+alphabet[position]
            for i in range(3):
              position=random.randint(0,25)
              back=back+alphabet[position]

          #    moving the first letter of string at last
            first=a[0]

          #    making rest letter of string to move forward in index
            rest=a[1:]

          #    joining the moved letter and rest letter because strings are immutable.So new strings are made
            move=rest+first

          #    finally joining front,altered string and back 
            final=front+move+back
            print(final)

          # if word is larger than 3 letters we are reversing letter to encode it
          else:
            d=a[::-1]
            print(d)

      elif consent.lower() == 'no':
          print("Thank You")

  except Exception as e:
      print(F"An error occured: {e}")
      raise TypeError
  

   

def consent1():
  # asking for to decode the code or not
  consent1=input("Do you want to decode your encoded code(Yes/No)?")

  # using try and except statement to handle wrong input by user
  try:
    if consent1 == 'yes':
        # taking code from user
        code=input("enter your encoded code ")

# using nested if else
        if len(code) <= 3:
          d=code[::-1]
          print(d)

        else:
          remove_first=code[3:-3]
          e=remove_first
          rem=e[len(e)]
          red=e[0:]
          mo=rem+red
          print(mo)

    elif consent1.lower() == 'no':
        print("Decoding precodure has not started.")

  except:
    raise ValueError


  
if __name__ == "__main__":

  #  command for first one task to run first
   consent()

  #  command for second task to run after second one
   consent1()

print("Have a Good Day!")