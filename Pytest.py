import random
import time
import sys

print("Welcome to bingo")
time.sleep(0.5)

user_input = input("Please insert a number from 1 to a 100: ")

try:
    user_input = int(user_input)
    valid_number = True
except ValueError:
    valid_number = False

if valid_number:
    print("is an integer")
else:
    sys.exit("!!not a number!!")

time.sleep(1)

if user_input < 101 and user_input > 0:
    print("is you number " + str(user_input) + " ?")
    print("if it is let's proceed")
    time.sleep(1)

    lotterie_random = random.randint(1, 100)
    print("the winning number was ....")
    print("basically")
    time.sleep(0.3)
    print(lotterie_random)
    if user_input == lotterie_random:
        print("You won the lotterie")
    else:
        print("You lost the lotterie")
else:
    print("Unvalid number")

