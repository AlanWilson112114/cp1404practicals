# a. count in 10s from 0 to 100: 0 10 20 30 40 50 60 70 80 90 100
print("a.")
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b. count down from 20 to 1: 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1
print("b.")
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c. print n stars
print("c.")
num_stars = int(input("Number of stars: "))
for _ in range(num_stars):
    print('*', end='')
print()

# d. print n lines of increasing stars
print("d.")
for i in range(1, num_stars + 1):
    print('*' * i)
