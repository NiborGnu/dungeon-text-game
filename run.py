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
    print('Hail warrior! State your name: \n')
    while True:
        player_name = input('>')
        if len(player_name) <= 20:
            return player_name
        else:
            print("I don't have room on my paper for that long a name!\n")
            print('Do you have a nickname i can call you?\n')


def difficulty():
    print('What difficulty do you crave warrior?\n')
    print('[Easy] - 100hp\n')
    print('[Normal] - 50hp\n')
    print('[Hard] - 25hp\n')
    diff = input('>').lower()

    if diff == 'easy':
        print('Difficulty Easy - 100hp set\n')
    elif diff == 'normal':
        print('Difficulty Normal - 50hp set\n')
    elif diff == 'hard':
        print('Difficulty Hard - 25hp set\n')
    else:
        print('Invalid difficulty. Try again\n')
        difficulty()


class monster():
    def __init__(self, name, description, health):
        self.name = name
        self.description = description
        self.health = 0

goblin = monster('Goblin', 'its wiry frame draped in tattered garments, with a crooked grin revealing jagged teeth and eyes gleaming with a mischievous glint', 5)
ork = monster('Ork', 'a towering and brutishly built, its grizzled body marked with scars', 5)
murloc = monster('Murloc', 'a small, amphibious creature with webbed appendages, emitting gurgling sounds', 5)
cave_troll = monster('Cave Troll', 'a hulking figure draped in crude hides, its massive frame adorned with tangled mossy hair and thick, gnarled limbs clutching a stone club, its eyes glowing with a primal, fierce intensity', 5)
forest_troll = monster('Forest Troll', 'a creature taller than the average human, its rugged, bark-like skin' 5)
basilisk = monster('Basilisk', 'a serpentine creature with shimmering scales of iridescent hues, its piercing gaze freezing the air around it, a forked tongue flickering as it hisses, emanating an aura of petrifying danger' 5)
wyvern = monster('Wyvern', 'a formidable winged creature with scaled skin shimmering in the dim light, razor-sharp talons gripping the cave floor as its leathery wings fold against its sleek body, keen eyes fixated on the intruder with a calculated intensity, ready to take flight at the slightest provocation' 5)
