from turtle import  Turtle



HORIZONTAL_LINE_AXIS = (-460,300)

class Score:

    def __init__(self):

        self.horizontal_line = Turtle("square")

        self.right_score = 0
        self.left_score = 0


    def draw_horizontal_line(self):
        """this method will create horizontal line."""

        self.horizontal_line.shapesize(stretch_wid=0.3, stretch_len=1)
        self.horizontal_line.hideturtle()
        self.horizontal_line.penup()
        self.horizontal_line.color("white")
        self.horizontal_line.setheading(0)
        self.horizontal_line.pensize(width=2)
        self.horizontal_line.goto(HORIZONTAL_LINE_AXIS)
        self.horizontal_line.pendown()
        self.horizontal_line.goto(460, 300)
