from paths import level_zero
from player import Player, get_player_name, difficulty
from simple_term_menu import TerminalMenu
from os_sys_function import clear_screen
from sys import exit


def main_game():
    """Main function to start the game."""
    if __name__ == "__main__":
        player_name = get_player_name()
        player_hp = difficulty()
        player = Player(player_name, player_hp)
        level_zero(player)


def main_start_menu():
    """Displays the main menu and handles user choices."""
    clear_screen()
    print(f"""
####################################
#   Step into the Dungeon Game!    #
# As a warrior, seek glory or face #
#  the perilous embrace of death.  #
#    Good luck on your journey!    #
#    See you on the other side!    #
####################################
""")

    options = ['Start Game', 'How to play', 'Quit']
    main_menu = TerminalMenu(options)
    x = main_menu.show()

    if x == 0:
        main_game()
    elif x == 1:
        print(f"""
1. Type when asked to and no menu
2. Choose a option in menu by keys [up] and [down]
3. Have fun.
""")
        options = ['Back to Menu']
        go_back = TerminalMenu(options)
        x = go_back.show()

        if x == 0:
            main_start_menu()

    elif x == 2:
        exit(0)

if __name__ == "__main__":
    main_start_menu()