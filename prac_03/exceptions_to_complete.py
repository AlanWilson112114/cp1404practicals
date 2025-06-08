"""
CP1404/CP5632 - Practical
"""

is_finished = False
result = None
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
    except ValueError:
        print("Please enter a valid integer.")
    else:
        is_finished = True
print("Valid result is:", result)
