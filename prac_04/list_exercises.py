"""
 CP1404/CP5632 Practical 04
 """
# 1. Basic list operations
# Create an empty list to store user-input numbers
numbers = []

# Prompt the user for 5 numbers and add them to the list
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)

# Print the first and last numbers in the list
print("The first number is", numbers[0])
print("The last number is", numbers[-1])

# Print the smallest and largest numbers in the list
print("The smallest number is", min(numbers))
print("The largest number is", max(numbers))

# Calculate and print the average of the numbers
print("The average of the numbers is", sum(numbers) / len(numbers))

# 2. Woefully inadequate security checker
# Check if a username is in the list of authorised users

# Predefined list of authorised usernames
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
             'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command',
             'ExecState', 'InteractiveConsole', 'InterpreterInterface',
             'StartServer', 'bob']

# Prompt the user to enter their username
username = input("Enter username: ")

# Check if the entered username exists in the list
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
