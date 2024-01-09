# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
# Text based Game RPG
# Made By Robin Ung 

import random
import time


class player():
    """
    Player setup
    """
    def __init__(self, name, hp):
        self.name = ''
        self.hp = 0


def get_player_name():
    """
    Get player name
    """
    print('Hail warrior! State your name: ')
    while True:
        player_name = input('>')
        if len(player_name) <= 20:
            return player_name
        else:
            print("I don't have room on my paper for that long a name! Do you have a nickname i can call you?")


def difficulty():
    print('What difficulty do you crave warrior?')
    print('[Easy] - 100hp')
    print('[Normal] - 50hp')
    print('[Hard] - 25hp')
    diff = input('>').lower()

    if diff == 'easy':
        print('Difficulty Easy - 100hp set')
    elif diff == 'normal':
        print('Difficulty Normal - 50hp set')
    elif diff == 'hard':
        print('Difficulty Hard - 25hp set')
    else:
        print('Invalid difficulty. Try again')
        difficulty()