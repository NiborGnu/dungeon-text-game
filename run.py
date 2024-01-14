import paths
from player import Player, get_player_name, difficulty
from simple_term_menu import TerminalMenu
from os_sys_function import clear_screen, restart_quit_game


def main_game():
    """Main function to start the game."""
    player_name = get_player_name()
    player_hp = difficulty()
    player = Player(player_name, player_hp)
    paths.level_zero(player)


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

    options = ['Start Game', 'How to play', 'Restart/Quit']
    main_menu = TerminalMenu(options)
    x = main_menu.show()

    if x == 0:
        main_game()
    elif x == 1:
        print(f"""
1. Type you name. 2 - 20 charcters
2. Choose a option in menu by keys [up] and [down]
3. Have fun.
""")
    elif x == 2:
        restart_quit_game()


main_start_menu()