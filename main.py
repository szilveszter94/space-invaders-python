import random
import time
from turtle import Screen, Turtle
from spaceship import Spaceship
from wall import draw_wall
from enemy import draw_enemy
from bullet import Bullet
from enemy_bullet import draw_enemy_bullet
from scoreboard import Scoreboard, high_score_reader


# set main function
def main():
    # set screen
    screen = Screen()
    screen.tracer(0)
    screen.bgcolor('#EEEEEE')
    screen.setup(width=800, height=600)

    # set turtle for writing text on the screen
    turtle = Turtle()
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-80, 0)

    # set constants
    enemy_speed = 2
    SCORE = 0
    game = True

    # draw elements, enemy, player, score
    element_list = draw_wall()
    enemy_list = draw_enemy()
    spaceship = Spaceship()
    bullet = Bullet(spaceship.xcor())
    enemy_bullet = draw_enemy_bullet()
    high_score = high_score_reader()
    scoreboard = Scoreboard(high_score)

    # define keyboard keys
    screen.onkeypress(fun=spaceship.move_right, key="d")
    screen.onkeypress(fun=spaceship.move_left, key="a")
    screen.onkey(fun=bullet.shoot, key="space")
    screen.listen()
    # start the game
    while game:
        time.sleep(0.04)
        # respawn enemies
        if len(enemy_list) == 0:
            enemy_list = draw_enemy()
        # move bullet if visible
        if bullet.isvisible():
            if bullet.ycor() == -210:
                bullet.xpos = spaceship.xcor()
            bullet.shoot()
        # move enemy bullets if visible
        for e_bullet in enemy_bullet:
            if e_bullet.isvisible():
                e_bullet.enemy_shoot()
        # manage enemy elements
        for i in element_list:
            # remove enemy, if the player shoots him, and respawn player bullet
            if bullet.distance(i) < 14:
                element_list.remove(i)
                i.hideturtle()
                bullet.respawn_bullet()
            # manage enemy bullets
            for e_bullet in enemy_bullet:
                if e_bullet.distance(i) < 14:
                    try:
                        element_list.remove(i)
                        i.hideturtle()
                        e_bullet.respawn_enemy_bullet()
                    except ValueError:
                        e_bullet.respawn_enemy_bullet()
        # manage enemy bullet when shoots the player
        for e_bullet in enemy_bullet:
            if e_bullet.distance(spaceship) < 30:
                if SCORE > high_score:
                    with open('highscore.txt', 'w') as f:
                        f.write(f'{SCORE}')
                turtle.write("You Lost", font=("Arial", 35, "normal"))
                # show restart after the end of the game
                restart = screen.textinput("Game Over", "\nDo you want to restart ? (y/n)")
                if restart == "y":
                    # restart
                    screen.clearscreen()
                    main()
                else:
                    game = False
        # move enemies
        for i in enemy_list:
            i.forward(enemy_speed)
            if i.xcor() > 272 or i.xcor() < -272:
                # turn back enemies if reach the sides
                enemy_speed *= -1
                # shuffle enemy list
                random_enemies = random.choices(enemy_list, k=len(enemy_list))
                if len(enemy_list) > 5:
                    range_num = 5
                else:
                    range_num = 1
                # spawn 5 or 1 enemy bullet
                for enemy_count in range(range_num):
                    enemy_bullet[enemy_count].xpos = random_enemies[enemy_count].xcor()
                    enemy_bullet[enemy_count].ypos = random_enemies[enemy_count].ycor()
                    enemy_bullet[enemy_count].enemy_shoot()
            # manage player bullet if shoots the enemy
            if bullet.distance(i) < 20:
                enemy_list.remove(i)
                i.hideturtle()
                SCORE += 1
                scoreboard.update_scoreboard(high_score)
                bullet.respawn_bullet()
        screen.update()


# start the game
if __name__ == "__main__":
    main()
