# This program calculates the total price for multiple items and applies a discount.
num = int(input("Number of items: "))
total = 0

for n in range(num):
    item_price = float(input("Price of item: "))
    total += item_price

if total >= 100:
    disc = total * 0.1
else:
    disc = 0

final_price = total - disc

print(f"Total price for {num} items is ${final_price:.2f}")
