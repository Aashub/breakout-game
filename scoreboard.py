import json
from turtle import  Turtle
import os

file_name = "data.json"
TOTAL_LEFT = 2
CURRENT_SCORE = 0
LEVEL = 0
HORIZONTAL_LINE_AXIS = (-460,300)

class Score:

    def __init__(self):

        self.horizontal_line = Turtle("square")

        self.pen = Turtle()
        self.score = Turtle()
        self.restart = Turtle()
        self.game_over = Turtle()

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
        """this method create user left life UI on the screen"""

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
        """this method decrease user life if user misses the ball to be touched with paddle"""

        global TOTAL_LEFT

        for  index, life_lost in enumerate(reversed(self.life_list_list)):

            if index == TOTAL_LEFT:
                life_lost.fillcolor("black")
                TOTAL_LEFT -= 1
                ball.goto(0, 0)
                break

        if TOTAL_LEFT == -1:

            self.game_over.color("white")
            self.game_over.penup()
            self.game_over.goto(0,0)
            self.game_over.write("Game Over!", align= "center", font = ("Arial", 24, "bold"))
            self.game_over.hideturtle()
            ball.hideturtle()
            self.create_restart_instruction_UI()


    def create_score_board(self):
        """this method create score card in the UI."""

        self.pen.color("white")
        self.pen.penup()
        self.pen.goto(250, 315)

        if not os.path.exists(file_name):
            highest_score = 0
        else:
            with open(file_name, "r") as file:
                data = json.load(file)
            highest_score = data["highest_score"]

        self.pen.write(f"Highest Score: {highest_score}", align="center", font=("Arial", 13, "bold"))
        self.pen.hideturtle()

        self.pen.color("white")
        self.pen.penup()
        self.pen.goto(-275, 315)
        self.pen.write(f"Current Score: {CURRENT_SCORE}", align="center", font=("Arial", 13, "bold"))
        self.pen.hideturtle()

    def increase_current_score(self, score_value):

        global CURRENT_SCORE
        CURRENT_SCORE += score_value

        self.pen.clear()
        self.create_score_board()


    def create_restart_instruction_UI(self):

        self.restart.color("white")
        self.restart.penup()
        self.restart.goto(0, -30)
        self.restart.write(f"Press R to restart!, or E to Exit Game!", align="center", font=("Arial", 16, "bold"))
        self.restart.hideturtle()

    def restart_game(self, ball_obj, broke_brick_dict):
        """Initialize or reset all game variables and characters here."""

        global TOTAL_LEFT
        TOTAL_LEFT = 2

        self.game_over.clear()
        self.restart.clear()

        ball_obj.ball.goto(0, 0)
        ball_obj.ball.showturtle()
        ball_obj.ball_speed = 1.5


        for brick, (xcor, ycor) in broke_brick_dict.items():
            brick.goto(xcor, ycor)

        for life in self.life_list_list:
            life.fillcolor("white")

        self.check_highest_score()


    def create_json_file(self):


        if not os.path.exists(file_name):

            data = {"highest_score": 0}
            with open(file_name, "w") as file:
                json.dump(data, file)


    def check_highest_score(self):

        global CURRENT_SCORE
        with open(file_name, "r") as file:
            data = json.load(file)

        previous_highest_score = data["highest_score"]

        if CURRENT_SCORE > previous_highest_score:

            data.update({'highest_score': CURRENT_SCORE})
            with open("data.json", "w") as file:
                json.dump(data, file)

            CURRENT_SCORE = 0
            self.pen.clear()
            self.create_score_board()

        else:
            CURRENT_SCORE = 0