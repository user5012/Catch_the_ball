# Catch the Ball Game

This is a simple Catch the Ball game implemented in Python using the Pygame library. The game involves moving a paddle to catch falling balls to score points. The difficulty of the game can be chosen in a Tkinter window at the beginning.

## How to Play

1. Run the game.
2. A Tkinter window will appear, allowing you to choose the game difficulty (Easy, Normal, or Hard).
3. Once you've selected a difficulty level, the game will start.
4. Move the paddle left and right using your mouse to catch the falling red balls.
5. The score will be displayed on the top left of the game window.
6. If a ball reaches the bottom without being caught, the game is over. You'll have the option to restart or quit.

## Game Controls

- Move the paddle: Use the mouse to control the paddle's horizontal position.

## Code Structure

The game is divided into two parts: the difficulty selection window and the game itself.

### Difficulty Selection (Tkinter Window)

The Tkinter window lets you choose the difficulty level of the game before starting. There are three options: Easy, Normal, and Hard.

### Game

- `WIDTH` and `HEIGHT` define the game window dimensions.
- `PADDLE_WIDTH` and `PADDLE_HEIGHT` determine the dimensions of the paddle.
- `BALL_RADIUS` sets the radius of the falling balls.
- `PADDLE_COLOR`, `BALL_COLOR`, and `BACKGROUND_COLOR` specify the colors used in the game.
- `SCORE` keeps track of your score.
- `QUESTIONMODE` is used to store the chosen difficulty level.
- The game loop is responsible for running the game and updating its elements.

## Dependencies

- Pygame: You need to have the Pygame library installed to run this game (You can download it by running the file).

## How to Run

1. Make sure you have Python 3 is installed
2. Go Download [here](https://github.com/user5012/Catch_the_ball/releases/tag/v1.0) the `Catch.the.ball.setup.msi` installer from realises tab
3. Run the `Catch.the.ball.setup.msi`
4. Nevigate to your `Desktop` and run the `Catch the ball` shortcut

**Enjoy playing Catch the Ball!**
