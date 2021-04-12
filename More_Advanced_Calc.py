num1 = int(input("Enter number 1: "))
op = input("Enter an operator: ")
num2 = int(input("Enter number 2: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid input")


# If statements for all the conditions +-*/, use elif for the preceeding last one