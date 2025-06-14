"""
CP1404/CP5632 Practical
Quick pick program
"""
import random

QUICK_PICK_LENGTH = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45



def main():
    """Ask user for number of quick picks, then generate and display them."""
    quick_picks_number = int(input("How many quick picks? "))
    while quick_picks_number < 0:
        print("That makes no sense!")
        quick_picks_number = int(input("How many quick picks? "))

    for _ in range(quick_picks_number):
        quick_pick = get_quick_pick(QUICK_PICK_LENGTH)
        # Print each number right-aligned in a 2-character field
        print(" ".join(f"{number:2}" for number in quick_pick))


def get_quick_pick(length):
    """Generate a single quick pick: a sorted list of unique random numbers."""
    quick_picks = []
    while len(quick_picks) < length:
        number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        if number not in quick_picks:
            quick_picks.append(number)
    return sorted(quick_picks)


# Run the program
main()
