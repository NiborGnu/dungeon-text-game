# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
# Text based RPG Game
# Made By Robin Ung 

import random
import diceroll
import time # Add a timer function and a scoreboard


def game():
    print(f'Hail {player.name} good to meet you!')
    level_one()


# Player 
class Player():
    """ Player setup """
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


def get_player_name():
    """ Get player name """
    print('Hail warrior! State your name: \n')
    while True:
        player_name = input('>')
        if len(player_name) <= 20:
            return player_name
        else:
            print(f"""I don't have room on my paper for that long a name!\n 
Do you have a nickname i can call you?(Max 20 characters)\n""")


# Difficulty
def difficulty():
    """ Choose difficulty between easy, normal or hard """
    print(f"""
What difficulty do you crave warrior?\n
[Easy] - 100hp\n
[Normal] - 50hp\n
[Hard] - 25hp\n""")
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


# Monsters
class Monster():
    """
    Creating monsters
    """
    def __init__(self, name, description, hp):
        self.name = name
        self.description = description
        self.hp = hp


goblin = Monster(
    'Goblin',
    f"""a monster.
It's wiry frame draped in tattered garments,
with a crooked grin revealing jagged teeth and
eyes gleaming with a mischievous glint""",
    5
)
ork = Monster(
    'Ork',
    'a towering and brutishly built shape, its grizzled body marked with scars',
    5
)
murloc = Monster(
    'Murloc',
    f"""a small, amphibious creature with webbed appendages,
emitting gurgling sounds""",
    5
)
cave_troll = Monster(
    'Cave Troll',
    f"""a hulking figure draped in crude hides,
its massive frame adorned with tangled mossy hair and thick,
gnarled limbs clutching a stone club,
its eyes glowing with a primal, fierce intensity""",
    5
)
forest_troll = Monster(
    'Forest Troll',
    'a creature taller than the average human, its rugged, bark-like skin',
    5
)
basilisk = Monster(
    'Basilisk',
    f"""a serpentine creature with shimmering scales of iridescent hues,
its piercing gaze freezing the air around it,
a forked tongue flickering as it hisses,
emanating an aura of petrifying danger""",
    5
)
wyvern = Monster(
    'Wyvern',
    f"""a formidable winged creature,
with scaled skin shimmering in the dim light, razor-sharp talons gripping
the cave floor as its leathery wings fold against its sleek body,
keen eyes fixated on the intruder with a calculated intensity,
ready to take flight at the slightest provocation""",
    5
)


def level_one():
    """ First route player can take """
    print(f"You enter a cave and you see {ork.description} it's an {ork.name}!")
    diceroll.dice_roll(player, ork)

    if player.hp >= 0:
        print(f"""
You survived the encountor!\n
Now you stand before a choice again will you go [left] or [right]?""")
        
        while True:
            choice_one = input('>').lower()
            if choice_one == 'left':
                print(f"""
You enter a dank cave with a puddle and you see {murloc.description} it's an
{murloc.name}!""")
                diceroll.dice_roll(player, murloc)
                if player.hp >= 0:
                    print(f"""
You survived the encountor!\n
Now you stand before a choice again will you go [left] or [right]?""")
            elif choice_one == 'right':
                print(f"""
You enter a new cave and you see {goblin.description} it's an {goblin.name}!""")
                diceroll.dice_roll(player, goblin)
                if player.hp >= 0:
                    print(f"""
You survived the encountor!\n
Now you stand before a choice again will you go [left] or [right]?""")
            else:
                print('Invalid choice. Choose [left] or [right].')


player_name = get_player_name()
player_hp = difficulty()
player = Player(player_name, player_hp)
game()