"""
CP1404/CP5632 - Practical 03

File reading and writing exercises.
"""

name_file = "name.txt"
number_file = "numbers.txt"

# 1. Ask the user for their name and write it to name.txt using open/close
name = input("What is your name? ")
out_file = open(name_file, "w")
print(name, file=out_file)
out_file.close()

# 2. Read the name from name.txt and print a greeting
in_file = open(name_file, "r")
name_from_file = in_file.read().strip()  # strip() to clean newline
in_file.close()
print(f"Hi {name_from_file}!")

# 3. Read the first two numbers from numbers.txt and print their sum
# Using with block as instructed
with open(number_file, "r") as in_file:
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
print(number1 + number2)

# 4. Read all numbers from numbers.txt and print the total
total = 0
with open(number_file, "r") as in_file:
    for line in in_file:
        total += int(line.strip())  # strip in case of extra whitespace
print(total)
