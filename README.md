# Dungeon-text-game

![Responsive Mockup](documentation/all-devices-black.png)

*The link to [Dungeon Text Game](https://dungeon-text-game-8f6df9144d01.herokuapp.com/)* #UPDATE LINK!

Dungeon Text Game is a Python terminal project whose primary purpose is to boost users' moods and provide various experiences.

Secondarily, it may help users to practice decision-making.

Users can quickly learn the rules of the game and type any words according to the provided instructions. In the end, they will receive a story from the choices of the user.

---

## How to play:

  1. Click this *[link](https://dungeon-text-game-8f6df9144d01.herokuapp.com/)* #UPDATE LINK!or copy this text: `https://dungeon-text-game-8f6df9144d01.herokuapp.com/` #UPDATE LINK! and paste it into your browser's address bar.
  2. As the page is loaded, click 'Start Game' or 'How to play'.
  3. Introduce yourself to the program.
  4. Choose the difficulty.
  5. Read the decisions and choose how to move forward.
  6. Play one more time and try to enter different choices to have a different outcome.
  7. As soon as you are sick and tired of the game, choose "Quit" and **send** the link to this program to your friends!

  Link to the game: *https://dungeon-text-game-8f6df9144d01.herokuapp.com/*#UPDATE LINK!

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

  ![loading Program](documentation)

---

## Technologies Used

### Languages:

- [Python 3.8.5](https://www.python.org/downloads/release/python-385/): used to anchor the project and direct all application behavior

- [JavaScript](https://www.javascript.com/): used to provide the start script needed to run the Code Institute mock terminal in the browser

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) used to construct the elements involved in building the mock terminal in the browser

### Frameworks/Libraries, Programmes and Tools:
#### Python modules/packages:

##### Standard library imports:

- [random](https://docs.python.org/3/library/random.html) was used to implement pseudo-random number generation.
- [os](https://docs.python.org/3/library/os.html ) was used to clear the terminal before running the program and some functions.
- [sys](https://docs.python.org/3/library/sys.html) was used to make exit and restart terminal.
##### Third-party imports:

- [Simple Terminal Menu](https://pypi.org/project/simple-term-menu/) was used to implement the menu.

#### Other tools:

- [VSCode](https://code.visualstudio.com/) was used as the main tool to write and edit code.
- [Git](https://git-scm.com/) was used for the version control of the website.
- [GitHub](https://github.com/) was used to host the code of the website.
- [Photoshop](https://www.adobe.com/se/products/photoshop.html) was used to make and resize images for the README file.
- [miro.com](https://www.miro.com/) was used to make a flowchart for the README file.
- [heroku.com](https://heroku.com/) was used to deploy the project.


---

**Solved bugs**

1. Function difficulty did not work
    
    *Solutions:* add "()" after lower in the input line: "input('>').lower"()"".

2. Game did not find player value
    
    *Solutions:* moved "player_name = get_player_name(), player_hp = difficulty(), player = Player(player_name, player_hp)" to main_game function so it was called in the right order.

3. Error in code from diceroll.py
    
    *Solutions:* deleted 4 spaces so "print(f"""Lets [roll] the dice and kill the {monster.name}, or to end the game [Restart]/[Quit]\n""")" was on the right line.


4. Restart function did not work correctly 
code line: "os.execl(sys.executable, os.path.abspath("run.py"), *sys.argv)"
    
    *Solutions:* change the line "os.path.abspath("run.py")" to "sys.executable". Bugg came because simple_term_menu and os/sys inteference with each other somehow. 

---

Took code to "clean screen" from
https://stackoverflow.com/questions/2084508/clear-terminal-in-python

poke answer.