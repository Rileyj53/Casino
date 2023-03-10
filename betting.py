MAX_LINES = 5
MAX_BET = 100
MIN_BET = 1


def get_number_of_lines():
    while True:
        lines = input("How many lines would you like to bet on (1- " + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid number of lines")
        else:
            print("Please enter a number.")

    return lines


def get_bet():
    while True:
        print(f"This machine has a minimum bet of ${MIN_BET} and a maximum bet of ${MAX_BET}")
        bet = input("How much would you like to bet on each line? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Please enter a bet between ${MIN_BET} and ${MAX_BET}")
        else:
            print("Please enter a number.")

    return bet
