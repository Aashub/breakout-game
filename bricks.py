from turtle import Turtle


BRICK_STRETCH_WIDTH = 3
BRICK_STRETCH_LENGTH = 1

class Bricks:

    def __init__(self):

        self.brick_list = []

    def create_bricks(self):
        """this method creates a bricks"""

        # this for loop create bricks assign each brick property and store each brick instance in a list for later use.
        for each_iterate in range(0, 100):
            bricks = Turtle("square")
            bricks.penup()
            bricks.shapesize(stretch_wid=BRICK_STRETCH_WIDTH, stretch_len=BRICK_STRETCH_LENGTH)
            self.brick_height = BRICK_STRETCH_LENGTH * 20
            self.brick_width = BRICK_STRETCH_WIDTH * 20
            bricks.setheading(90)
            self.brick_list.append(bricks)

        x_cord = -300
        y_cord = 285


        # this for loop position each brick on a screen at their desired location with equal distance
        for brick in self.brick_list:

            brick.goto(x_cord, y_cord)
            x_cord = x_cord + 65

            if x_cord > 300:
                x_cord = -300
                y_cord = y_cord - 25

        # this for loop assign color to each brick as per the below each brick index division condition
        for index, brick in enumerate(self.brick_list):

            if index  < 20:
                brick.color("red")
            elif index  < 40:
                brick.color("orange")
            elif index  < 60:
                brick.color("green")
            elif index  < 80:
                brick.color("aqua")
            elif index  < 100:
                brick.color("yellow")

    def check_brick_collision(self, ball_x_cord, ball_y_cord, brick, ball_diameter):
        """this method is responsible for checking brick collision in each for side and whatever side of the brick which is close to a ball that brick get removed."""


        brick_color = brick.fillcolor()


        brick_left = brick.xcor() - self.brick_width / 2
        brick_right = brick.xcor() + self.brick_width / 2
        brick_bottom_cord = brick.ycor() - self.brick_height / 2
        brick_top_cord = brick.ycor() + self.brick_height / 2
        ball_radius = ball_diameter / 2

        # is the ball even touching the brick at all? (loose box check)
        touching_horizontally = brick_left - ball_radius <= ball_x_cord <= brick_right + ball_radius
        touching_vertically = brick_bottom_cord - ball_radius <= ball_y_cord <= brick_top_cord + ball_radius

        if not (touching_horizontally and touching_vertically):
            return None  # not touching the brick, nothing to do

        # how far past each edge has the ball poked through?
        # smaller number = ball is closer to that edge = that's the edge it hit
        distance_past_left_edge = (ball_x_cord + ball_radius) - brick_left
        distance_past_right_edge = brick_right - (ball_x_cord - ball_radius)
        distance_past_bottom_edge = (ball_y_cord + ball_radius) - brick_bottom_cord
        distance_past_top_edge = brick_top_cord - (ball_y_cord - ball_radius)

        # whichever edge has the smallest distance is the one the ball actually hit
        closest_edge = min(
            distance_past_left_edge,
            distance_past_right_edge,
            distance_past_bottom_edge,
            distance_past_top_edge
        )

        if closest_edge == distance_past_bottom_edge:
            return "lower_wall_collide", brick_color
        if closest_edge == distance_past_top_edge:
            return "upper_wall_collide", brick_color
        if closest_edge == distance_past_left_edge:
            return "left_wall_collide", brick_color
        if closest_edge == distance_past_right_edge:
            return "right_wall_collide", brick_color

        return None, None


