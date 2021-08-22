# for odd numbers from 0 - 20

for i in range(1, 21, 2):
    print(i, end=' ')
print()

# Task A

for i in range(0, 101, 10):
    print(i, end=' ')
print()

# Task B

for i in range(20, 0, -1):
    print(i, end=' ')
print()

# Task C

number_of_stars = int(input("Please enter the number of stars: "))
for i in range(number_of_stars):
    print('*', end=' ')
print()

#Task D

for i in range(1, number_of_stars + 1):
    print('*' * i)
print()