# Dice Roll function 

import random
from simple_term_menu import TerminalMenu


def dice_roll(player, monster):
    """Battle the monster by rolling the dice."""
    print(f"""Lets [roll] the dice and kill the {monster.name},
or to end the game [Quit]""")
    options = ['Roll', 'Quit']
    main_menu = TerminalMenu(options)
    x = main_menu.show()

    while True:
        if x == 0:
            player_damage = random.randint(1, 6)
            monster_damage = random.randint(1, 6)

            # Deduct damage from monster's and player's health points
            monster.hp -= player_damage
            player.hp -= monster_damage

            if monster.hp < 0:
                monster.hp = 0
            if player.hp < 0:
                player.hp = 0

            print(f"""
{player.name} dealt {player_damage} damage.
{monster.name}'s remaining HP: {monster.hp}\n
{monster.name} dealt {monster_damage} damage.
{player.name}'s remaining HP: {player.hp}""")

            if monster.hp >= 1:
                print(f'\nThe {monster.name} still moves lets [roll] again!')
            elif monster.hp <= 1 or player.hp <= 1:
                break
        elif x == 1:
            print(f"""
Sad to see you go warrior! Come back and fight the dungeon again one day!""")
            # Quit function needed
            break

    if monster.hp <= 0:
        print(f"\nThe {monster.name} is dead!")
    elif player.hp <= 0:
        print(f"{player.name} has been defeated!")