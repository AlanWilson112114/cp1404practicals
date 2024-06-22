import random

QUICK_PICK_LENGTH = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45


def main():
    quick_picks_number = int(input("How many quick picks do u wish ? "))
    column_length = QUICK_PICK_LENGTH
    row_length = quick_picks_number

    for row in range(row_length):
        quick_pick = get_quick_pick(column_length)
        print(', '.join([str(number) for number in quick_pick]))


def get_quick_pick(column_length):
    quick_picks = []
    for column in range(column_length):
        new_pick = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        while new_pick in quick_picks:  # ensure no repeated numbers
            new_pick = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        quick_picks.append(new_pick)
    return sorted(quick_picks)


main()
