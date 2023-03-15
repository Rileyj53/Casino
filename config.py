from colorama import Fore
# import banking

# account = 10


def handle_input(question):
    usr_input = input(question)
    if usr_input.lower() == "end":
        print("\nGoodbye! " + Fore.RED + "* gets kicked out of casino *")
        quit()
    if usr_input.lower() == "quit":
        print("\nGoodbye! " + Fore.RED + "* gets kicked out of casino *")
        quit()
    elif usr_input.lower() == "bank":
        print("going to Bank")
        import banking
        banking.deposit()
    elif usr_input.lower() == "home":
        import games
        games.select()
        # print("going to Bank")
    else:
        return usr_input
