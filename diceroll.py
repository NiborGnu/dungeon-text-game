import random
from time import sleep
from os_sys_function import restart_quit_game
from simple_term_menu import TerminalMenu


def dice_roll(player, monster):
    """Player battle the monster by rolling the dice."""
    print(f"""Lets [roll] the dice and kill the {monster.name},
or to end the game [Restart]/[Quit]\n""")
    
    while True:
        options = ['Roll', 'Restart/Quit']
        roll_quit_menu = TerminalMenu(options)
        x = roll_quit_menu.show()

        if x == 0:
            player_damage = random.randint(1, 6)
            monster_damage = random.randint(1, 6)

            # Deduct damage from monster's and player's health points
            monster.hp -= player_damage
            player.hp -= monster_damage

            # Make sure HP don't go below zero
            monster.hp = max(0, monster.hp)
            player.hp = max(0, player.hp)

            print(f"""
{player.name} dealt {player_damage} damage.
{monster.name}'s remaining HP: {monster.hp}\n
{monster.name} dealt {monster_damage} damage.
{player.name}'s remaining HP: {player.hp}""")

            if monster.hp >= 1:
                print(f'\nThe {monster.name} still moves lets [roll] again!\n')
            elif monster.hp <= 1 or player.hp <= 1:
                break
        elif x == 1:
            print(f"""
Sad to see you go warrior! Come back and fight the dungeon again one day!""")
            restart_quit_game()

    if monster.hp <= 0:
        print(f"\nThe {monster.name} is dead!")
        sleep(2)
    elif player.hp <= 0:
        print(f"{player.name} has been defeated!")


def dice_roll_2(player, monster):
    """Player battle the monster by rolling the dice."""
    print(f"""Lets [roll] the dice and kill the {monster.name},
or to end the game [Restart]/[Quit]\n""")
    
    while True:
        options = ['Roll', 'Restart/Quit']
        roll_quit_menu = TerminalMenu(options)
        x = roll_quit_menu.show()

        if x == 0:
            player_damage = random.randint(1, 6)*2
            monster_damage = random.randint(1, 6)

            # Deduct damage from monster's and player's health points
            monster.hp -= player_damage
            player.hp -= monster_damage

            # Make sure HP don't go below zero
            monster.hp = max(0, monster.hp)
            player.hp = max(0, player.hp)

            print(f"""
{player.name} dealt {player_damage} damage.
{monster.name}'s remaining HP: {monster.hp}\n
{monster.name} dealt {monster_damage} damage.
{player.name}'s remaining HP: {player.hp}""")

            if monster.hp >= 1:
                print(f'\nThe {monster.name} still moves lets [roll] again!\n')
            elif monster.hp <= 1 or player.hp <= 1:
                break
        elif x == 1:
            print(f"""
Sad to see you go warrior! Come back and fight the dungeon again one day!""")
            restart_quit_game()

    if monster.hp <= 0:
        print(f"\nThe {monster.name} is dead!")
        sleep(2)
    elif player.hp <= 0:
        print(f"{player.name} has been defeated!")