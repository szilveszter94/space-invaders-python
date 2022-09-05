from turtle import Turtle


# read the high score
def high_score_reader():
    with open(file='highscore.txt') as file:
        return int(file.read())


# set scoreboard class
class Scoreboard(Turtle):
    def __init__(self, highscore):
        # config the scoreboard
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(-360, 250)
        self.write(f'SCORE: {self.score}', font=('consolas', 14, 'bold'))
        self.goto(-360, 230)
        self.write(f'HIGHSCORE: {highscore}', font=('consolas', 14, 'bold'))

    # manage the scoreboard changes
    def update_scoreboard(self, highscore):
        self.clear()
        self.score += 1
        self.goto(-360, 250)
        self.write(f'SCORE: {self.score}', font=('consolas', 14, 'bold'))
        self.goto(-360, 230)
        self.write(f'HIGHSCORE: {highscore}', font=('consolas', 14, 'bold'))
