MIN_LENGTH = 2

def password_checker ():
    password = input("Enter a password of at least {} characters: ".format(MIN_LENGTH))
    while len(password) < MIN_LENGTH:
        password = input("Enter a password of at least {} characters: ".format(MIN_LENGTH))

    print('*' * len(password))


# password_checker()

def main():
    password = get_password(MIN_LENGTH)
    print_asterisks(password)


def get_password(minimum_length):
    password = input("Enter a password of at least {} characters: ".format(minimum_length))
    while len(password) < minimum_length:
        print("Password is too short")
        password = input("Enter a password of at least {} characters: ".format(minimum_length))
    return password


def print_asterisks(sequence):
    print('*' * len(sequence))


main()
