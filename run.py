from player import Player, get_player_name, difficulty
import paths
import time
from simple_term_menu import TerminalMenu
import os
import sys

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def main_game():
    """Main function to start the game."""
    player_name = get_player_name()
    player_hp = difficulty()
    player = Player(player_name, player_hp)
    paths.level_zero(player)


def main_start_menu():
    """Displays the main menu and handles user choices."""
    clear_screen()
    print(f"""
####################################
#   Step into the Dungeon Game!    #
# As a warrior, seek glory or face #
#  the perilous embrace of death.  #
#    Good luck on your journey!    #
#    See you on the other side!    #
####################################
""")

    options = ['Start Game', 'How to play', 'Restart/Quit']
    main_menu = TerminalMenu(options)
    x = main_menu.show()

    if x == 0:
        main_game()
    elif x == 1:
        print('How to play: ...')
    elif x == 2:
        restart_quit_game()


def restart_quit_game():
    """Quit the game"""
    clear_screen()
    print("Do you wan't to restart or quit playing?")

    options = ['Restart Game', 'Quit']
    quit_menu = TerminalMenu(options)
    x = quit_menu.show()

    if x == 0:
        os.execl(sys.executable, os.path.abspath("run.py"), *sys.argv)

    elif x == 1:
        print(f"""
#####################################
# Thank you for playing my dungeon! #
#  See you on your next adventure!  #
#       Quitting in 2 second...     #
#####################################
""")
        time.sleep(2)
        sys.exit(0)

main_start_menu()