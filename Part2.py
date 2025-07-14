# Critical Thinking Assignment 1: 
#Part 2:
#Write a Python program to find the multiplication and division of two numbers.
try:
    num1 = float(input("Please Enter the first numer: "))
    num2 = float(input("Please Enter a second number: "))
    multiplication = num1 * num2
    if num2 != 0:
        division = num1 / num2
    else:
        divsion = None
    print(f"The multiplication of {num1} and {num2} is: {multiplication}")
    if division is None:
        print("Dividing by zero is not allowed.")
    else:
        print(f"The division of {num1} and {num2} is: {division}")
except ValueError:
    print("Invalid input. Please enter numeric values.")
