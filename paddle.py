from turtle import Turtle
MOVE_DISTANCE = 30

class Paddle:

    def __init__(self):

        self.paddle_list = []
        self.create_paddle()
        self.paddle = self.paddle_list[0]


        self.paddle_xcor = self.paddle.xcor()


    def create_paddle(self):
        """this method will set paddle details and also create a paddle"""

        for each_iterate in range(0, 1):

            paddle = Turtle("square")
            paddle.penup()
            paddle.shapesize(stretch_wid=1, stretch_len=6)
            paddle.color("white")
            paddle.setheading(180)
            self.paddle_list.append(paddle)

        self.paddle_list[0].goto(0,-325)


    def paddle_right_movement(self):
        """method for moving paddle to right side"""

        if self.paddle.xcor() > 360:
            return


        self.paddle.forward(-MOVE_DISTANCE)



    def paddle_left_movement(self):
        """method for moving paddle to left side"""

        if self.paddle.xcor() < -360:
            return

        self.paddle.forward(MOVE_DISTANCE)

