import sys


def add(num1, num2):
    num1 = num1 + num2
    print("The result is " + str(num1))
    carryon(num1)
    operator = input("Enter operator: (add/subtract/multiply/divide) ")
    num2 = float(input("Enter second number: "))
    selectchoice(num1, num2, operator)


def subtract(num1, num2):
    num1 = num1 - num2
    print("The result is " + str(num1))
    carryon(num1)
    operator = input("Enter operator: (add/subtract/multiply/divide) ")
    num2 = float(input("Enter second number: "))
    selectchoice(num1, num2, operator)


def multiply(num1, num2):
    num1 = num1 * num2
    print("The result is " + str(num1))
    carryon(num1)
    operator = input("Enter operator: (add/subtract/multiply/divide) ")
    num2 = float(input("Enter second number: "))
    selectchoice(num1, num2, operator)


def divide(num1, num2):
    num1 = num1 / num2
    print("The result is " + str(num1))
    carryon(num1)
    operator = input("Enter operator: (add/subtract/multiply/divide) ")
    num2 = float(input("Enter second number: "))
    selectchoice(num1, num2, operator)


def carryon(num1):
    ans = input("Would you like to restart or continue to modify current number? (restart/continue) ")
    if ans == "restart":
        main()
    else:
        print("Current number is: " + str(num1))
        return


def selectchoice(num1, num2, operator):
    if operator == "add":
        add(num1, num2)
    elif operator == "subtract":
        subtract(num1, num2)
    elif operator == "multiply":
        multiply(num1, num2)
    elif operator == "divide":
        divide(num1, num2)
    elif operator == "finish":
        sys.exit("Your final number is " + str(num1) + "")


def main():
    num1 = float(input("Enter first number: "))
    choice = input("Enter operator: (add/subtract/multiply/divide) ")
    num2 = float(input("Enter second number: "))
    selectchoice(num1, num2, choice)


main()
