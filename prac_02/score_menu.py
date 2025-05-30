def main():
    """Display user interface to get valid score, print the stars"""
    menu = """(G)et a valid score 
(P)rint result 
(S)how stars 
(Q)uit"""
    score = int(input("Enter a score between 1 and 100: "))
    while is_invalid_score(score):
        print("Invalid score")
        score = int(input("Enter a score between 1 and 100: "))

    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = int(input("Enter a score between 1 and 100: "))
            while is_invalid_score(score):
                print("Invalid score")
                score = int(input("Enter a score between 1 and 100: "))
        elif choice == "P":
            print(determine_performance(score))
        elif choice == "S":
            print(get_star_string(score))
        else:  # Invalid option
            print("Invalid")
        print(menu)
        choice = input(">>> ").upper()
    print("Farewell")


def get_star_string(score):
    """Return a string of asterisks equal to the score."""
    return score * "*"


def is_invalid_score(score):
    """Return true if user's score input is invalid"""
    return score < 0 or score > 100


def determine_performance(score):
    """Provide feedback regarding performance corresponding to the entered score."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
