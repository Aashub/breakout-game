from turtle import Turtle
MOVE_DISTANCE = 50

class Paddle:

    def __init__(self):

        self.paddle = Turtle("square")
        self.create_paddle()

        self.paddle_xcor = self.paddle.xcor()


    def create_paddle(self):
        """this method will set paddle details and also create a paddle"""

        self.paddle.penup()
        self.paddle.shapesize(stretch_wid=6, stretch_len=1)
        self.paddle.color("white")
        self.paddle.setheading(90)
        self.paddle.goto(0,-325)


    def paddle_right_movement(self):
        """method for moving paddle to right side"""

        if self.paddle.xcor() > 360:
            return

        self.paddle.setx(self.paddle.xcor() + MOVE_DISTANCE)



    def paddle_left_movement(self):
        """method for moving paddle to left side"""

        if self.paddle.xcor() < -360:
            return

        self.paddle.setx(self.paddle.xcor() - MOVE_DISTANCE)

