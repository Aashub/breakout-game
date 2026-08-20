from turtle import Turtle


class Bricks:

    def __init__(self):

        self.brick_list = []

    def create_bricks(self):
        """this method creates a bricks"""

        # this for loop create bricks assign each brick property and store each brick instance in a list for later use.
        for each_iterate in range(0, 150):
            bricks = Turtle("square")
            bricks.penup()
            bricks.shapesize(stretch_wid=1, stretch_len=3)
            bricks.setheading(180)
            self.brick_list.append(bricks)

        x_cord = -425
        y_cord = 285

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