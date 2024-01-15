from simple_term_menu import TerminalMenu


class Player():
    """Player setup"""

    def __init__(self, name, hp):
        """Initialize a player's name and health points."""
        self.name = name
        self.hp = hp


def get_player_name():
    """Get player name from the user, ensuring it's between 2-20 characters."""
    print('\nHail warrior! State your name:')
    while True:
        player_name = input('>')
        if len(player_name) >= 20:
            print(f"""
I don't have room on my paper for that long a name!\n
Do you have a nickname I can call you? (2 - 20 characters needed)""")
        elif len(player_name) <= 0:
            print('I need a name for my registry')
        elif len(player_name) <= 1:
            print('Really one character? (2 - 20 Characters needed)')
        else:
            return player_name


# Difficulty
def difficulty():
    """User chooses difficulty between easy, normal, or hard."""
    print(f"""
What difficulty do you crave, Warrior?\n
Use arrows to navigate the Menu Up and Down.
Enter to select\n""")
    diff = ['Easy - 100 HP', 'Normal - 50 HP', 'Hard - 25 HP']
    difficulty_menu = TerminalMenu(diff)
    x = difficulty_menu.show()

    if x == 0:
        print('Difficulty Easy - 100HP set\n')
        return 100
    elif x == 1:
        print('Difficulty Normal - 50HP set\n')
        return 50
    elif x == 2:
        print('Difficulty Hard - 25HP set\n')
        return 25
