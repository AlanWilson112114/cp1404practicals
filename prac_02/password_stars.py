def main():
    """Obtain a password that meets the minimum length requirements and display it as asterisks."""
    minimum_length = 3
    password = get_password(minimum_length)
    print_asterisks(password)


def print_asterisks(password):
    """Display a number of asterisks corresponding to the length of the input string."""
    print(len(password) * "*")


def get_password(minimum_length):
    """Return valid password from the user"""
    password = input("Enter password: ")
    while len(password) < minimum_length:
        print(f"Password must be at least {minimum_length} characters long.")
        password = input("Renter password: ")
    return password


main()
