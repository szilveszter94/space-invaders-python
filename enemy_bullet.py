from turtle import Turtle

# set constants
SPEED = 15


# set enemy bullet class
class EnemyBullet(Turtle):
    # set attributes
    def __init__(self, xcor, ycor):
        super().__init__()
        self.xpos = xcor
        self.ypos = ycor
        self.shape("circle")
        self.shapesize(0.4, 0.4)
        self.penup()
        self.goto(self.xpos, self.ypos + 50)
        self.hideturtle()
        self.speed("fastest")

    # set shooting method
    def enemy_shoot(self):
        self.showturtle()
        ycor = self.ycor()
        if ycor > -250:
            self.setposition(self.xpos, ycor - SPEED)
        else:
            self.hideturtle()
            self.goto(self.xpos, self.ypos)

    # set respawn method
    def respawn_enemy_bullet(self):
        self.hideturtle()
        self.goto(self.xpos, self.ypos)


# spawn enemy bullets
def draw_enemy_bullet():
    bullet_list = []
    for i in range(5):
        bullets = EnemyBullet(i, 0)
        bullet_list.append(bullets)
    return bullet_list
