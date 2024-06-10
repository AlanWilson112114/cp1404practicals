"""
CP1404 Practical 03 Hunter Kruger-Ilingworth
1. Write code that asks the user for their name, then opens a file called name.txt and writes that name to it. Use open and close for this question.

2. In the same file, but as if it were a separate program, write code that opens "name.txt" and reads the name (as above) then prints (note the exact output),
Hi Bob! (or whatever the name is in the file). Do not simply print the user's input variable!
Use open and close for this question.

3.Create a text file called numbers.txt and save it in your prac directory. Put the following three numbers on separate lines in the file and save it:
17
42
400
Write code that opens numbers.txt, reads only the first two numbers, adds them together then prints the result, which should be... 59. Use with instead of open and close for this question.

4. Now write a fourth block of code that prints the total for all lines in numbers.txt. This should work for a file with any number of numbers. Use with instead of open and close for this question."""

name_file = "name.txt"
number_file = "numbers.txt"

# 1)
name = input("What is your name? ")
with open(name_file, "w") as file:
    print(f"{name}", file=file)

# 2)
with open(name_file, "r") as file:
    text = file.read()
    print(f"Hi {text}")

# 3)
numbers = []
with open(number_file, "r") as file:
    for _ in range(2):
        numbers.append(int(file.readline().strip()))
result = numbers[0] + numbers[1]
print(result)

# 4)
total = 0

with open('numbers.txt', 'r') as file:
    for line in file:
        total += int(line.strip())

print(total)

