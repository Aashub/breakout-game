from turtle import Turtle



class Ball:

    def __init__(self, ball_width, ball_height):

        self.ball = Turtle("circle")
        self.ball.setheading(90)
        self.ball.shapesize(ball_width, ball_height)
        self.ball.penup()
        self.ball.color("white")
        self.ball_speed = 0.2
        self.ball_hit = False


    def ball_movement(self, ball_direction):
        """this method will set ball heading & make ball move forward at certain speed and give x y cord of ball"""

        self.ball.setheading(ball_direction)
        self.ball.forward(self.ball_speed)

        x_cor = round(self.ball.xcor(), 2) + 20
        y_cor = round(self.ball.ycor(), 2)

        return x_cor, y_cor

    def on_ball_collision_with_paddle(self, ball_direction):
        """this method will help is change the ball direction after hitting paddle"""

        # here are also increasing ball speed.
        if not self.ball_hit:
            self.ball_speed += 0.05
            self.ball_hit = True


        new_heading = 360 - ball_direction
        return new_heading

    def on_ball_collision_with_side_wall(self, ball_direction):

        new_heading = (180 - ball_direction) % 360
        return new_heading

    def on_ball_collision_with_top_wall(self, ball_direction):

        new_heading = 360 - ball_direction
        return new_heading


    def on_ball_collision_with_bricks(self, ball_direction):

        new_heading = 360 - ball_direction
        return new_heading