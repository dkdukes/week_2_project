import random
import sys
random_num = random.randint(1,100)

def random_guess():
    try:
        user_num = int(input("guess a number between 1-100: "))
        if user_num in range(1,101):
            if user_num == random_num:
                print("Correct")
                sys.exit()
            elif user_num < random_num:
                print("Too Low")
            else:
                print("Too High")
        else:
            print("Error: Number should be between 1-100")
            sys.exit()
    except ValueError:
        print("Error: Use whole numbers only ")
        sys.exit()

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
        print(f"Remaining attempts: {10-count}")
            # break
elif user_level == "medium":
     while (count < 7):
        random_guess()
        count += 1
        print(f"Remaining attempts: {7-count}")
            # break
else:
    while (count < 5):
        random_guess()
        count += 1
        print(f"Remaining attempts: {5-count}")
            # break
            
print(f"\n Game over! The correct number is: {random_num}")
