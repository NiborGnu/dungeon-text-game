from simple_term_menu import TerminalMenu


# Player
class Player():
    """Player setup"""
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


def get_player_name():
    """Get player name"""
    print('\nHail warrior! State your name: \n')
    while True:
        player_name = input('>')
        if len(player_name) >= 20:
            print(f"""
I don't have room on my paper for that long a name!\n
Do you have a nickname i can call you?(Max 20 characters)\n""")
        elif len(player_name) <= 0:
            print('You do have a name right?')
        elif len(player_name) <= 1:
            print('Really one character? Maybe you have 1 more to use?')
        else:
            return player_name
            


# Difficulty
def difficulty():
    """Choose difficulty between easy, normal or hard"""
    print(f"""
What difficulty do you crave, warrior?\n
Use arrows to navigate Up and Down.
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