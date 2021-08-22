total = 0
number_items = int(input("Please enter the number of items: "))
while number_items < 0:
    print("Invalid number of items!")
    number_items = int(input("Please enter the number of items: "))
for i in range(number_items):
    price = float(input("Please enter the price of item: "))
    total += price

if total > 100:
    total *= 0.9

print("The total price for {} items is ${:.2f}".format(number_items, total))