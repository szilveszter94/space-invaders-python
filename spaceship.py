from turtle import Turtle, Screen

# set constants
SPEED = 15
XCOR = 0
YCOR = -250


# set spaceship class
class Spaceship(Turtle):
    # set attributes
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.screen.addshape("spaceship.gif")
        self.shape("spaceship.gif")
        self.shapesize(2, 2)
        self.penup()
        self.speed("fastest")
        self.goto(XCOR, YCOR)

    # set move right method
    def move_right(self):
        x_cor = self.xcor() + SPEED
        if x_cor < 350:
            self.goto(x_cor, self.ycor())

    # set move left method
    def move_left(self):
        x_cor = self.xcor() - SPEED
        if x_cor > -350:
            self.goto(x_cor, self.ycor())
