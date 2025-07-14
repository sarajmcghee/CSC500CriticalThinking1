# Critical Thinking Assignment 1: 
#Part 1:
#Write a Python program to find the addition and subtraction of two numbers.

#Ask the user to input two numbers (num1 and num2). Given those two numbers, add them together to find the output. Also, subtract the two numbers to find the output.
try:
    num1 = float(input("Please Enter a Number: "))
    num2 = float(input("Please Enter a Second Number: "))
    addition = num1 + num2
    subtraction = num1 -num2
    print(f"The addition result of {num1} and {num2} is: {addition}")
    print(f"The subtraction result of {num1} and {num2} is: {subtraction}")
except ValueError:
    print("Invalid input. Please enter numeric values.")
    