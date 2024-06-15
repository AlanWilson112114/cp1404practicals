number_of_prompts = 5
numbers = []

for i in range(number_of_prompts):
    numbers.append(int(input(f"Number: ")))

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers) / len(numbers)}")
