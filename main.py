# all required classes

from turtle import Screen
from paddle import Paddle
from scoreboard import Score
from bricks import Bricks
from ball import Ball
import random

BALL_HEADING = random.randint(210, 330)
BALL_WIDTH, BALL_HEIGHT = 1, 1
BALL_DIAMETER = (BALL_WIDTH * 10) + (BALL_HEIGHT * 10)
broke_brick_dict = {}


color_score_dict = {

    "yellow": 200, "aqua": 400, "green": 600, "orange": 800, "red": 1000

}


# create_screen
screen_object = Screen()
screen_object.tracer(0)




# create paddle
paddle_object = Paddle()


# create scoreboard
score = Score()
score.create_score_board()
score.draw_horizontal_line()
score.user_life_UI()


# create bricks
bricks = Bricks()
bricks.create_bricks()


# create ball
ball_object = Ball(BALL_WIDTH, BALL_HEIGHT)


# create black screen and setup screen size
screen_object.bgcolor("black")
screen_object.setup(width=910, height=700)

#  key binding for left and right paddle movement
screen_object.listen()
screen_object.onkey(fun=paddle_object.paddle_right_movement, key="Right")
screen_object.onkey(fun=paddle_object.paddle_left_movement, key="Left")

score.create_json_file()
screen_object.onkey(fun= lambda: score.restart_game(ball_object, broke_brick_dict) , key = "r")


def update_score(brick_clr):

    for color in color_score_dict:

        if color == brick_clr:
            broke_brick_score = color_score_dict[color]

            score.increase_current_score(broke_brick_score)
        else:
            pass



is_game_on = True

paddle_x_cor = paddle_object.paddle.xcor() + 30
paddle_y_cor = paddle_object.paddle.ycor() + 15
while is_game_on:

    ball_x_cor, ball_y_cor = ball_object.ball_movement(BALL_HEADING)

    if ball_y_cor > 285:
        # if ball y cor is greater than 290 value than this method will get called and give us new heading after colliding with upper wall.

        new_heading = ball_object.on_ball_collision_with_top_wall(BALL_HEADING)

        BALL_HEADING = new_heading
        ball_object.ball_hit = False

    if ball_x_cor >= 440 or ball_x_cor <= -445:
        # if ball x cor is greater than those value than this method will get called and give us new heading after colliding with left & right side of wall.

        new_heading = ball_object.on_ball_collision_with_side_wall(BALL_HEADING)
        BALL_HEADING = new_heading
        ball_object.ball_hit = False

    if ball_y_cor <= paddle_y_cor and ball_object.ball.distance(paddle_object.paddle) < 50 and  ball_object.ball_hit == False:
        # if ball y_cor is greater than paddle y_cor and ball & paddle distance is less than 40 and ball not hit than this method will give us new direction

        new_heading = ball_object.on_ball_collision_with_paddle()
        BALL_HEADING = new_heading
        ball_object.ball_hit = True

    elif ball_y_cor <= paddle_y_cor:
        score.decrease_user_life(ball_object.ball)
        new_random_heading  = random.randint(210, 330)
        BALL_HEADING = new_random_heading


    # this for loop will check that which brick is closest to the ball and as per that break that brick
    for index, brick in enumerate(bricks.brick_list):

        # this method checks each brick and the brick which is closest to the ball it gives us on which side of brick wall it was the closest
        collision_result = bricks.check_brick_collision(ball_x_cor, ball_y_cor, brick, BALL_DIAMETER)

        if collision_result is None:
            continue
        brick_collision_side, brick_color = collision_result

        # if upper and lower side of that brick is closest to the ball than this condition breaks the brick and change the ball direction
        if brick_collision_side == "lower_wall_collide" or brick_collision_side == "upper_wall_collide":

            x_cor, ycor = brick.position()
            broke_brick_dict[brick] = x_cor, ycor

            new_heading = ball_object.on_ball_collision_with_top_bottom_wall_of_bricks(BALL_HEADING)

            brick.goto(460, 400)
            BALL_HEADING = new_heading
            ball_object.ball_hit = False
            update_score(brick_color)
            break

        # if left and right side of that brick is closest to the ball than this condition breaks the brick and change the ball direction
        elif brick_collision_side == "right_wall_collide" or brick_collision_side == "right_wall_collide":

            x_cor, ycor = brick.position()
            broke_brick_dict[brick] = x_cor, ycor

            new_heading = ball_object.on_ball_collision_with_brick_side_wall(BALL_HEADING)
            BALL_HEADING = new_heading
            brick.goto(460, 400)
            ball_object.ball_hit = False
            update_score(brick_color)
            break

        else:
            pass

    screen_object.update()

screen_object.exitonclick()