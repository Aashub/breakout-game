# Day 87 – Breakout Game with Turtle Graphics

## Project Overview

This is a classic Breakout game built using Python's Turtle graphics library. The game features a paddle controlled by the player, a ball that bounces around the screen, and a grid of colorful bricks that the player needs to break. Each brick has a different color with corresponding point values, and the game tracks the player's current score, highest score (saved in a JSON file), and remaining lives (3 lives total). The ball speed increases with each paddle hit, making the game progressively more challenging. Players can restart the game by pressing 'R' and exit by pressing 'E'. The game ends when all lives are lost or all bricks are destroyed.

The code is designed with a modular structure where each game component - paddle, ball, bricks, and scoreboard - is separated into different files for better organization and maintainability.

## What I Have Learned

* **Turtle Graphics Game Development**: Revised how to build a complete game using Python's Turtle graphics library. Created game objects, handled collisions, and managed game loop logic.

* **Object-Oriented Programming (OOP)**: Built the entire game using classes for each component - Paddle, Ball, Bricks, and Score. Each class handles its own behavior and interactions.

* **Collision Detection**: Implemented collision detection logic for ball with paddle, walls, and bricks. Used distance calculations and bounding box checks to determine when objects intersect.
    
* **Ball Physics and Direction Changes**: Learned how to change ball direction based on what it hits. Used angle calculations to reflect the ball off walls, paddle, and bricks.
 
* **Brick Management**: Created a grid of 100 bricks with different colors (yellow, aqua, green, orange, red) using nested loops. Each row of bricks has a specific color and point value.

* **Score Tracking with JSON**: Used JSON files to store and retrieve the highest score persistently. This allows the game to remember the highest score even after the program is closed.

* **Lives System**:  Implemented a lives system where players start with 3 lives. Each time the ball falls below the paddle, a life is lost and the ball resets to the center.

* **Progressive Difficulty**: Increased ball speed by 0.05 each time the ball hits the paddle, making the game gradually harder as the player progresses.

* **Keyboard Controls**: Used Turtle's onkey() method to capture keyboard inputs for paddle movement (Left/Right arrows), restart (R key), and exit (E key).
 
* **Game State Management**: Managed game states including active gameplay, game over, and restart functionality using global variables and flags.

* **Brick Collision Detection**: Implemented a comprehensive brick collision system that detects which side of the brick the ball hits (top, bottom, left, or right) and reflects the ball accordingly.


## How It Works

### main.py

* **Imports and Setup**: The file imports all required classes (Paddle, Score, Bricks, Ball), sets up the screen with Screen(), configures the game window size and background color, and initializes all game objects. It also defines the color_score_dict which maps brick colors to point values

* **Game Loop**: The main while GAME_ON loop runs continuously, updating the ball position, checking for collisions with walls, paddle, and bricks, and updating the screen. The loop breaks when the player presses 'E' to exit.

* **Wall Collisions**: When the ball hits the top wall, on_ball_collision_with_top_wall() is called which changes the ball's heading to reflect off the top. When the ball hits the left or right walls, on_ball_collision_with_side_wall() is called to change the direction.

* **Paddle Collision**: When the ball reaches the paddle's y-coordinate and the distance between the ball and paddle is less than 50, on_ball_collision_with_paddle() is called. This changes the ball direction to a random angle between 30-150 degrees and increases ball speed by 0.05.

* **Missed Ball**: If the ball falls below the paddle (y-coordinate less than -340), decrease_user_life() is called, a life is lost, and the ball resets to the center with a new random heading.

* **Brick Collision Loop**: For each brick in bricks.brick_list, check_brick_collision() is called to check if the ball is touching that brick. If a collision is detected, the brick is moved off-screen, the ball direction changes based on which side of the brick was hit, and the score is updated using update_score().


### ball.py

* **__init__ Method**: Creates the ball object using Turtle, sets its shape to "circle", color to white, and initializes ball speed to 1.5. The ball_hit flag tracks whether the ball has hit the paddle to prevent multiple speed increases.

* **ball_movement()**: Moves the ball forward at the current speed in the given direction. Returns the current x and y coordinates of the ball for collision detection.

* **on_ball_collision_with_paddle()**: Generates a random angle between 30-150 degrees, increases ball speed by 0.05 (only once per paddle hit), and returns the new heading using (180 - ball_direction) % 360.

* **on_ball_collision_with_side_wall()**: Changes the ball direction if the ball hits the left or right walls by returning the new heading using (180 - ball_direction) % 360.

* **on_ball_collision_with_top_wall()**: Changes the ball direction if the ball hits the top walls by returning the new heading using 360 - ball_direction.

* **on_ball_collision_with_top_bottom_wall_of_bricks()**: Changes the ball direction if the ball hits the top or bottom of a brick using 360 - ball_direction.

* **on_ball_collision_with_brick_side_wall()**: Changes the ball direction if the ball hits the left or right side of a brick using (180 - ball_direction) % 360.


### paddle.py

* **__init__ Method**: Creates the paddle object using Turtle, sets its shape to "square", color to white, and positions it at (0, -325). The paddle is stretched to 6x1 size.

* **create_paddle()**: Sets the paddle's properties including penup, shapesize, color, and initial position.

* **paddle_right_movement()**: Moves the paddle to the right by 50 pixels. Prevents the paddle from moving beyond x-coordinate 360.

* **paddle_left_movement()**: Moves the paddle to the left by 50 pixels. Prevents the paddle from moving beyond x-coordinate -360.

### bricks.py

* **create_bricks()**: Creates 100 bricks using a for loop. Each brick is a Turtle with "square" shape, stretched to 3x1 size. Positions are calculated using x and y coordinates starting from (-300, 285) with spacing of 65 pixels horizontally and 25 pixels vertically. Colors are assigned based on index - first 20 bricks are red, next 20 are orange, next 20 are green, next 20 are aqua, and last 20 are yellow.

* **check_brick_collision()**: Checks if the ball is touching a brick using bounding box collision detection. It calculates the brick's left, right, bottom, and top edges, and checks if the ball overlaps with any of these edges. If a collision is detected, it determines which side of the brick the ball hit by measuring the distance past each edge and returns the collision side along with the brick color.


### scoreboard.py

* **draw_horizontal_line()**: Draws a horizontal line at y-coordinate 300 to separate the game area from the score area.

* **user_life_UI()**: Creates 3 life indicators (circles) positioned at (-40, 325), (-10, 325), and (20, 325) to show remaining lives.

* **decrease_user_life()**: When the ball is missed, changes one life indicator from white to black (loses color). If all lives are lost, displays "Game Over!" and shows restart instructions

* **create_score_board()**: Displays the current score and highest score (loaded from JSON file) at the top of the screen.

* **increase_current_score()**: Adds points to the current score based on the brick color broken and updates the score display.

* **create_restart_instruction_UI()**: Displays "Press R to restart!, or E to Exit Game!" when the game ends.

* **restart_game()**: Resets all game variables, moves the ball to center, restores life indicators, and brings all bricks back to their original positions.

* **create_json_file()**: Creates a data.json file with initial highest score of 0 if the file doesn't exist.

* **check_highest_score()**: Compares the current score with the highest score stored in JSON. If the current score is higher, updates the JSON file with the new highest score.

## Project Highlights

* **Turtle Graphics Game**: Built a complete Breakout game using Python's Turtle library.
* **Object-Oriented Design**: Used classes for each game component - Paddle, Ball, Bricks, and Score.
* **Collision Detection**: Implemented accurate collision detection for ball with paddle, walls, and bricks.
* **Brick Grid System**: Created 100 bricks with 5 different colors and corresponding point values.
* **Progressive Difficulty**: Ball speed increases with each paddle hit, making the game gradually harder
* **Lives System**: Players start with 3 lives, losing one when the ball falls below the paddle.
* **Score Persistence**: Highest score is saved in a JSON file and persists between game sessions.
* **Keyboard Controls**: Left/Right arrows for paddle movement, R for restart, E for exit.
* **Game States**: Handles active gameplay, game over, and restart states.
* **Modular Code Structure**: Separated game components into different files for maintainability.


