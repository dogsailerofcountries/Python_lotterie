import random
import time
import sys

def yes_no():
    returned = False
    while returned == False:
        user_boolean = input("You can answer yes or no:  ")
        if user_boolean == "Yes" or user_boolean == "yes" or user_boolean == "y":
            return True
        elif user_boolean == "No" or user_boolean == "no" or user_boolean == "n":
            return False
        else:
            print("'" + user_boolean + "' isn't answering the question, please: Yes or No")


print("Welcome to bingo")
time.sleep(0.5)

## stage 1 ##

## integer check ## overcomplicating code ...
def integer_check():
    finished = False
    while not finished:
        global user_input
        user_input = input("Please insert a number from 1 to a 100: ")
        try:
            user_input = int(user_input)
            valid_number = True
        except ValueError:
            valid_number = False

        if valid_number:
            print("is an integer")
            finished = True
        else:
            print("'" + user_input + "' is not a number!! try again")
    time.sleep(1)
integer_check()

## Number filter
finished = False
while not finished:
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
        finished = True
    else:
        print("'" + str(user_input) + "' isn't a number from 1 to 100, please try again.")
        integer_check()
time.sleep(1)

## stage 2 ##
print(" ## Bingo - stage 2 ##")
time.sleep(1)
print("Do you want to double or nothing?")
user_input = yes_no()

if user_input:
    print("let's proceed")
elif not user_input:
    sys.exit("See you next time!")    

print("You will insert a number, that number will be your probability of winning.")
time.sleep(1)
print("The formula for the probability, will be 1 in the amount of possibilities.")
time.sleep(1)
print("So '1' would be 100% chance")
time.sleep(0.8)
print("If you win, that number will be doubled (in imaginary cash)")
time.sleep(0.8)
print("So 1 would only give you 2 imaginary dollars.")
time.sleep(1)

integer_check()
finished = False
while not finished:
    if user_input < 101 and user_input > 0:
        print("is you number " + str(user_input) + " ?")
        print("if it is let's proceed")
        time.sleep(1)

        lotterie_random = random.randint(1, + int(user_input))
        print("the winning number was ....")
        print("...........silence...............")
        time.sleep(0.3)
        print(lotterie_random)

        if user_input == lotterie_random:
            print("You won " + str(int(user_input) * 2) + " Dollars")
        else:
            print("You got nothing. );")
        finished = True
    else:
        print("'" + str(user_input) + "' isn't a number from 1 to 100, please try again.")
        integer_check()
print("Good game")

