# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
# Text based RPG Game
# Made By Robin Ung

from player import Player, get_player_name, difficulty
import paths
import time  # Add a timer function and a scoreboard
from simple_term_menu import TerminalMenu


def main_game():
    player_name = get_player_name()
    player_hp = difficulty()
    player = Player(player_name, player_hp)
    paths.level_zero(player)

def main_start_menu():
    print(f"""
    ####################################
    #   Step into the Dungeon Game!    #
    # As a warrior, seek glory or face #
    #  the perilous embrace of death.  #
    #    Good luck on your journey!    #
    #    See you on the other side!    #
    ####################################
    """)

    options = ['Start Game', 'How to play', 'Quit']
    main_menu = TerminalMenu(options)
    x = main_menu.show()

    if x == 0:
        main_game()
    elif x == 1:
        print('How to play: ...')
    elif x == 2:
        print('Exiting the game. Goodbye!')

main_start_menu()