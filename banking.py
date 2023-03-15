import config
from definitions import *
import definitions


def nothing():
    while True:
        print(MAGENTA + f"{top}")
        print("║" + "You do not have any money in your account".center(58) + "║")
        print("║" + "Please deposit money to play".center(58) + "║")
        print(f"{bottom}" + RESET)
        usr_input = config.handle_input("Say 'bank' to deposit money, or 'quit' to exit \n")


def deposit():
    old_balance = definitions.account
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                definitions.account = amount + old_balance
                print(f'\nYour new balance is ' + GREEN + f'${definitions.account}\n' + RESET)
                break
            else:
                print("Please enter a positive number greater than zero")
        else:
            print("Please enter a number.")

    return


def get_balance():
    if definitions.account == 0:
        nothing()

    else:
        print('You have ' + GREEN + '${:.2f}'.format(definitions.account) + RESET + ' in your account\n')
    return


def withdraw(amount):
    definitions.account -= amount
    # print(definitions.account)
    return


def add(amount):
    definitions.account += amount
    return


def just_check():
    if definitions.account == 0:
        nothing()
    return

# get_balance()
# nothing()