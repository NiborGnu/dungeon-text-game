import time
import random
from simple_term_menu import TerminalMenu
from os_interaction import clear_screen, restart_quit_game, end_of_game
from diceroll import dice_roll, dice_roll_2
import monster


def survived_encounter():
    """Text to show after ended survived encounter"""
    print("""
############################################
# You survived the encounter!              #
# And finds 2 more paths at the far end... #
############################################

Now you stand before a choice again will you go [left] or [right]?
""")


def level_zero(player):
    """Initiates dungeon entry, welcomes player, and prompts path choice."""
    clear_screen()
    print(f"""
##############################################
# Hail {player.name}! Good to meet you!
# You are cleared to move into the dungeon!  #
# You enter the opening, and before you      #
# are 2 paths leading forth! Left and right  #
##############################################
##############################################
# Which way will you go? [Left] or [Right]   #
# Or will you [Restart/Quit] before entering!#
##############################################
""")

    path = ['Left', 'Right', 'Restart/Quit']
    path_menu = TerminalMenu(path)

    while True:
        x = path_menu.show()
        if x == 0:
            clear_screen()
            print('\nYou choose the left path and start walking')
            level_one_first(player)
        elif x == 1:
            clear_screen()
            print('\nYou choose the right path and start walking')
            level_one_second(player)
        elif x == 2:
            restart_quit_game()


def encounter_and_choose_path(player, current_monster, next_level_functions):
    """Handles monster encounter and prompts for next path choice."""
    print(f"{current_monster.description}\n")
    dice_roll(player, current_monster)

    if player.hp >= 0:
        survived_encounter()

    path_options = ['Left', 'Right', 'Restart/Quit']
    path_menu = TerminalMenu(path_options)

    while True:
        x = path_menu.show()
        if x == 0:
            clear_screen()
            print('\nYou choose the left path and start walking')
            next_level_functions[0](player)
        elif x == 1:
            clear_screen()
            print('\nYou choose the right path and start walking')
            next_level_functions[1](player)
        elif x == 2:
            restart_quit_game()


def level_one_first(player):
    """Encounter goblin, fight and survive. Choose new path"""
    encounter_and_choose_path(
        player, monster.goblin, [level_two_first, level_two_second]
    )


def level_one_second(player):
    """Encounter orc, fight and survive. Choose new path"""
    encounter_and_choose_path(
        player, monster.orc, [level_two_second, level_two_third]
    )


def level_two_first(player):
    """Encounter orc, fight and survive. Choose new path"""
    encounter_and_choose_path(
        player, monster.orc, [level_three_first, level_three_second]
    )


def level_two_second(player):
    """Encounter murloc, fight and survive. Choose new path"""
    encounter_and_choose_path(
        player, monster.murloc, [level_three_second, level_three_third]
    )


def level_two_third(player):
    """Encounter goblin, fight and survive. Choose new path"""
    encounter_and_choose_path(
        player, monster.goblin, [level_three_third, level_three_fourth]
    )


def level_three_first(player):
    """Encounter wyvern, fight and survive. Choose new path"""
    encounter_and_choose_path(
        player, monster.wyvern, [level_fourth_first, level_fourth_second]
    )


def level_three_second(player):
    """Encounter forest troll, fight and survive. Choose new path"""
    encounter_and_choose_path(
        player, monster.forest_troll, [level_fourth_first, level_fourth_second]
    )


def level_three_third(player):
    """Encounter cave troll, fight and survive. Choose new path"""
    encounter_and_choose_path(
        player, monster.cave_troll, [level_fourth_second, level_fourth_third]
    )


def level_three_fourth(player):
    """Encounter basilisk, fight and survive. Choose new path"""
    encounter_and_choose_path(
        player, monster.basilisk, [level_fourth_second, level_fourth_third]
    )


def level_fourth_first(player):
    """Encounter wizard in library with a tempting offer."""
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
    # To long text so showing 1 line at a time with 1 sec between lines
    for text in texts:
        print(text)
        time.sleep(1)

    path = ['Take the offer', "Don't take the offer", 'Restart/Quit']
    path_menu = TerminalMenu(path)

    while True:
        x = path_menu.show()
        if x == 0:
            accept_offer_text = [
                "##################################################",
                "# Upon accepting the offer, the wizard instructs #",
                "# you to step into a magic circle. As he utters  #",
                "# the incantation, the last image burned into    #",
                "# your memory is the wizard's sinister smile.    #",
                "# You've fallen victim to a cunning trick!       #",
                "##################################################"
                "Processing ..."
            ]
            # To long text so showing 1 line at a time with 1 sec between lines
            for line in accept_offer_text:
                print(line)
                time.sleep(1)
            time.sleep(5)
            level_zero(player)

        elif x == 1:
            deny_offer_text = [
                "#################################################",
                "# Politely declining the wizard's offer, you    #",
                "# express gratitude for the opportunity but     #",
                "# choose to continue your journey without the   #",
                "# aid of magical transport. The wizard nods     #",
                "# understandingly, his eyes reflecting both     #",
                "# wisdom and curiosity. As you turn away, the   #",
                "# wooden floor beneath your feet creaks softly, #",
                "# resuming its transformation into the rough    #",
                "# and uneven terrain of the dungeon.            #",
                "# You leave the library behind, the warm glow   #",
                "# of knowledge fading as you venture further    #",
                "# into the unknown depths of the dungeon.       #",
                "#################################################"
            ]
            # To long text so showing 1 line at a time with 1 sec between lines
            for line in deny_offer_text:
                print(line)
                time.sleep(1)
            treasure(player)

        elif x == 2:
            restart_quit_game()


def level_fourth_second(player):
    """Encounter a mathematical challenge from a dryad in a serene clearing."""
    print("""
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

    # Generate question with +, - or *
    if operation == '+':
        correct_answer = num1 + num2
        question = f"What is the sum of {num1} + {num2}?\n>"
    elif operation == '-':
        # Make sure the bigger number is presented first
        num1, num2 = max(num1, num2), min(num1, num2)
        correct_answer = num1 - num2
        question = f"What is the sum of {num1} - {num2}?\n>"
    elif operation == '*':
        correct_answer = num1 * num2
        question = f"What is the sum of {num3} * {num4}?\n>"

    while True:
        check = input(question)

        # Handle restart and quit options
        if check.lower() == 'restart' or check.lower() == 'quit':
            restart_quit_game()

        try:
            answer = int(check)
        except ValueError:
            print('Invalid input. Please enter a number.')
            continue

        # Check the correctness of the answer
        if answer == correct_answer:
            print("""
##############################################################
# In recognition of your astute identification of the answer,#
# a mystical boon awaits you. Behold the bestowed gift:      #
# the enchantment of double damage, destined to surge        #
# through your weapon in the imminent battles ahead.         #
# Go forth, valiant warrior, wield this newfound power       #
# with valor, and let the resonance of victory echo          #
# in the realms of the dugneon!                              #
##############################################################
Processing ...""")
            time.sleep(10)
            level_five_second(player)
        elif answer != correct_answer:
            print("""
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
Processing ...""")
            time.sleep(10)
            level_five_first(player)


def level_fourth_third(player):
    """Encounter a Sleeping Beauty under a magical slumber;
face a consequential choice."""
    texts = [
        "######################################################",
        "# Upon an ornate bed adorned with silken drapes      #",
        "# and glistening jewels, lies a Sleeping Beauty,     #",
        "# countenance serene in the undisturbed embrace      #",
        "# of a magical slumber. The soft glow of moonlight   #",
        "# bathes the room, casting an ethereal aura.         #",
        "# A delicate sign placed near the bed bears          #",
        "# testament to a haunting curse, telling of a deep   #",
        "# enchantment that has plunged the beauty into an    #",
        "# unending sleep. The words reveal the only          #",
        "# antidote to this magical malady—a kiss of true     #",
        "# love, a remedy whispered through the ages.         #",
        "# The inscription delicately details the nature of   #",
        "# the curse, describing the beauty's repose as a     #",
        "# consequence of a malevolent spell woven by dark    #",
        "# forces. Only the touch of an authentic love, pure  #",
        "# and genuine, possesses the power to break the      #",
        "# spell, rousing the sleeping maiden from bewitched  #",
        "# dreams. As the moonlight weaves through the        #",
        "# tapestries, the room remains suspended in a        #",
        "# timeless hush, waiting for the fateful moment when #",
        "# a lover's kiss shall dispel the enchantment and    #",
        "# awaken Sleeping Beauty to a world long yearned for.#",
        "######################################################"
    ]
    # To long text so showing 1 line at a time with 1 sec between lines
    for text in texts:
        print(text)
        time.sleep(1)

    path = ['Walk away', 'Kiss the Beauty', 'Restart/Quit']
    path_menu = TerminalMenu(path)

    while True:
        x = path_menu.show()
        if x == 0:
            walk_away_text = [
                "#####################################################",
                "# As you walk away, a sudden chill crawls up your   #",
                "# spine. Glancing back, you witness a horrifying    #",
                "# transformation the once beautiful Sleeping Beauty #",
                "# contorts into a slimy, poisonous creature. The    #",
                "# room echoes with malevolent hisses as the entity  #",
                "# writhes in the throes of its monstrous form. A    #",
                "# cautionary shiver runs down your spine, serving   #",
                "# as a chilling reminder of the dangers concealed   #",
                "# in the dungeon's depths.                          #",
                "#####################################################"
            ]
            # To long text so showing 1 line at a time with 1 sec between lines
            for line in walk_away_text:
                print(line)
                time.sleep(1)
            time.sleep(5)
            treasure(player)
        elif x == 1:
            kiss_beauty_text = [
                "#####################################################",
                "# As your lips meet those of Sleeping Beauty,       #",
                "# a sudden tremorreverberates through the room,     #",
                "# and the world tilts on its axis. A disorienting   #",
                "# daze envelops you as you collapse to the floor,   #",
                "# the taste of poison lingering on your lips.       #",
                "# The air thickens with malevolence, and mocking    #",
                "# laughter echoes in your ears, an insidious taunt  #",
                "# from an unseen malefactor. The room blurs as the  #",
                "# poison courses through your veins, and the        #",
                "# once promised victory transforms into a bitter    #",
                "# defeat.In the fading consciousness, you discern   #",
                "# the haunting echo of the evil laughter, a cruel   #",
                "# reminder of a trap intricately laid and           #",
                "# effortlessly sprung. As darkness claims your      #",
                "# senses, the last vestiges of awareness are        #",
                "# consumed by the chilling realization that, in     #",
                "# the game of fate, you were but a pawn manipulated #",
                "# by a malevolent force—a force that reveled in     #",
                "# your vulnerability and relished the simplicity    #",
                "# with which it tricked your noble intentions.      #",
                "#####################################################"
            ]
            # To long text so showing 1 line at a time with 1 sec between lines
            for line in kiss_beauty_text:
                print(line)
                time.sleep(1)
            time.sleep(5)
            end_of_game()

        elif x == 2:
            restart_quit_game()


def level_five_first(player):
    """Face a Black Dragon in a thrilling boss fight."""
    print(f"""{monster.black_dragon.description}\n""")
    dice_roll(player, monster.black_dragon)

    if player.hp >= 0:
        print("""
###############################
# You survived the encounter! #
###############################""")

    path = ['Continue', 'Restart/Quit']
    path_menu = TerminalMenu(path)

    while True:
        x = path_menu.show()
        if x == 0:
            print('Walk away and see a opening and continu that way')
            treasure(player)
        elif x == 1:
            restart_quit_game()


def level_five_second(player):
    """Face a Black Dragon in a thrilling boss fight. With dubbel attack"""
    print(f"""{monster.black_dragon.description}\n""")
    dice_roll_2(player, monster.black_dragon)

    if player.hp >= 0:
        print("""
###############################
# You survived the encounter! #
###############################""")

    path = ['Continue', 'Restart/Quit']
    path_menu = TerminalMenu(path)

    while True:
        x = path_menu.show()
        if x == 0:
            print('Walk away and see a opening and continu that way')
            treasure(player)
        elif x == 1:
            restart_quit_game()


def treasure(player):
    """Discover an abundance of treasures and face the
ultimate decision at the end of the game."""
    texts = [
        "###################################################",
        "# You follow the path, and just as doubt creeps   #",
        "# in about continuing forward, a breathtaking     #",
        "# sight unfolds before you a treasure so abundant #",
        "# it seems surreal. The glittering riches and     #",
        "# artifacts strewn across the chamber leave you   #",
        "# in awe, making you question whether such a      #",
        "# discovery is even possible.                     #",
        "#                                                 #",
        "# As you marvel at the bounty, you notice an      #",
        "# ancient portal tucked away in the corner.       #",
        "# Its shimmering energy suggests a way out of     #",
        "# the dungeon, providing a tempting opportunity   #",
        "# to secure your newfound treasures and escape    #",
        "# the perilous depths. The decision now lies      #",
        "# with you continue exploring the riches, or      #",
        "# step through the portal and exit the dungeon.   #",
        "# The path to your destiny awaits.                #",
        "###################################################",
        "Processing ..."
    ]
    # To long text so showing 1 line at a time with 1 sec between lines
    for text in texts:
        print(text)
        time.sleep(1)
    time.sleep(5)
    print(f"""
**{player.name} you have {player.hp}HP remaining**
#####################################################
#####################################################
###################### THE END ######################
#####################################################
#####################################################
""")
    end_of_game()
