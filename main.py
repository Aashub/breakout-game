# all required classes
import time
from turtle import Screen
from paddle import Paddle
from scoreboard import Score
from bricks import Bricks
from ball import Ball
import random

# BALL_HEADING = random.randint(210, 330)
BALL_HEADING = 291
BALL_WIDTH, BALL_HEIGHT = 1, 1
BALL_DIAMETER = (BALL_WIDTH * 10) + (BALL_HEIGHT * 10)


# create_screen
screen_object = Screen()
screen_object.tracer(0)

# create paddle
paddle_object = Paddle()

# create bricks
bricks = Bricks()
bricks.create_bricks()

# create scoreboard
score = Score()
score.draw_horizontal_line()

# create ball
ball_object = Ball(BALL_WIDTH, BALL_HEIGHT)


# create black screen and setup screen size
screen_object.bgcolor("black")
screen_object.setup(width=910, height=700)

#  key binding for left and right paddle movement
screen_object.listen()
screen_object.onkey(fun=paddle_object.paddle_right_movement, key="Right")
screen_object.onkey(fun=paddle_object.paddle_left_movement, key="Left")

is_game_on = True

paddle_x_cor = paddle_object.paddle.xcor() + 30
paddle_y_cor = paddle_object.paddle.ycor() + 15
while is_game_on:

    ball_x_cor, ball_y_cor = ball_object.ball_movement(BALL_HEADING)

    if ball_y_cor >= 290:
        # if ball y cor is greater than 290 value than this method will get called and give us new heading after colliding with upper wall.

        new_heading = ball_object.on_ball_collision_with_top_wall(BALL_HEADING)

        BALL_HEADING = new_heading
        ball_object.ball_hit = False

    if ball_x_cor >= 440 or ball_x_cor <= -445:
        # if ball x cor is greater than those value than this method will get called and give us new heading after colliding with left & right side of wall.

        new_heading = ball_object.on_ball_collision_with_side_wall(BALL_HEADING)
        BALL_HEADING = new_heading
        ball_object.ball_hit = False

    if ball_y_cor <= paddle_y_cor and ball_object.ball.distance(paddle_object.paddle) < 40 and  ball_object.ball_hit == False:
        # if ball y_cor is greater than paddle y_cor and ball & paddle distance is less than 40 and ball not hit than this method will give us new direction

        new_heading = ball_object.on_ball_collision_with_paddle(BALL_HEADING)
        BALL_HEADING = new_heading
        ball_object.ball_hit = True


    for index, brick in enumerate(bricks.brick_list):

        brick_collision_side = bricks.check_brick_collision(ball_x_cor, ball_y_cor, brick, BALL_DIAMETER)


        if brick_collision_side == "lower_wall_collide" or brick_collision_side == "upper_wall_collide":

            new_heading = ball_object.on_ball_collision_with_top_bottom_wall_of_bricks(BALL_HEADING)
            BALL_HEADING = new_heading
            ball_object.ball_hit = False
            break

        elif brick_collision_side == "right_wall_collide":

            new_heading = ball_object.on_ball_collision_with_brick_side_wall(BALL_HEADING)
            BALL_HEADING = new_heading


            ball_object.ball_hit = False
            break

        else:
            pass


    screen_object.update()

screen_object.exitonclick()