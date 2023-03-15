from colorama import Fore, Back, Style
import random
import config
import banking
import definitions
from definitions import *

# import main

seven = Fore.RED + "7" + Style.RESET_ALL
bar = Fore.WHITE + Back.BLACK + "Bar" + Style.RESET_ALL

ONE = ['🍒', '🍒', '🍒', '🍒', '🍋', '🍋', '🍋', '🍋', '🍋', '🍋', '🍋', '🍋', f'{bar}', f'{bar}', f'{seven}']
TWO = ['🍒', '🍋', '🍋', f'{bar}', f'{seven}']
THREE = ['🍒', '🍒', '🍒', '🍒', '🍒', '🍒', '🍋', '🍋', '🍋', '🍋', '🍋', '🍋', '🍋', '🍋', '🍋', '🍋', '🍋', '🍋', f'{bar}', f'{bar}',
         f'{seven}']


def place_bet():
    # print('In place_bet')
    while True:
        bet = config.handle_input("How much would you like to bet? ")
        if bet.isdigit():
            if int(bet) > definitions.account:
                print("You do not have enough money to bet that much!")
                banking.get_balance()
                print("Say 'bank' to access the cashier and add more")
            else:
                break
        else:
            print("Please enter a number.")

    return int(bet)


def spin_slot(bet):
    # print('In spin_slot')
    mult = 0
    slot1 = random.choice(ONE)
    slot2 = random.choice(TWO)
    slot3 = random.choice(THREE)

    if slot1 == slot2 == slot3:
        if slot2 == f'{seven}':
            mult = 5.0
        elif slot2 == '🍒':
            mult = 4.0
        elif slot2 == f'{bar}':
            mult = 3.0
        elif slot2 == '🍋':
            mult = 2.0

    elif slot1 == slot2 or slot2 == slot3:
        if slot2 == f'{seven}':
            mult = 3.33
        elif slot2 == '🍒':
            mult = 2.66
        elif slot2 == f'{bar}':
            mult = 2.0
        elif slot2 == '🍋':
            mult = 1.33
    else:
        mult = 0

    winnings = bet * mult

    return slot1, slot2, slot3, winnings


def user_spin(bet):
    # print('In user_spin')
    usr_input = ''
    config.handle_input("\nPress Enter to Spin\n")

    while True:
        if usr_input == 'bet':
            bet = place_bet()

        if int(bet) > definitions.account:
            print("You do not have enough money to bet that much!")
            banking.get_balance()

        banking.withdraw(bet)

        slot1, slot2, slot3, winnings = spin_slot(bet)

        banking.add(winnings)

        print(f"Result: {slot1} | {slot2} | {slot3}")

        if winnings == 0.0:
            # print('Line 92 - 96')
            print("Sorry Spin again\n")
            banking.get_balance()
            # print('IF')
            print("Press Enter to Spin again with the same bet")
            usr_input = config.handle_input("Or say bet to change your bet\n")
        elif definitions.account == 0:
            # print('ELIF Line 97 - 100')
            banking.nothing()
            break
            # ADD BANKING HERE
        else:
            # print('ELSE Line 102 - 106')
            print('Your Winnings are' + GREEN + '${:.2f}\n'.format(winnings) + RESET)
            banking.get_balance()
            # print('ELSE')
            print("Press Enter to Spin again with the same bet")
            usr_input = config.handle_input("Or say bet to change your bet\n")


def play():
    # bet = 100
    usr_input = ''
    print('Welcome to Slots!\n')
    banking.get_balance()

    bet = place_bet()

    user_spin(bet)


# play()