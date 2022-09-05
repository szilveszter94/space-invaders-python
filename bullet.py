from turtle import Turtle

# set constants
SPEED = 20
YCOR = -230


# set bullet class
class Bullet(Turtle):
    # set attributes
    def __init__(self, xcor):
        super().__init__()
        self.xpos = xcor
        self.shape("circle")
        self.shapesize(0.4, 0.4)
        self.penup()
        self.goto(self.xpos, YCOR)
        self.hideturtle()
        self.speed("fastest")

    # set shooting method
    def shoot(self):
        self.showturtle()
        y_cor = self.ycor()
        if y_cor < 280:
            self.setposition(self.xpos, y_cor + SPEED)
        else:
            self.hideturtle()
            self.goto(self.xpos, YCOR)

    # set respawn method
    def respawn_bullet(self):
        self.hideturtle()
        self.goto(self.xpos, YCOR)
