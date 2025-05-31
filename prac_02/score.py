import random

def main():
    """Obtain a valid user score, then display both the user's performance and the performance of a random score."""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    print(determine_performance(score))
    score_random = random.randint(0, 100)
    print(f"Random score: {score_random}")
    print(determine_performance(score_random))


def determine_performance(score):
    """Get comment on performance based on the given score."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()
