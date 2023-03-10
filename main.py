from banking import *
from betting import *


def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    print(f"You have deposited ${balance} and are betting ${bet} on {lines} lines.")
    print(f"Your total bet is ${bet * lines}, Good luck!")

main()