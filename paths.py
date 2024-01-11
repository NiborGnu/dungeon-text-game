# Paths true the dungen

import monster
import player
from diceroll import dice_roll
from simple_term_menu import TerminalMenu

def level_zero():
    """Dungeon entrence"""
    print(f"""
Hail {player.player.name} good to meet you!
You are cleared to move into the dungeon!
You enter the opening and before you are 2 paths leading forth!\n
Where way will you go? [Left] or [Right]
Or will you [Quit] before entering!\n""")
    path = ['Left', 'Right', 'Quit']
    path_menu = TerminalMenu(path)

    while True:
        x = path_menu.show()
        if x == 0:
            print('\nYou choose the left path and start walking')
            level_one_first()
            # level 2 path
        elif x == 1:
            print('\nYou choose the right path and start walking')
            level_one_second()
            # level 2 path
        elif x == 2:
            print('quiting...')
            # quit function

######## level 1 first encounter ########
def level_one_first():
    """First route player can take"""
    print(f"{monster.goblin.description}it's a{monster.goblin.name}!\n")
    dice_roll(player.player, monster.goblin)

    if player.player.hp >= 0:
        print(f"""
You survived the encountor!
And finds 2 more paths at the far end...\n
Now you stand before a choice again will you go [left] or [right]?\n""")
    path = ['Left', 'Right', 'Quit']
    path_menu = TerminalMenu(path)

    while True:
        x = path_menu.show()
        if x == 0:
            print('\nYou choose the left path and start walking')
            level_two_first()
            # level 2 path
        elif x == 1:
            print('\nYou choose the right path and start walking')
            level_two_second()
            # level 2 path
        elif x == 2:
            print('quiting...')
            # quit function


######## level 1 second encounter ########
def level_one_second():
    """First route player can take"""
    print(f"{monster.ork.description}it's an{monster.ork.name}!\n")
    dice_roll(player.player, monster.ork)

    if player.player.hp >= 0:
        print(f"""
You survived the encountor!
And finds 2 more paths at the far end...\n
Now you stand before a choice again will you go [left] or [right]?\n""")
    path = ['Left', 'Right', 'Quit']
    path_menu = TerminalMenu(path)

    while True:
        x = path_menu.show()
        if x == 0:
            print('\nYou choose the left path and start walking')
            level_two_second()
            # level 2 path
        elif x == 1:
            print('\nYou choose the right path and start walking')
            level_two_third()
            # level 2 path
        elif x == 2:
            print('quiting...')
            # quit function


######## level 2 first encounter ########
def level_two_first():
    """First route player can take"""
    print(f"{monster.ork.description}it's an{monster.ork.name}!\n")
    dice_roll(player.player, monster.ork)

    if player.player.hp >= 0:
        print(f"""
You survived the encountor!
And finds 2 more paths at the far end...\n
Now you stand before a choice again will you go [left] or [right]?\n""")
    path = ['Left', 'Right', 'Quit']
    path_menu = TerminalMenu(path)

    while True:
        x = path_menu.show()
        if x == 0:
            print('\nYou choose the left path and start walking')
            level_three_first()
            # level 3 path
        elif x == 1:
            print('\nYou choose the right path and start walking')
            level_three_second()
            # level 3 path
        elif x == 2:
            print('quiting...')
            # quit function


######## level 2 second encounter ########
def level_two_second():
    """First route player can take"""
    print(f"{monster.murloc.description}it's a{monster.murloc.name}!\n")
    dice_roll(player.player, monster.murloc)

    if player.player.hp >= 0:
        print(f"""
You survived the encountor!
And finds 2 more paths at the far end...\n
Now you stand before a choice again will you go [left] or [right]?\n""")
    path = ['Left', 'Right', 'Quit']
    path_menu = TerminalMenu(path)

    while True:
        x = path_menu.show()
        if x == 0:
            print('\nYou choose the left path and start walking')
            level_three_second()
            # level 3 path
        elif x == 1:
            print('\nYou choose the right path and start walking')
            level_three_third()
            # level 3 path
        elif x == 2:
            print('quiting...')
            # quit function


######## level 2 third encounter ########
def level_two_third():
    """First route player can take"""
    print(f"{monster.goblin.description}it's a{monster.goblin.name}!\n")
    dice_roll(player.player, monster.goblin)

    if player.player.hp >= 0:
        print(f"""
You survived the encountor!
And finds 2 more paths at the far end...\n
Now you stand before a choice again will you go [left] or [right]?\n""")
    path = ['Left', 'Right', 'Quit']
    path_menu = TerminalMenu(path)

    while True:
        x = path_menu.show()
        if x == 0:
            print('\nYou choose the left path and start walking')
            level_three_third()
            # level 3 path
        elif x == 1:
            print('\nYou choose the right path and start walking')
            level_three_fourth()
            # level 3 path
        elif x == 2:
            print('quiting...')
            # quit function


######## level 3 first encounter ########
def level_three_first():
    """First route player can take"""
    print(f"{monster.wyvern.description}it's a{monster.wyvern.name}!\n")
    dice_roll(player.player, monster.wyvern)

    if player.player.hp >= 0:
        print(f"""
You survived the encountor!
And finds 2 more paths at the far end...\n
Now you stand before a choice again will you go [left] or [right]?\n""")
    path = ['Left', 'Right', 'Quit']
    path_menu = TerminalMenu(path)

    while True:
        x = path_menu.show()
        if x == 0:
            print('\nYou choose the left path and start walking')
            level_fourth_first()
            # level 4 path
        elif x == 1:
            print('\nYou choose the right path and start walking')
            level_fourth_second()
            # level 4 path
        elif x == 2:
            print('quiting...')
            # quit function


######## level 3 second encounter ########
def level_three_second():
    """First route player can take"""
    print(f"""{monster.forest_troll.description}
it's a{monster.forest_troll.name}!\n""")
    dice_roll(player.player, monster.forest_troll)

    if player.player.hp >= 0:
        print(f"""
You survived the encountor!
And finds 2 more paths at the far end...\n
Now you stand before a choice again will you go [left] or [right]?\n""")
    path = ['Left', 'Right', 'Quit']
    path_menu = TerminalMenu(path)

    while True:
        x = path_menu.show()
        if x == 0:
            print('\nYou choose the left path and start walking')
            level_fourth_first()
            # level 4 path
        elif x == 1:
            print('\nYou choose the right path and start walking')
            level_fourth_second()
            # level 4 path
        elif x == 2:
            print('quiting...')
            # quit function


######## level 3 third encounter ########
def level_three_third():
    """First route player can take"""
    print(f"""{monster.cave_troll.description}
    it's a{monster.cave_troll.name}!\n""")
    dice_roll(player.player, monster.cave_troll)

    if player.player.hp >= 0:
        print(f"""
You survived the encountor!
And finds 2 more paths at the far end...\n
Now you stand before a choice again will you go [left] or [right]?\n""")
    path = ['Left', 'Right', 'Quit']
    path_menu = TerminalMenu(path)

    while True:
        x = path_menu.show()
        if x == 0:
            print('\nYou choose the left path and start walking')
            level_fourth_second()
            # level 4 path
        elif x == 1:
            print('\nYou choose the right path and start walking')
            level_fourth_third()
            # level 4 path
        elif x == 2:
            print('quiting...')
            # quit function


######## level 3 fourth encounter ########
def level_three_fourth():
    """First route player can take"""
    print(f"{monster.basilisk.description}it's a{monster.basilisk.name}!\n")
    dice_roll(player.player, monster.basilisk)

    if player.player.hp >= 0:
        print(f"""
You survived the encountor!
And finds 2 more paths at the far end...\n
Now you stand before a choice again will you go [left] or [right]?\n""")
    path = ['Left', 'Right', 'Quit']
    path_menu = TerminalMenu(path)

    while True:
        x = path_menu.show()
        if x == 0:
            print('\nYou choose the left path and start walking')
            level_fourth_second()
            # level 4 path
        elif x == 1:
            print('\nYou choose the right path and start walking')
            level_fourth_third()
            # level 4 path
        elif x == 2:
            print('quiting...')
            # quit function


######## level 4 first encounter ########
def level_fourth_first():
    """First route player can take"""
    print(f"{monster.basilisk.description}it's a{monster.basilisk.name}!\n")
    dice_roll(player.player, monster.basilisk)

    if player.player.hp >= 0:
        print(f"""
You survived the encountor!
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
            print('quiting...')
            # quit function


######## level 4 second encounter ########
def level_fourth_second():
    """First route player can take"""
    print(f"{monster.basilisk.description}it's a{monster.basilisk.name}!\n")
    dice_roll(player.player, monster.basilisk)

    if player.player.hp >= 0:
        print(f"""
You survived the encountor!
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
            print('quiting...')
            # quit function


######## level 4 third encounter ########
def level_fourth_third():
    """First route player can take"""
    print(f"{monster.basilisk.description}it's a{monster.basilisk.name}!\n")
    dice_roll(player.player, monster.basilisk)

    if player.player.hp >= 0:
        print(f"""
You survived the encountor!
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
            print('quiting...')
            # quit function


######## level 5 encounter ########
def level_five_first():
    """First route player can take"""
    print(f"""{monster.black_dragon.description}
it's a{monster.black_dragon.name}!!!\n""")
    dice_roll(player.player, monster.black_dragon)

    if player.player.hp >= 0:
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
            print('quiting...')
            # quit function
