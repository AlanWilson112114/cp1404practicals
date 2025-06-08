"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
>> A ValueError occurs when an operation or function receives an argument with the correct type but an inappropriate value
2. When will a ZeroDivisionError occur?
>>ZeroDivisionError occurs when a number is divided by zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
>>Yes,the corrected code is below
"""

denominator = 0
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print(f"Denominator cannot be zero!")
        denominator = int(input("Re-enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
