# improting modue for random question given
import random

# using list of dictionary to store questions, options, answer and money
questions = [
    {
        "question": "What is the capital of Nepal?",
        "options": ["A. London", "B. Paris", "C. Kathmandu", "D. Madrid"],
        "answer": "C",
        "money": 1000
    },
    {
        "question": "What is name of Prime Minister of Nepal?",
        "options": ["A. Balendra Shah", "B. K P Ojha", "C. Surya Bahadur Thapa", "D. Khadga Prasad Sharma"],
        "answer": "A",
        "money": 2000
    },
    {
        "question": "What is the currency of Nepal?",
        "options": ["A. Dollar", "B. Euro", "C. Nepalese Rupee", "D. Pound"],
        "answer": "C",
        "money": 3000
    },
    {
        "question": "What is birthplace of Nepali language?",
        "options": ["A. Kathmandu", "B. Pokhara", "C. Sinja Valley", "D. Janakpur"],
        "answer": "C",
        "money": 4000
    },
    {
        "question": "What is deepest part of OCean?",
        "options": ["A. Mariana Trench", "B. Java Trench", "C. Puerto Rico Trench", "D. Tonga Trench"],
        "answer": "A",
        "money": 5000
    },
    {
        "question": "What is the largest desert in the world?",
        "options": ["A. Sahara Desert", "B. Arabian Desert", "C. Gobi Desert", "D. Kalahari Desert"],
        "answer": "A",
        "money": 10000
    }

]

# making questions random so that each time user can get different question?
random.shuffle(questions)

# initializing total_winnings and lifelines_left
total_winnings = 0
lifelines_left = 1

print("Welcome TO Ko Banxa crorepati(KBC) Game Show")

print("You have 1 lifelines to use in the game")
print("1. 50-50\n")

print("Let's start the game!\n")

# using loop to print questions and its indexing
for i in range(len(questions)):
    so=questions[i]
    print("Question", i + 1, "for Rs.", so["money"])
    print(so["question"])

# giving variaable to show options and print it
    show=so["options"]

# using if-else statement to check if lifelines_left is greater than 0, then ask user if they want to use a lifeline. If yes, remove two incorrect options and show the remaining options. Then take user input for answer and check if it is correct or not. If correct, add the money to total_winnings, else print game over message and break the loop.
    if lifelines_left > 0:
       chance=input("Do you want to use a lifeline? (yes/no): ")
       if chance == "yes":
          print("You have chosen to use the 50-50 lifeline.")
          lifelines_left-=1

          correct=so["answer"]

          incorrect=[opt for opt in so["options"] if opt.startswith(correct)==False]

          remove=random.sample(incorrect, 2)

          show=[]
          for opt in so["options"]:
              if opt not in remove:
                  show.append(opt)

    for option in show:
       print(option)

    user_answer = input("Enter your answer (A,B,C,D): ").strip().upper()

    if user_answer==so["answer"]:
       total_winnings+=so["money"]
       print("correct Answer! You have won Rs.", {total_winnings})
    else:
        print("wrong Answer! You have won Rs.", {total_winnings})
        print("Game Over!")
        break
    
# printing("Total Winnings: Rs.", {total_winnings})
print("\n"+"="*40)