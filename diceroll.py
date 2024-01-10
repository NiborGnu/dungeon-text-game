# Dice Roll function 

import random



def dice_roll(player, monster):
    """ Battle the monster by rolling the dice. """
    print(f"""Lets [roll] the dice and kill the {monster.name},
or to end the game type [quit]""")

    while True:
        roll_quit = input('>').lower()
        if roll_quit == 'roll':
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
                print(f'The {monster.name} still moves lets [roll] again!')
            elif monster.hp <= 1 or player.hp <= 1:
                break
        elif roll_quit == 'quit':
            print(f"""
Sad to see you go warrior! Come back and fight the dungeon again one day!""")
            # Add a way to restart game here!
        else:
            print(f"""
Invalid input!\nType [roll] to attack or [quit] to end game""")

    if monster.hp <= 0:
        print(f"\nThe {monster.name} is dead!")
    elif player.hp <= 0:
        print(f"{player.name} has been defeated!")