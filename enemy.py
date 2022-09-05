from turtle import Turtle, Screen


# set enemy class
class Enemy(Turtle):
    # set attributes
    def __init__(self, xcor, ycor):
        super().__init__()
        self.screen = Screen()
        self.screen.addshape("enemy.gif")
        self.shape("enemy.gif")
        self.shapesize(0.4, 0.4)
        self.penup()
        self.speed("fastest")
        self.goto(xcor, ycor)


# spawn enemies
def draw_enemy():
    e_list = []
    for y in range(100, 250, 50):
        for i in range(-200, 201, 50):
            elements = Enemy(i, y)
            e_list.append(elements)
    return e_list
