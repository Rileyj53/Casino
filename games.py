import time
from definitions import *
import banking
import config
import slots


def select():
    banking.just_check()
    games = {
        "slots": slots.play,
        # "blackjack": blackjack.play,
        # "roulette": roulette.play,
        # "poker": poker.play
    }

    valid_games = ", ".join(games.keys())

    while True:
        print(f"We have a variety of games available to play! including: " + BLUE + f"{valid_games}!\n" + RESET)
        time.sleep(1)
        game = config.handle_input("Let's get started! What game would you like to play? ")
        game_func = games.get(game.lower())
        if game_func:
            game_func()
        else:
            print(RED + f"\n{game} is not a game we have! Please enter a valid game.\n" + RESET)
            time.sleep(2)


# select()
