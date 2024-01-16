# Dungeon-text-game

![Responsive Mockup](documentation/all-devices-black.png)

*The link to [Dungeon Text Game](https://dungeon-text-game-8f6df9144d01.herokuapp.com/)*

Dungeon Text Game is a Python terminal project whose primary purpose is to boost users' moods and provide various experiences.

Secondarily, it may help users to practice decision-making.

Users can quickly learn the rules of the game and type any words according to the provided instructions. In the end, they will receive a story from the choices of the player.

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