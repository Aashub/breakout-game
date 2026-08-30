from turtle import  Turtle

TOTAL_LEFT = 2

HORIZONTAL_LINE_AXIS = (-460,300)

class Score:

    def __init__(self):

        self.horizontal_line = Turtle("square")


        self.right_score = 0
        self.left_score = 0

        self.life_list_list = []

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


    def user_life_UI(self):



        for ball in range(0, 3):

            self.user_life = Turtle("circle")
            self.user_life.penup()
            self.user_life.shapesize(stretch_wid=1, stretch_len=1, outline=0.5)
            self.user_life.pencolor("white")
            self.user_life.fillcolor("white")
            self.life_list_list.append(self.user_life)

        x_cord = -40
        y_cord = 325

        # this for loop position each user_life on a screen at their desired location with equal distance
        for user_life in self.life_list_list:

            user_life.goto(x_cord, y_cord)
            x_cord = x_cord + 30


    def decrease_user_life(self, ball):

        global TOTAL_LEFT

        for  index, life_lost in enumerate(reversed(self.life_list_list)):

            if index == TOTAL_LEFT:
                self.life_list_list[index].fillcolor("black")
                TOTAL_LEFT -= 1
                ball.goto(0, 0)
                break