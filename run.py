from os_interaction import clear_screen
from simple_term_menu import TerminalMenu
from paths import level_zero
from player import Player, get_player_name, difficulty


def main():
    clear_screen()
    print("""
####################################
#   Step into the Dungeon Game!    #
# As a warrior, seek glory or face #
#  the perilous embrace of death.  #
#    Good luck on your journey!    #
#    See you on the other side!    #
####################################
""")
    main_start_menu()


def main_start_menu():
    """Displays the main menu and handles user choices."""
    options = ['Start Game', 'How to play']
    main_menu = TerminalMenu(options)
    x = main_menu.show()

    if x == 0:
        main_game()
    elif x == 1:
        print("""
1. Type the answer when asked a question.
For example: name or number.
2. When you see a menu: Choose an option in menu by using
keys [up] or [down] and [enter] to select that option.
3. Have fun!
""")
        options = ['Start Game']
        go_back = TerminalMenu(options)
        x = go_back.show()

        if x == 0:
            main_game()


def main_game():
    """Main function to start the game."""
    if __name__ == "__main__":
        player_name = get_player_name()
        player_hp = difficulty()
        player = Player(player_name, player_hp)
        level_zero(player)
        main_start_menu()


if __name__ == "__main__":
    main()
