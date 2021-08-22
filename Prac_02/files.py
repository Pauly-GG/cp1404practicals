# # Files question 1
# out_file = open("name.txt", "w")
# name = input("What is your name? ")
# print(name, file=out_file)
# out_file.close()
#
# # Files question 2
# in_file = open("name.txt", "r")
# name = in_file.read().strip()
# in_file.close()
# print("Your name is", name)
#
# # Files question 3
# in_file = open("numbers.txt", "r")
# number1 = int(in_file.readline())
# number2 = int(in_file.readline())
# in_file.close()
# print(number1 + number2)

# Files question 4
# in_file = open("numbers.txt", "r")
#
# lines = in_file.readlines()
# sum = 0
#
# for line in lines:
#     for x in line:
#         if x.isdigit() == True:
#             sum = sum + int(x)
# print(sum)
# in_file.close()



