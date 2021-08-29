import random

NUMBERS_PER_LINE = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45


number_of_quick_picks = int(input("How many quick picks? "))
for i in range(number_of_quick_picks):
    quick_picks = []
    for x in range(NUMBERS_PER_LINE):
        random_numbers = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        while random_numbers in quick_picks:
            random_numbers = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        quick_picks.append(random_numbers)
    quick_picks.sort()
    print(" ".join("{:2}".format(random_num) for random_num in quick_picks))