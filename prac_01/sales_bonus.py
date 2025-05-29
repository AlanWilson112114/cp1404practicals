"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""


def calculate_bonus(sales):
    """Calculate bonus based on sales."""
    if sales < 1000:
        bonus = sales * 0.10
    else:
        bonus = sales * 0.15
    return bonus


def main():
    """Main program to repeatedly ask for user's sales and print the bonus until they enter a negative number."""
    sales = float(input("Enter sales: $"))
    while sales >= 0:
        bonus = calculate_bonus(sales)
        print(f"Bonus: ${bonus:.2f}")
        sales = float(input("Enter sales: $"))
    print("Thank you!")


if __name__ == "__main__":
    main()
