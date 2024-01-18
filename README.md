# Dungeon-text-game

![Responsive Mockup](documentation/all-devices-black.png)

*The link to [Dungeon Text Game](https://dungeon-text-game-8f6df9144d01.herokuapp.com/)*

Dungeon Text Game is a Python terminal project whose primary purpose is to boost users' moods and provide various experiences.

Secondarily, it may help users to practice decision-making.

Users can quickly learn the rules of the game and type any words according to the provided instructions. In the end, they will receive a story from the choices of the user.

---

## How to play:

  1. Click this *[link](https://dungeon-text-game-8f6df9144d01.herokuapp.com/)* or copy this text: `https://dungeon-text-game-8f6df9144d01.herokuapp.com/` and paste it into your browser's address bar.
  2. As the page is loaded, click 'Start Game' or 'How to play'.
  3. Introduce yourself to the program.
  4. Choose the difficulty.
  5. Read the decisions and choose how to move forward.
  6. Play one more time and try to enter different choices to have a different outcome.
  7. As soon as you are sick and tired of the game, choose "Quit" and **send** the link to this program to your friends!

  Link to the game: *https://dungeon-text-game-8f6df9144d01.herokuapp.com/*

---
## User Stories
### First Time Visitor Goals:

* As a First Time Visitor, I want to quickly understand the program's primary purpose so that I can start to play.
* As a First Time Visitor, I want to navigate through the program easily so that I can move true the game.
* As a First Time Visitor, I want to relax and have fun playing the game.

### Frequent Visitor Goals:
* As a Frequent User, I want to be able to find different paths true the game.
* As a Frequent User, I want the stories to be a bit different to have new experiences. 

---

## Features
  
  - **When the program is loaded**

  - The user can see a welcoming message which options(menu) to 'start game' or 'How to play'.
  - The user can manipulate the terminal menu with the arrow keys to choose an option and the enter key to confirm the choice.

  ![loading Program](documentation)

  - **When the user chooses 'How to play'.**
  - How to play:
        1. Type the answer when asked a question. For example: name or number.
        2. When you see a menu: Choose an option in menu by using keys [up] or [down] and [enter] to select that option.
        3. Have fun!

        * Start Game(menu) - to start the game.

    ![loading Program](documentation)

  - **When the user chooses 'Start Game'.**
  - Message asking for the name(input) of user in 2- 20 charcters(letters and numbers accepted)

  - **Then the user are asked what difficulty(menu) to play at.**
  - Difficultys menu: 
        * Easy 100 health points.
        * Normal 50 health points.
        * Hard 25 health points.

    ![loading Program](documentation)

  - **Then the user gets welcome text with name and a choocie(menu)**
  - Shows the terminal menu with two options:

    1. Left - Take left choice
    2. Right - Take right choice
    3. Restart/Quit 
      - The program will show the sub-menu with the following options to choose from:
        1. Restart Game. - Restart game.
        2. Quit - End game.
        3. Back - Go back to left/right choice.(Option don't show if dead or reached the last function)

      ![loading Program](documentation)

  - **When the user chose 'left'**
  - Show text explaining the user 'start walking left' then coming to a room/cave and a monster is waiting there. 
  - Show description of the cave and monster
  - A battle chooise [roll] to attack or [Restart/Quit] to end game
    
    1. roll:
      - random number generated between 1-6 and use that number as attack for user and a random 1-6 number for the monster to attack user with.
    2. Restart/Quit
      - The program will show the sub-menu with the following options to choose from:
        1. Restart Game. - Restart game.
        2. Quit - End game.
        3. Back - Go back to left/right choice.(Option don't show if dead)

  ![loading Program](documentation)
  
  - **When the user chose 'Restart Game'**

  - Game restarts at the welcome text.

  ![loading Program](documentation)

  - **When the user chose "Quit"**

  The user will see a goodbye message, and the program will be stopped.

  ![loading Program](documentation/features/goodbye_message.png)

---














---

BUGGS
1. Bugg: Function difficulty did not work
    Solved: "()" after lower in the input line: "input('>').lower"()""

2. Bugg: Game did not find player value
    Solved: moved player_name = get_player_name()
            player_hp = difficulty()
            player = Player(player_name, player_hp)
            out of game function

3. Bugg: Error in code from diceroll.py
    Solved: deleted 4 spaces so "print" was on the right line


---

Took code to "clean screen" from
https://stackoverflow.com/questions/2084508/clear-terminal-in-python

poke answer.