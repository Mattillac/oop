import math
import turtle
import random
import winsound

# screnene
scrn = turtle.Screen()
scrn.bgcolor("black")
scrn.title("RANDOM SHOOTER GO")
scrn.bgpic(r"C:\Users\Matthew\PycharmProjects\PythonProject\f.gif")
scrn.tracer(0)
#design
turtle.register_shape(r"C:\Users\Matthew\PycharmProjects\PythonProject\SOULO.gif")
turtle.register_shape(r"C:\Users\Matthew\PycharmProjects\PythonProject\REPEARI.gif")

# border setup
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("darkseagreen")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#scores
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("light green")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score %s" %score
score_pen.write(scorestring, False, align="left", font=("Monospace", 14, "normal"))
score_pen.hideturtle()



# charsetup
player = turtle.Turtle()
player.color("blue")
player.shape(r"C:\Users\Matthew\PycharmProjects\PythonProject\REPEARI.gif")

player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)
# Player bilis
player.speed = 30

# PLAYER KONTROL BOLLIT
bullet = turtle.Turtle()
bullet.color("chartreuse")
bullet.shape("circle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 3

# state bollit
bulletstate = "ready"

# kalaban
num_of_klbns = 30
klbns = []


for i in range(num_of_klbns):
    klbns.append(turtle.Turtle())

klbn_start_x = -225
klbn_start_y = 250
klbn_number = 0



for klbn in klbns:
    klbn.color("darkred")
    klbn.shape(r"C:\Users\Matthew\PycharmProjects\PythonProject\SOULO.gif")
    klbn.setheading(270)
    klbn.penup()
    klbn.speed(0)
    x = klbn_start_x + (50 * klbn_number)
    y = klbn_start_y
    klbn.setposition(x, y)
    klbn_number += 1
    if klbn_number == 10:
        klbn_start_y -= 50
        klbn_number = 0

klbnspeed = 0.2

# Movement functions
def move_left():
    x = player.xcor()
    x -= 30
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += 30
    if x > 280:
        x = 280
    player.setx(x)


def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        winsound.PlaySound("boom10", winsound.SND_ASYNC)
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    return distance < 15

def you_win():
    """Displays 'You Win!' and stops game execution"""
    global running
    running = False  # Stop game loop

    # Hide
    player.hideturtle()
    for klbn in klbns:
        klbn.hideturtle()


    win_pen = turtle.Turtle()
    win_pen.speed(0)
    win_pen.color("gold")
    win_pen.penup()
    win_pen.hideturtle()
    win_pen.setposition(0, 0)
    win_pen.write("YOU WIN!", align="center", font=("Monospace", 24, "bold"))
    win_pen.setposition(0, -50)
    win_pen.write("Congratulations!", align="center", font=("Monospace", 24, "bold"))
    winsound.PlaySound("win.wav", winsound.SND_ASYNC)


def game_over():

    global running
    running = False  # Stop game loop

    # Hide player and enemies
    player.hideturtle()
    for klbn in klbns:
        klbn.hideturtle()

    game_over_pen = turtle.Turtle()
    game_over_pen.speed(0)
    game_over_pen.color("red")
    game_over_pen.penup()
    game_over_pen.hideturtle()
    game_over_pen.setposition(0, 0)
    game_over_pen.write("GAME OVER", align="center", font=("Monospace", 24, "bold"))
    game_over_pen.setposition(0, -50)
    game_over_pen.write("Thank you for playing!", align="center", font=("Monospace", 24, "bold"))




# keys
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")



# KLBN SPEED
while True:
    scrn.update()
    wall_ht = False
    for klbn in klbns:
        # Move enemy
        x = klbn.xcor()
        x += klbnspeed
        klbn.setx(x)

        # Check if any enemy touches the wall
        if x > 280 or x < -280:
            wall_ht = True

    if wall_ht:
        for klbn in klbns:
            y = klbn.ycor()
            y -= 40
            klbn.sety(y)

            # Check if enemy reaches bottom
            if y < -250:
                game_over()
                break

        klbnspeed *= -1

    # Check for bullet collision
    for klbn in klbns:
        if isCollision(bullet, klbn):
            winsound.PlaySound("boom7.wav", winsound.SND_ASYNC)
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)

            klbn.hideturtle()
            klbns.remove(klbn)
            score += 10
            scorestring = "Score: %s" % score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Monospace", 14, "normal"))


        if len(klbns) == 0:
            you_win()
            break

        if isCollision(klbn, player):
            print("YOUR DEATH WILL NOT BE IN VAIN BROTHER!!!")
            game_over()
            break
            winsound.PlaySound("win.wav", winsound.SND_ASYNC)

    # Move bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

        if bullet.ycor() > 275:
            bullet.hideturtle()
            bulletstate = "ready"

scrn.mainloop()