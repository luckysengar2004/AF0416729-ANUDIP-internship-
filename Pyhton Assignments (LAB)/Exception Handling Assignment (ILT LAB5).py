#Q-1- Write a program to handle a ZeroDivisionError exception when dividing a number by zero.
num1=int(input("Enter first number:- "))
num2=int(input("Enter second number:- "))
try:
    print(num1/num2)
except ZeroDivisionError as e:
    print(e)

#Q-2- Write a python program that prompts the user to inputan integer and raises a valueError exception if the input is not valid integer.
num1=int(input("Enter first number:- "))
num2=int(input("Enter second number:- "))
try:
    print(num1/num2)
except ValueError as e:
    print(e)

#Q-3- Write a python program that opens a file and handle a FileNotFoundError exception if the file does not exist.
num1=int(input("Enter first number:- "))
num2=int(input("Enter second number:- "))
try:
    print(num1/num2)
    open("Lucky.txt")
except FileNotFoundError as e:
    print(e)

#Q-4- Write a pyhton program that prompts the user to input two numbers and rasises a TypeError exception if the inputs are not numerical.
def get_number(prompt):
    user_input = input(prompt)
    if not user_input.isdigit():
        raise TypeError(f"Input '{user_input}' is not a numerical value.")
    return int(user_input)
try:
    number1 = get_number("Enter the first number: ")
    number2 = get_number("Enter the second number: ")
    print(f"The numbers you entered are {number1} and {number2}.")
except TypeError as e:
    print(e)
