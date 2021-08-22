# try:
#     numerator = int(input("Enter the numerator: "))
#     denominator = int(input("Enter the denominator: "))
#     fraction = numerator / denominator
#     print(fraction)
# except ValueError:
#     print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# print("Finished.")

# Questions:
# 1. When there's a decimal a value error will occur
# 2. When the denominator is enter as 0
# 3. yes, see below:

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
except ZeroDivisionError:
    fraction = 0
print(fraction)
