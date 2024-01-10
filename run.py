# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
# Text based RPG Game
# Made By Robin Ung

import random
import monster
import diceroll
import time  # Add a timer function and a scoreboard
from simple_term_menu import TerminalMenu


def main_game():
    print(f'Hail {player.name} good to meet you!')
    level_one()


# Player
class Player():
    """Player setup"""
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


def get_player_name():
    """Get player name"""
    print('Hail warrior! State your name: \n')
    while True:
        player_name = input('>')
        if len(player_name) <= 20:
            return player_name
        else:
            print(f"""
I don't have room on my paper for that long a name!\n
Do you have a nickname i can call you?(Max 20 characters)\n""")


# Difficulty
def difficulty():
    """Choose difficulty between easy, normal or hard"""
    print('What difficulty do you crave, warrior?\n')
    diff = ['Easy - 100 HP', 'Normal - 50 HP', 'Hard - 25 HP']
    main_menu = TerminalMenu(diff)
    x = main_menu.show()

    if x == 0:
        print('Difficulty Easy - 100hp set\n')
        return 100
    elif x == 1:
        print('Difficulty Normal - 50hp set\n')
        return 50
    elif x == 2:
        print('Difficulty Hard - 25hp set\n')
        return 25


def level_one():
    """First route player can take"""
    print(f"""\nYou enter a cave and you see {monster.ork.description}
it's an {monster.ork.name}!\n""")
    diceroll.dice_roll(player, monster.ork)

    if player.hp >= 0:
        print(f"""
You survived the encountor!\n
Now you stand before a choice again will you go [left] or [right]?""")

        while True:
            choice_one = input('>').lower()
            if choice_one == 'left':
                print(f"""
You enter a dank cave with a puddle and you see {monster.murloc.description}
it's an {monster.murloc.name}!""")
                diceroll.dice_roll(player, monster.murloc)
                if player.hp >= 0:
                    print(f"""
You survived the encountor!\n
Now you stand before a choice again will you go [left] or [right]?""")
            elif choice_one == 'right':
                print(f"""
You enter a new cave and you see {monster.goblin.description}
it's an {monster.goblin.name}!""")
                diceroll.dice_roll(player, monster.goblin)
                if player.hp >= 0:
                    print(f"""
You survived the encountor!\n
Now you stand before a choice again will you go [left] or [right]?""")
            else:
                print('Invalid choice. Choose [left] or [right].')


player_name = get_player_name()
player_hp = difficulty()
player = Player(player_name, player_hp)
main_game()