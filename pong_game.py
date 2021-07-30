"This code is the tweaked and improved version of Christian Thompson's Pong"
"Link: http://christianthompson.com/sites/default/files/Pong/pong.py"

import turtle
import winsound
from random import randint

wn = turtle.Screen()
wn.title("Pong by O.K.")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.hideturtle()

def paddle_up_a():
    y = paddle_a.ycor()

    if(y <= 239):
        y += 20
        paddle_a.sety(y)


def paddle_down_a():
    y = paddle_a.ycor()

    if(y >= -239):
        y -= 20
        paddle_a.sety(y)

ball = turtle.Turtle()
ball.speed(1)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.7
ball.dy = 0.7
ball.hideturtle()

paddle_b = turtle.Turtle()
paddle_b.speed(1)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=15,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.hideturtle()

def paddle_up_b():
    y = paddle_b.ycor()

    if(y <= 150):
        y += 1
        paddle_b.sety(y)

def paddle_down_b():
    y = paddle_b.ycor()

    if(y >= -150):
        y -= 1
        paddle_b.sety(y)




#starting the game
def start():
   

    ball.showturtle()
    paddle_a.showturtle()
    paddle_b.showturtle()


    # clearing intro titles
    pen1.clear()
    
   

    # setting the game boundaries
    pen2= turtle.Turtle()
    pen2.speed(0)
    pen2.color("white")
    pen2.goto(399,299)
    pen2.clear()
    pen2.goto(-399,299)
    pen2.goto(-399,-299)
    pen2.goto(399,-299)
    pen2.goto(399,299)

    #changing sound file
    winsound.PlaySound(None, winsound.SND_PURGE)
    winsound.PlaySound("rasputin.wav", winsound.SND_ASYNC | winsound.SND_ALIAS | winsound.SND_LOOP)

    wn.listen()

    wn.onkeypress(paddle_up_a, "Up")
    wn.onkeypress(paddle_down_a, "Down")


#shutting the game down
def close():
    wn.bye()

# Intro titles
pen1 = turtle.Turtle()
pen1.speed(0)
pen1.shape("square")
pen1.color("white")
pen1.penup()
pen1.hideturtle()
pen1.goto(0, 260)
pen1.write("Welcome to the Game!\nSPACE: Start -- ESC: Quit\nCreated by Onat Kaya, Inspired from Christian Thompson", align="center", font=("Georgia", 40, "normal"))

wn.listen()
wn.onkeypress(close, "Escape")
wn.onkeypress(start, "space")

#play intro song
winsound.PlaySound("happy.wav", winsound.SND_ASYNC | winsound.SND_ALIAS | winsound.SND_LOOP )


pen2 = turtle.Turtle()
pen2.speed(0)
pen2.shape("square")
pen2.color("white")
pen2.penup()
pen2.hideturtle()
pen2.goto(0,260)

# main game loop
while (True):
    
    wn.update()

    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1


    if ball.xcor() > 350:
        #score_a += 1
        
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        #score_b += 1
        

        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1

    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 150 and ball.ycor() > paddle_b.ycor() - 150:
        ball.dx *= -1

    value = randint(0,20)
    if(value % 2 == 0):
        for i in range(value):
            paddle_up_b()
    else:
        for i in range(value):
            paddle_down_b()


    