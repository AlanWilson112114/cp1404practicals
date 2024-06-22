def main():
    """Ask the user for name and email then store it in the dictionary"""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        name_confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if name_confirmation not in ['y', '']:
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    print("")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    name = email.split("@")[0]
    name = name.replace(".", " ").title()
    return name


main()
