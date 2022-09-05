from turtle import Turtle

# set constants
color = "#7F8487"
SHAPE = "square"


# set wall class
class Wall(Turtle):
    # set attributes
    def __init__(self, xcor, ycor):
        super().__init__()
        self.shape(SHAPE)
        self.shapesize(0.4, 0.4)
        self.color(color)
        self.penup()
        self.speed("fastest")
        self.goto(xcor, ycor)


# draw the wall
def draw_wall():
    e_list = []
    for y in range(-150, -90, 15):
        for i in range(-300, 301, 15):
            elements = Wall(i, y)
            e_list.append(elements)
    return e_list
