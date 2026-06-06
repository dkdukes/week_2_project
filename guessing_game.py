import random
import sys
random_num = random.randint(1,100)

def random_guess():
    try:
        user_num = int(input("guess a number between 1-100: "))
        if user_num == random_num:
            print("Correct")
            sys.exit()
        elif user_num <random_num:
            print("Too Low")
        else:
            print("Too High")
    except ValueError:
        print("Error: Use numbers only ")

count=0


levels = ["easy","medium","hard"]

user_level = input("Choose a level:\n Easy: 10 attempts \n Medium: 7 attempts \n Hard: 5 attempts\n").lower().strip()

if user_level not in levels:
    print("Error: Please use the given choices!")
    sys.exit()

if user_level == "easy":
    while (count < 10):
        random_guess()
        count += 1
            # break
elif user_level == "medium":
     while (count < 7):
        random_guess()
        count += 1
            # break
else:
    while (count < 5):
        random_guess()
        count += 1
            # break
            

