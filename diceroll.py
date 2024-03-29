import random
from time import sleep
from simple_term_menu import TerminalMenu
from os_interaction import restart_quit_game, end_of_game


def dice_roll(player, monster):
    """Player battles the monster by rolling the dice."""
    print(f"""Lets [roll] the dice and kill the {monster.name},
or to end the game [Restart]/[Quit]
{player.name}'s remaining HP: {player.hp}
""")

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

            if monster.hp <= 0 or player.hp <= 0:
                break
            elif monster.hp >= 1:
                print(f'\nThe {monster.name} still moves lets [roll] again!\n')
        elif x == 1:
            print(f"""
Sad to see you go warrior! Come back and fight the dungeon again one day!""")
            restart_quit_game()

    if player.hp <= 0:
        print(f"\n{player.name} has been defeated!\n")
        end_of_game()
    elif monster.hp <= 0:
        print(f"\nThe {monster.name} is dead!\nProcessing ...")
        sleep(2)


def dice_roll_2(player, monster):
    """Player battles the monster by rolling the dice."""
    print(f"""Lets [roll] the dice and kill the {monster.name},
or to end the game [Restart]/[Quit]\n""")

    while True:
        options = ['Roll', 'Restart/Quit']
        roll_quit_menu = TerminalMenu(options)
        x = roll_quit_menu.show()

        if x == 0:
            player_damage = random.randint(1, 6) * 2
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

            if monster.hp <= 0 or player.hp <= 0:
                break
            elif monster.hp >= 1:
                print(f'\nThe {monster.name} still moves lets [roll] again!\n')
        elif x == 1:
            print(f"""
Sad to see you go warrior! Come back and fight the dungeon again one day!""")
            restart_quit_game()

    if player.hp <= 0:
        print(f"\n{player.name} has been defeated!\n")
        end_of_game()
    elif monster.hp <= 0:
        print(f"\nThe {monster.name} is dead!\nProcessing ...")
        sleep(2)
