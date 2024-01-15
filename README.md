# Dungeon-text-game

![Responsive Mockup](documentation)

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



























![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Robin Ung,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!









BUGGS
1. Bugg: Function difficulty did not work
    Solved: "()" after lower in the input line: "input('>').lower"()""

2. Bugg: Game did not find player value
    Solved: moved player_name = get_player_name()
            player_hp = difficulty()
            player = Player(player_name, player_hp)
            out of game function

3. Bugg: Error in code from diceroll.py
    Solved: deleted 4 spaces so print was on right line



Took line to clean screen from text from 
https://stackoverflow.com/questions/2084508/clear-terminal-in-python

poke answer.