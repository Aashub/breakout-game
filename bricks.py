from turtle import Turtle


BRICK_STRETCH_WIDTH = 3
BRICK_STRETCH_LENGTH = 1

class Bricks:

    def __init__(self):

        self.brick_list = []

    def create_bricks(self):
        """this method creates a bricks"""

        # this for loop create bricks assign each brick property and store each brick instance in a list for later use.
        for each_iterate in range(0, 1):
            bricks = Turtle("square")
            bricks.penup()
            bricks.shapesize(stretch_wid=BRICK_STRETCH_WIDTH, stretch_len=BRICK_STRETCH_LENGTH)
            self.brick_height = BRICK_STRETCH_LENGTH * 20
            self.brick_width = BRICK_STRETCH_WIDTH * 20
            bricks.setheading(90)
            self.brick_list.append(bricks)

        # x_cord = -425
        # y_cord = 285
        x_cord = 0
        y_cord = 100

        # this for loop position each brick on a screen at their desired location with equal distance
        for brick in self.brick_list:

            brick.goto(x_cord, y_cord)
            x_cord = x_cord + 65

            if x_cord > 485:
                x_cord = -425
                y_cord = y_cord - 25

        # this for loop assign color to each brick as per the below each brick index division condition
        for index, brick in enumerate(self.brick_list):

            if index / 3 < 10:
                brick.color("red")
            elif index / 3 < 20:
                brick.color("orange")
            elif index / 3 < 30:
                brick.color("green")
            elif index / 3 < 40:
                brick.color("aqua")
            elif index / 3 < 50:
                brick.color("yellow")

    def check_brick_collision(self, ball_x_cord, ball_y_cord, brick, ball_diameter):
        brick_left = brick.xcor() - self.brick_width / 2
        brick_right = brick.xcor() + self.brick_width / 2
        brick_bottom_cord = brick.ycor() - self.brick_height / 2
        brick_top_cord = brick.ycor() + self.brick_height / 2
        ball_radius = ball_diameter / 2

        x_overlap = brick_left - ball_radius <= ball_x_cord <= brick_right + ball_radius

        if (ball_y_cord + ball_radius - 9 >= brick_bottom_cord) and (ball_y_cord < brick_bottom_cord) and x_overlap:
            return "lower_wall_collide"

        elif (ball_y_cord - ball_radius + 10<= brick_top_cord) and (ball_y_cord > brick_top_cord) and x_overlap:
            return "upper_wall_collide"

        return None

