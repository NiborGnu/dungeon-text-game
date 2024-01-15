import os
import sys
from simple_term_menu import TerminalMenu


def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def restart_quit_game():
    """Quit the game."""
    options = ['Restart Game', 'Quit', 'Back']
    quit_menu = TerminalMenu(options)
    x = quit_menu.show()

    if x == 0:
        os.execl(sys.executable, sys.executable, *sys.argv)

    elif x == 1:
        print(f"""
#####################################
# Thank you for playing my dungeon! #
# See you on your next adventure!   #
#####################################
""")
        sys.exit(0)

    elif x == 2:
        return
