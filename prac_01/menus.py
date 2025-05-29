# This program displays a menu and greets the user or says goodbye.
def display_menu():
    """Display the menu options."""
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")


def main():
    """Run the menu system."""
    name = input("Enter name: ")
    choice = ''
    while choice != 'Q':
        display_menu()
        choice = input(">>> ").upper()
        if choice == 'H':
            print("Hello", name)
        elif choice == 'G':
            print("Goodbye", name)
        elif choice != 'Q':
            print("Invalid choice")
    print("Finished.")


if __name__ == "__main__":
    main()
