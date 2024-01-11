# Paths true the dungen

import monster
import player
from diceroll import dice_roll
from simple_term_menu import TerminalMenu

def level_zero(player):
    """Dungeon entrence"""
    print(f"""
Hail {player.name} good to meet you!
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
            level_one_first(player)
            # level 2 path
        elif x == 1:
            print('\nYou choose the right path and start walking')
            level_one_second(player)
            # level 2 path
        elif x == 2:
            print('quiting...')
            # quit function

######## level 1 first encounter ########
def level_one_first(player):
    """First route player can take"""
    print(f"{monster.goblin.description}it's a{monster.goblin.name}!\n")
    dice_roll(player, monster.goblin)

    if player.hp >= 0:
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
            level_two_first(player)
            # level 2 path
        elif x == 1:
            print('\nYou choose the right path and start walking')
            level_two_second(player)
            # level 2 path
        elif x == 2:
            print('quiting...')
            # quit function


######## level 1 second encounter ########
def level_one_second(player):
    """First route player can take"""
    print(f"{monster.ork.description}it's an{monster.ork.name}!\n")
    dice_roll(player, monster.ork)

    if player.hp >= 0:
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
            level_two_second(player)
            # level 2 path
        elif x == 1:
            print('\nYou choose the right path and start walking')
            level_two_third(player)
            # level 2 path
        elif x == 2:
            print('quiting...')
            # quit function


######## level 2 first encounter ########
def level_two_first(player):
    """First route player can take"""
    print(f"{monster.ork.description}it's an{monster.ork.name}!\n")
    dice_roll(player, monster.ork)

    if player.hp >= 0:
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
            level_three_first(player)
            # level 3 path
        elif x == 1:
            print('\nYou choose the right path and start walking')
            level_three_second(player)
            # level 3 path
        elif x == 2:
            print('quiting...')
            # quit function


######## level 2 second encounter ########
def level_two_second(player):
    """First route player can take"""
    print(f"{monster.murloc.description}it's a{monster.murloc.name}!\n")
    dice_roll(player, monster.murloc)

    if player.hp >= 0:
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
            level_three_second(player)
            # level 3 path
        elif x == 1:
            print('\nYou choose the right path and start walking')
            level_three_third(player)
            # level 3 path
        elif x == 2:
            print('quiting...')
            # quit function


######## level 2 third encounter ########
def level_two_third(player):
    """First route player can take"""
    print(f"{monster.goblin.description}it's a{monster.goblin.name}!\n")
    dice_roll(player, monster.goblin)

    if player.hp >= 0:
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
            level_three_third(player)
            # level 3 path
        elif x == 1:
            print('\nYou choose the right path and start walking')
            level_three_fourth(player)
            # level 3 path
        elif x == 2:
            print('quiting...')
            # quit function


######## level 3 first encounter ########
def level_three_first(player):
    """First route player can take"""
    print(f"{monster.wyvern.description}it's a{monster.wyvern.name}!\n")
    dice_roll(player, monster.wyvern)

    if player.hp >= 0:
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
            level_fourth_first(player)
            # level 4 path
        elif x == 1:
            print('\nYou choose the right path and start walking')
            level_fourth_second(player)
            # level 4 path
        elif x == 2:
            print('quiting...')
            # quit function


######## level 3 second encounter ########
def level_three_second(player):
    """First route player can take"""
    print(f"""{monster.forest_troll.description}
it's a{monster.forest_troll.name}!\n""")
    dice_roll(player, monster.forest_troll)

    if player.hp >= 0:
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
            level_fourth_first(player)
            # level 4 path
        elif x == 1:
            print('\nYou choose the right path and start walking')
            level_fourth_second(player)
            # level 4 path
        elif x == 2:
            print('quiting...')
            # quit function


######## level 3 third encounter ########
def level_three_third(player):
    """First route player can take"""
    print(f"""{monster.cave_troll.description}
    it's a{monster.cave_troll.name}!\n""")
    dice_roll(player, monster.cave_troll)

    if player.hp >= 0:
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
            level_fourth_second(player)
            # level 4 path
        elif x == 1:
            print('\nYou choose the right path and start walking')
            level_fourth_third(player)
            # level 4 path
        elif x == 2:
            print('quiting...')
            # quit function


######## level 3 fourth encounter ########
def level_three_fourth(player):
    """First route player can take"""
    print(f"{monster.basilisk.description}it's a{monster.basilisk.name}!\n")
    dice_roll(player, monster.basilisk)

    if player.hp >= 0:
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
            level_fourth_second(player)
            # level 4 path
        elif x == 1:
            print('\nYou choose the right path and start walking')
            level_fourth_third(player)
            # level 4 path
        elif x == 2:
            print('quiting...')
            # quit function


######## level 4 first encounter ########
def level_fourth_first(player):
    """First route player can take"""
    print(f"{monster.basilisk.description}it's a{monster.basilisk.name}!\n")
    dice_roll(player, monster.basilisk)

    if player.hp >= 0:
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
def level_fourth_second(player):
    """First route player can take"""
    print(f"{monster.basilisk.description}it's a{monster.basilisk.name}!\n")
    dice_roll(player, monster.basilisk)

    if player.hp >= 0:
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
def level_fourth_third(player):
    """First route player can take"""
    print(f"{monster.basilisk.description}it's a{monster.basilisk.name}!\n")
    dice_roll(player, monster.basilisk)

    if player.hp >= 0:
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
def level_five_first(player):
    """First route player can take"""
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
            print('quiting...')
            # quit function
