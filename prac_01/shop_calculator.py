num = int(input("Number of items: "))
total = 0

for n in range(num):
    item_price = float(input("Price of item: "))
    total += item_price

if total >= 100:
    disc = total * 0.1
else:
    disc = 0

sum = total - disc

print(f"Total price for {num} items is ${sum:.2f}")
