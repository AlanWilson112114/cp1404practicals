"""
CP1404/CP5632 Practical
Email to name dictionary
"""


def main():
    """Prompt user for email addresses and store names associated with them in a dictionary."""
    email_to_name = {}  # Dictionary to store email and corresponding names
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")  # Ask for actual name if guess is incorrect
        email_to_name[email] = name  # Add email and name to dictionary
        email = input("Email: ")

    # Display the collected email-name pairs
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """Guess a person's name based on their email prefix (before the @ sign)."""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
