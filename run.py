# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
# Text based RPG Game
# Made By Robin Ung 

import random
import time


# Player 
class Player():
    """
    Player setup
    """
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


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


# Difficulty
def difficulty():
    """
    Choose difficulty between easy, normal or hard
    """
    print('What difficulty do you crave warrior?\n')
    print('[Easy] - 100hp\n')
    print('[Normal] - 50hp\n')
    print('[Hard] - 25hp\n')
    diff = input('>').lower()

    if diff == 'easy':
        print('Difficulty Easy - 100hp set\n')
        return 100
    elif diff == 'normal':
        print('Difficulty Normal - 50hp set\n')
        return 50
    elif diff == 'hard':
        print('Difficulty Hard - 25hp set\n')
        return 25
    else:
        print('Invalid difficulty. Try again\n')
        return difficulty()


# Player 
player_name = get_player_name()
player_hp = difficulty()
player = Player(player_name, player_hp)


# Monsters
class Monster():
    """
    Creating monsters
    """
    def __init__(self, name, description, hp):
        self.name = name
        self.description = description
        self.hp = hp


goblin = Monster('Goblin', 'its wiry frame draped in tattered garments, with a crooked grin revealing jagged teeth and eyes gleaming with a mischievous glint', 5)
ork = Monster('Ork', 'a towering and brutishly built, its grizzled body marked with scars', 5)
murloc = Monster('Murloc', 'a small, amphibious creature with webbed appendages, emitting gurgling sounds', 5)
cave_troll = Monster('Cave Troll', 'a hulking figure draped in crude hides, its massive frame adorned with tangled mossy hair and thick, gnarled limbs clutching a stone club, its eyes glowing with a primal, fierce intensity', 5)
forest_troll = Monster('Forest Troll', 'a creature taller than the average human, its rugged, bark-like skin', 5)
basilisk = Monster('Basilisk', 'a serpentine creature with shimmering scales of iridescent hues, its piercing gaze freezing the air around it, a forked tongue flickering as it hisses, emanating an aura of petrifying danger', 5)
wyvern = Monster('Wyvern', 'a formidable winged creature with scaled skin shimmering in the dim light, razor-sharp talons gripping the cave floor as its leathery wings fold against its sleek body, keen eyes fixated on the intruder with a calculated intensity, ready to take flight at the slightest provocation', 5)


def dice_roll(player, monster):
    """
    Battle the monster by rolling the dice.
    """
    print(f'Lets [roll] the dice and kill the {monster.name}')

    while True:
        roll = input('>')
        if roll == 'roll':
            player_damage = random.randint(1, 6)
            monster_damage = random.randint(1, 6)

            # Deduct damage from monster's and player's health points
            monster.hp -= player_damage
            player.hp -= monster_damage

            print(f"Player dealt {player_damage} damage. Monster's remaining HP: {monster.hp}")
            print(f"Monster dealt {monster_damage} damage. Player's remaining HP: {player.hp}")

            if monster.hp <= 0 or player.hp <= 0:
                break

    if monster.hp <= 0:
        print(f"The {monster.name} is dead!")
    elif player.hp <= 0:
        print(f"{player.name} has been defeated!")



