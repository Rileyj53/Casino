import banking
import time
import config
# import definitions
from definitions import *
# from colorama import Fore, Back, Style
import games


def main():
    # This is the welcome function, welcomes the user, teaches them how to play, and asks them if they want to add
    # money of they have none
    welcome()

    # This is the main game loop, it gives the user the option to choose a game
    games.select()


def welcome():
    # Welcome the user to the casino
    print(MAGENTA + f"{top}")
    print("║" + " Welcome to the Casino!".center(58) + "║")
    print(f"{bottom}" + RESET)
    print("\nWe have a variety of games to play, including: Slots, Blackjack, Roulette, and Poker!\n")
    time.sleep(3)
    print()

    # Print the rules of the casino
    print(BLUE + "Get ready to win big!\n" + RESET)
    print("- Say " + RED + "'end'" + RESET + " at any time to exit the casino and go home.")
    print("- Say " + RED + "'bank'" + RESET + " to access the cashier and manage your money.")
    print("- Say " + RED + "'home'" + RESET + " to end the current game and select a new one.\n")

    # Display the user's current balance
    print("Let's check your balance first.")
    print(YELLOW + f"{top}")
    print("║" + GREEN + f" Your current balance is ${account} ".center(58) + YELLOW + "║")
    print(f"{bottom}" + RESET)
    time.sleep(2)

    # Check if the user has any money in their account
    if account == 0:
        while True:
            usr_input = config.handle_input(
                # Ask the user if they would like to deposit money
                "\nyour balance is " + GREEN + "$0" + RESET + ", would you like to deposit money? (y/n) ")

            if usr_input.lower() in ["y", "yes"]:
                # If the user says yes, go to the deposit function in banking.py
                # print("Money")
                banking.deposit()
                break
            elif usr_input.lower() in ["n", "no"]:
                # If the user says no, kick them out of the casino for jokes
                time.sleep(1)
                print("\nYou cannot play without money! Goodbye! " + RED + "* gets kicked out of casino *")
                quit()
            else:
                # If the user enters an invalid response, tell them to enter a valid response
                time.sleep(1)
                print(RED + "\nPlease enter a valid response.\n")
    else:
        pass
    # This goes back to the main function and will continue to the games selection function

    time.sleep(2)


main()