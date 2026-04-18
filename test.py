input = input("Hello")
try:
    input = int(input)
except ValueError:
    print("Not a number")

pepito = 1000
pepito += input
print(pepito)