# Change "level (number) path" to specific monster

import monster
import time
import random
from os_sys_function import clear_screen, restart_quit_game
from diceroll import dice_roll, dice_roll_2
from simple_term_menu import TerminalMenu


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
            restart_quit_game()


######## level 1 first encounter ########
def level_one_first(player):
    """Level 1 first choice from the left"""
    print(f"{monster.goblin.description}\n")
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
            restart_quit_game()


######## level 1 second encounter ########
def level_one_second(player):
    """Level 1 second choice from the left"""
    print(f"{monster.ork.description}\n")
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
            restart_quit_game()


######## level 2 first encounter ########
def level_two_first(player):
    """Level 2 first choice from the left"""
    print(f"{monster.ork.description}\n")
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
            restart_quit_game()


######## level 2 second encounter ########
def level_two_second(player):
    """Level 2 second choice from the left"""
    print(f"{monster.murloc.description}\n")
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
            restart_quit_game()


######## level 2 third encounter ########
def level_two_third(player):
    """Level 2 third choice from the left"""
    print(f"{monster.goblin.description}\n")
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
            restart_quit_game()


######## level 3 first encounter ########
def level_three_first(player):
    """Level 3 first choice from the left"""
    print(f"{monster.wyvern.description}\n")
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
            restart_quit_game()


######## level 3 second encounter ########
def level_three_second(player):
    """Level 3 second choice from the left"""
    print(f"""{monster.forest_troll.description}\n""")
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
            restart_quit_game()


######## level 3 third encounter ########
def level_three_third(player):
    """Level 3 third choice from the left"""
    print(f"""{monster.cave_troll.description}\n""")
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
            restart_quit_game()


######## level 3 fourth encounter ########
def level_three_fourth(player):
    """Level 3 fourth choice from the left"""
    print(f"{monster.basilisk.description}\n")
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
            restart_quit_game()


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
            time.sleep(10)
            level_zero(player)
        elif x == 1:
            print('\nYou choose the right path and start walking')
            treasure(player)
            
        elif x == 2:
            restart_quit_game()


######## level 4 second encounter ########
def level_fourth_second(player):
    """Level 4 second choice from the left"""
    print(f"""
#####################################################
# The path transitions into a lush greenery, and    #
# a serene clearing unfolds before you. At the      #
# center of the clearing, a graceful dryad appears, #
# her presence emanating tranquility. She gazes at  #
# you with curiosity and speaks in a melodic voice: #
#                                                   #
# Dryad: Greetings, brave adventurer! Before you    #
# lies a treasure beyond measure, guarded not by    #
# force, but by wit. Are you skilled in the art of  #
# mathematics? If so, prove your prowess, and the   #
# riches shall be yours.                            #
#####################################################
If you want to [restart] or [quit] type that.
""")
    
    # Generate random numbers and operation
    num1 = random.randint(1, 400)
    num2 = random.randint(1, 400)
    num3 = random.randint(1, 20)
    num4 = random.randint(1, 20)
    
    # Randomly choose an operation
    operation = random.choice(['+', '-', '*'])
    
    if operation == '+':
        correct_answer = num1 + num2
        question = f"What is the sum of {num1} + {num2}\n>?"
    elif operation == '-':
        correct_answer = num1 - num2
        question = f"What is the sum of {num1} - {num2}\n>?"
    elif operation == '*':
        correct_answer = num1 * num2
        question = f"What is the sum of {num3} * {num4}?\n>"

    while True:
        check = input(question)

        if check.lower == 'restart' or check.lower == 'quit':
            restart_quit_game()

        try:
            answer = int(check)
        except ValueError:
            print('Invalid input. Please enter a number.')
            continue

        if answer == correct_answer:
            print(f"""
You have answerd the dryad correctly and will get a gift 
""")
            level_five_second(player)
        elif answer != correct_answer:
            print(f"""
#####################################################
# You chose a different path, missing out on the    #
# dryad's mysterious gift. The allure of the        #
# unknown remains as you proceed deeper into the    #
# dungeon, embracing new challenges and adventures. #
#                                                   #
# The Dryad is gone and the path is emty once more. #
# All evidence it was there gone with it.           #
# You shake your head and continue.                 #
#####################################################
""")
            level_five_first(player)


######## level 4 third encounter ########
def level_fourth_third(player):
    """Level 4 third choice from the left"""
    print(f"{monster.basilisk.description}\n")
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
            treasure(player)
        elif x == 2:
            restart_quit_game()


######## level 5 encounter ########
def level_five_first(player):
    """Level 5 'Boss fight'"""
    print(f"""{monster.black_dragon.description}\n""")
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
            clear_screen()
            print(f"""
#####################################
# Thank you for playing my dungeon! #
#  See you on your next adventure!  #
#####################################
""")
            time.sleep(10)
            break


######## level 5 encounter ########
def level_five_second(player):
    """Level 5 'Boss fight' with multiplyed attack"""
    print(f"""{monster.black_dragon.description}
it's a {monster.black_dragon.name}!!!\n""")
    dice_roll_2(player, monster.black_dragon)

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
            clear_screen()
            print(f"""
#####################################
# Thank you for playing my dungeon! #
#  See you on your next adventure!  #
#####################################
""")
            time.sleep(10)
            break


def treasure(player):
    print(f"""
#####################################################
# You follow the path, and just as doubt creeps     #
# in about continuing forward, a breathtaking       #
# sight unfolds before you – a treasure so abundant #
# it seems surreal. The glittering riches and       #
# artifacts strewn across the chamber leave you     #
# in awe, making you question whether such a        #
# discovery is even possible.                       #
#                                                   #
# As you marvel at the bounty, you notice an        #
# ancient portal tucked away in the corner.         #
# Its shimmering energy suggests a way out of       #
# the dungeon, providing a tempting opportunity     #
# to secure your newfound treasures and escape      #
# the perilous depths. The decision now lies        #
# with you – continue exploring the riches, or      #
# step through the portal and exit the dungeon.     #
# The path to your destiny awaits.                  #
#####################################################
""")
    time.sleep(30)
    clear_screen()
    print(f"""
#####################################################
#####################################################
###################### THE END ######################
#####################################################
#####################################################
""")    
    time.sleep(10)
    return
