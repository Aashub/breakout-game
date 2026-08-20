from turtle import Turtle
import random

RANDOM_ANGLE = random.randint(210, 330)

class Ball:

    def __init__(self):

        self.ball = Turtle("circle")
        self.ball.penup()
        self.ball.color("white")

        self.ball_speed = 0.9
        self.ball_hit = False


    def ball_movement(self):
        """this method will set ball heading & make ball move forward at certain speed and give x y cord of ball"""

        self.ball.setheading(RANDOM_ANGLE)
        self.ball.forward(self.ball_speed)

        x_cor = round(self.ball.xcor(), 2) + 20
        y_cor = round(self.ball.ycor(), 2)

        return x_cor, y_cor