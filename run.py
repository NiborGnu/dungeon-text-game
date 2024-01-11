# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
# Text based RPG Game
# Made By Robin Ung

import random
import paths
import player
import time  # Add a timer function and a scoreboard
from simple_term_menu import TerminalMenu


def main_game():
    paths.level_zero()

main_game()