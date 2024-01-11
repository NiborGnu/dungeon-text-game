import monster
import player
import time
import os
from diceroll import dice_roll
from simple_term_menu import TerminalMenu

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def level_zero(player):
    """Dungeon entrance"""
    clear_screen()
    print(f"""
Hail {player.name}! Good to meet you!
You are cleared to move into the dungeon!
You enter the opening, and before you are 2 paths leading forth!\n
Which way will you go? [Left] or [Right]
Or will you [Quit] before entering!\n""")

    path = ['Left', 'Right', 'Quit']
    path_menu = TerminalMenu(path)

    while True:
        x = path_menu.show()
        if x == 0:
            clear_screen()
            print('\nYou choose the left path and start walking')
            level_one_first(player)
            # level 2 path
        elif x == 1:
            clear_screen()
            print('\nYou choose the right path and start walking')
            level_one_second(player)
            # level 2 path
        elif x == 2:
            print('Quitting...')
            # quit function

######## level 1 first encounter ########
def level_one_first(player):
    """Level 1 first choice from the left"""
    print(f"{monster.goblin.description}it's a{monster.goblin.name}!\n")
    dice_roll(player, monster.goblin)

    if player.hp >= 0:
        print(f"""
You survived the encounter!
And finds 2 more paths at the far end...\n
Now you stand before a choice again will you go [left] or [right]?\n""")
    path = ['Left', 'Right', 'Quit']
    path_menu = TerminalMenu(path)

    while True:
        x = path_menu.show()
        if x == 0:
            clear_screen()
            print('\nYou choose the left path and start walking')
            level_two_first(player)
            # level 2 path
        elif x == 1:
            clear_screen()
            print('\nYou choose the right path and start walking')
            level_two_second(player)
            # level 2 path
        elif x == 2:
            print('Quiting...')
            # quit function


######## level 1 second encounter ########
def level_one_second(player):
    """Level 1 second choice from the left"""
    print(f"{monster.ork.description}it's an{monster.ork.name}!\n")
    dice_roll(player, monster.ork)

    if player.hp >= 0:
        print(f"""
You survived the encounter!
And finds 2 more paths at the far end...\n
Now you stand before a choice again will you go [left] or [right]?\n""")
    path = ['Left', 'Right', 'Quit']
    path_menu = TerminalMenu(path)

    while True:
        x = path_menu.show()
        if x == 0:
            clear_screen()
            print('\nYou choose the left path and start walking')
            level_two_second(player)
            # level 2 path
        elif x == 1:
            clear_screen()
            print('\nYou choose the right path and start walking')
            level_two_third(player)
            # level 2 path
        elif x == 2:
            print('Quiting...')
            # quit function


######## level 2 first encounter ########
def level_two_first(player):
    """Level 2 first choice from the left"""
    print(f"{monster.ork.description}it's an{monster.ork.name}!\n")
    dice_roll(player, monster.ork)

    if player.hp >= 0:
        print(f"""
You survived the encounter!
And finds 2 more paths at the far end...\n
Now you stand before a choice again will you go [left] or [right]?\n""")
    path = ['Left', 'Right', 'Quit']
    path_menu = TerminalMenu(path)

    while True:
        x = path_menu.show()
        if x == 0:
            clear_screen()
            print('\nYou choose the left path and start walking')
            level_three_first(player)
            # level 3 path
        elif x == 1:
            clear_screen()
            print('\nYou choose the right path and start walking')
            level_three_second(player)
            # level 3 path
        elif x == 2:
            print('Quiting...')
            # quit function


######## level 2 second encounter ########
def level_two_second(player):
    """Level 2 second choice from the left"""
    print(f"{monster.murloc.description}it's a{monster.murloc.name}!\n")
    dice_roll(player, monster.murloc)

    if player.hp >= 0:
        print(f"""
You survived the encounter!
And finds 2 more paths at the far end...\n
Now you stand before a choice again will you go [left] or [right]?\n""")
    path = ['Left', 'Right', 'Quit']
    path_menu = TerminalMenu(path)

    while True:
        x = path_menu.show()
        if x == 0:
            clear_screen()
            print('\nYou choose the left path and start walking')
            level_three_second(player)
            # level 3 path
        elif x == 1:
            clear_screen()
            print('\nYou choose the right path and start walking')
            level_three_third(player)
            # level 3 path
        elif x == 2:
            print('Quiting...')
            # quit function


######## level 2 third encounter ########
def level_two_third(player):
    """Level 2 third choice from the left"""
    print(f"{monster.goblin.description}it's a{monster.goblin.name}!\n")
    dice_roll(player, monster.goblin)

    if player.hp >= 0:
        print(f"""
You survived the encounter!
And finds 2 more paths at the far end...\n
Now you stand before a choice again will you go [left] or [right]?\n""")
    path = ['Left', 'Right', 'Quit']
    path_menu = TerminalMenu(path)

    while True:
        x = path_menu.show()
        if x == 0:
            clear_screen()
            print('\nYou choose the left path and start walking')
            level_three_third(player)
            # level 3 path
        elif x == 1:
            clear_screen()
            print('\nYou choose the right path and start walking')
            level_three_fourth(player)
            # level 3 path
        elif x == 2:
            print('Quiting...')
            # quit function


######## level 3 first encounter ########
def level_three_first(player):
    """Level 3 first choice from the left"""
    print(f"{monster.wyvern.description}it's a{monster.wyvern.name}!\n")
    dice_roll(player, monster.wyvern)

    if player.hp >= 0:
        print(f"""
You survived the encounter!
And finds 2 more paths at the far end...\n
Now you stand before a choice again will you go [left] or [right]?\n""")
    path = ['Left', 'Right', 'Quit']
    path_menu = TerminalMenu(path)

    while True:
        x = path_menu.show()
        if x == 0:
            clear_screen()
            print('\nYou choose the left path and start walking')
            level_fourth_first(player)
            # level 4 path
        elif x == 1:
            clear_screen()
            print('\nYou choose the right path and start walking')
            level_fourth_second(player)
            # level 4 path
        elif x == 2:
            print('Quiting...')
            # quit function


######## level 3 second encounter ########
def level_three_second(player):
    """Level 3 second choice from the left"""
    print(f"""{monster.forest_troll.description}
it's a{monster.forest_troll.name}!\n""")
    dice_roll(player, monster.forest_troll)

    if player.hp >= 0:
        print(f"""
You survived the encounter!
And finds 2 more paths at the far end...\n
Now you stand before a choice again will you go [left] or [right]?\n""")
    path = ['Left', 'Right', 'Quit']
    path_menu = TerminalMenu(path)

    while True:
        x = path_menu.show()
        if x == 0:
            clear_screen()
            print('\nYou choose the left path and start walking')
            level_fourth_first(player)
            # level 4 path
        elif x == 1:
            clear_screen()
            print('\nYou choose the right path and start walking')
            level_fourth_second(player)
            # level 4 path
        elif x == 2:
            print('Quiting...')
            # quit function


######## level 3 third encounter ########
def level_three_third(player):
    """Level 3 third choice from the left"""
    print(f"""{monster.cave_troll.description}
    it's a{monster.cave_troll.name}!\n""")
    dice_roll(player, monster.cave_troll)

    if player.hp >= 0:
        print(f"""
You survived the encounter!
And finds 2 more paths at the far end...\n
Now you stand before a choice again will you go [left] or [right]?\n""")
    path = ['Left', 'Right', 'Quit']
    path_menu = TerminalMenu(path)

    while True:
        x = path_menu.show()
        if x == 0:
            clear_screen()
            print('\nYou choose the left path and start walking')
            level_fourth_second(player)
            # level 4 path
        elif x == 1:
            clear_screen()
            print('\nYou choose the right path and start walking')
            level_fourth_third(player)
            # level 4 path
        elif x == 2:
            print('Quiting...')
            # quit function


######## level 3 fourth encounter ########
def level_three_fourth(player):
    """Level 3 fourth choice from the left"""
    print(f"{monster.basilisk.description}it's a{monster.basilisk.name}!\n")
    dice_roll(player, monster.basilisk)

    if player.hp >= 0:
        print(f"""
You survived the encounter!
And finds 2 more paths at the far end...\n
Now you stand before a choice again will you go [left] or [right]?\n""")
    path = ['Left', 'Right', 'Quit']
    path_menu = TerminalMenu(path)

    while True:
        x = path_menu.show()
        if x == 0:
            clear_screen()
            print('\nYou choose the left path and start walking')
            level_fourth_second(player)
            # level 4 path
        elif x == 1:
            clear_screen()
            print('\nYou choose the right path and start walking')
            level_fourth_third(player)
            # level 4 path
        elif x == 2:
            print('Quiting...')
            # quit function


######## level 4 first encounter ########
def level_fourth_first(player):
    """Level 4 first choice from the left"""
    texts = [    
"#############################################",
"# In the depths of the dungeon, the path    #",
"# abruptly transformed beneath your feet,   #",
"# shifting from rugged rock to a smooth     #",
"# wooden floor. Surprised, you cautiously   #",
"# continued forward, guided by the          #",
"# unexpected change in terrain.             #",
"# The dim, foreboding corridors gave way    #",
"# to a warmly lit room, its shelves adorned #",
"# with countless tomes. As you took in the  #",
"# sight of this peculiar library, a figure  #",
"# caught your eye. A old bent wizard        #",
"# stood amidst the books, engrossed in the  #",
"# ancient knowledge they held.              #",
"# He looked up from his reading as you      #",
"# entered, his wise eyes meeting yours.     #",
"# With a gentle smile, the wizard said:     #",
"# Greetings, adventurer. The path has led   #",
"# you to my sanctuary of knowledge. Would   #",
"# you seek something more? Perhaps the      #",
"# allure of treasure awaits you. Would you  #",
"# like to be transported to its hidden      #",
"# location?                                 #",
"#                                           #",
"# The offer hung in the air, and the        #",
"# possibilities echoed in the hallowed      #",
"# room of books. What choice will you make? #",
"#############################################"
]
    for text in texts:
        print(text)
        time.sleep(1)

    path = ['Take the offer', "Don't take the offer", 'Quit']
    path_menu = TerminalMenu(path)

    while True:
        x = path_menu.show()
        if x == 0:
            print(f"""
##################################################
# Upon accepting the offer, the wizard instructs #
# you to step into a magic circle. As he utters  #
# the incantation, the last image burned into    #
# your memory is the wizard's sinister smile.    #
# You've fallen victim to a cunning trick!       #
##################################################
""")
            time.sleep(5)
            level_zero(player)
        elif x == 1:
            print('\nYou choose the right path and start walking')
            # Win
        elif x == 2:
            print('Quiting...')
            # quit function


######## level 4 second encounter ########
def level_fourth_second(player):
    """Level 4 second choice from the left"""
    print(f"{monster.basilisk.description}it's a{monster.basilisk.name}!\n")
    dice_roll(player, monster.basilisk)

    if player.hp >= 0:
        print(f"""
You survived the encounter!
And finds 2 more paths at the far end...\n
Now you stand before a choice again will you go [left] or [right]?\n""")
    path = ['Left', 'Right', 'Quit']
    path_menu = TerminalMenu(path)

    while True:
        x = path_menu.show()
        if x == 0:
            print('\nYou choose the left path and start walking')
            # win --> Move on
        elif x == 1:
            print('\nYou choose the right path and start walking')
            # lose
        elif x == 2:
            print('Quiting...')
            # quit function


######## level 4 third encounter ########
def level_fourth_third(player):
    """Level 4 third choice from the left"""
    print(f"{monster.basilisk.description}it's a{monster.basilisk.name}!\n")
    dice_roll(player, monster.basilisk)

    if player.hp >= 0:
        print(f"""
You survived the encounter!
And finds 2 more paths at the far end...\n
Now you stand before a choice again will you go [left] or [right]?\n""")
    path = ['Left', 'Right', 'Quit']
    path_menu = TerminalMenu(path)

    while True:
        x = path_menu.show()
        if x == 0:
            print('\nYou choose the left path and start walking')
            # Lose
        elif x == 1:
            print('\nYou choose the right path and start walking')
            # Win
        elif x == 2:
            print('Quiting...')
            # quit function


######## level 5 encounter ########
def level_five_first(player):
    """Level 5 'Boss fight'"""
    print(f"""{monster.black_dragon.description}
it's a{monster.black_dragon.name}!!!\n""")
    dice_roll(player, monster.black_dragon)

    if player.hp >= 0:
        print(f"""You survived the encountor!\n""")
    
    
    
    
    path = ['Left', 'Right', 'Quit']
    path_menu = TerminalMenu(path)

    while True:
        x = path_menu.show()
        if x == 0:
            print('\nYou choose the left path and start walking')
            # Lose
        elif x == 1:
            print('\nYou choose the right path and start walking')
            # Win
        elif x == 2:
            print('Quiting...')
            # quit function
