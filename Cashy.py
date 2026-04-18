funds = 1000
amount = 1000
option = 0

def amount_input(message):
    global amount
    while 1 == 1:
        amount = input(message + ": ")
        try:
            amount = int(amount)
            break
        except ValueError:
            print("'" + str(amount) + "' Not a valid input")

while not option == 4:
    print("---Cash register---")
    print("1. Add money")
    print("2. Withdraw money")
    print("3. See current funds")
    print("4. EXIT cash register")

    option = int(input("Please select an option: "))

    if option == 1:
        print("Please input the amount of that will be added to your funds")
        amount_input("Amount of money: ")
        funds += amount
        print("Transaction success!")
    elif option == 2:
        print("Please input the amoun of money to be withdrawed")
        amount_input("amount of money")
        if amount <= funds:
            funds -= amount
            print("Transaction success!")
        else:
            print("You don't have enough funds")
    elif option == 3:
        print("Funds =" + str(funds))
    elif option == 4:
        print("Goodbye!")
    else:
        print("Not a valid input")
        print("please try again")