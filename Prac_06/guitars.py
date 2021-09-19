from Prac_06.guitar import Guitar


def main():
    guitars = []

    # print("My guitars!")
    # name = input("Input your name: ")
    # while name != "":
    #     year = int(input("Input a year: "))
    #     cost = float(input("Input the cost: "))
    #     guitar_to_add = Guitar(name, year, cost)
    #     guitars.append(guitar_to_add)
    #     print(guitar_to_add, "added.")
    #     name = input("Name: ")
    # else:
    #     input("Input your name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))


main()
