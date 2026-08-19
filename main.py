# all required classes
from turtle import Screen
from paddle import Paddle


# create_screen
screen_object = Screen()
screen_object.tracer(0)

# create paddle
paddle_object = Paddle()

# create black screen and setup screen size
screen_object.bgcolor("black")
screen_object.setup(width=900, height=700)

#  key binding for left and right paddle movement
screen_object.listen()
screen_object.onkey(fun=paddle_object.paddle_right_movement, key="Right")
screen_object.onkey(fun=paddle_object.paddle_left_movement, key="Left")

is_game_on = True


while is_game_on:
    screen_object.update()


screen_object.exitonclick()