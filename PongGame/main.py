from turtle import Screen
from paddle import Paddle
from scoreboard import ScoreBoard
from ball import Ball

screen = Screen()
screen.title("Pong Game")
screen.setup(600,600)
screen.bgcolor("black")

paddlex = 280
paddleL = Paddle(paddlex)
paddlex = -280
paddleR = Paddle(paddlex)

scoreL = ScoreBoard()
scoreR = ScoreBoard()
line = ScoreBoard()
start = ScoreBoard()

ball = Ball()

scoreL.createscoreboardL()
scoreR.createscoreboardR()
line.drawline()
start.startgame()


screen.onkey(paddleL.moveup, "Up")
screen.onkey(paddleL.movedown, "Down")

screen.onkey(paddleR.moveup, "w")
screen.onkey(paddleR.movedown, "s")

def Start():
    game = 1
    start.clear()
    screen.onkey(None, "")
    while game:
        ball.move()
        if ball.distance(paddleL) < 30 or ball.distance(paddleR) < 30:
            ball.collide_x()
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.collide_y()
        if ball.xcor() > 280:
            print("GameOver")
            scoreL.score += 1
            scoreL.createscoreboardL()
            game = 0
            ball.goto(0,0)
            start.startgame()
            screen.onkey(Start,"")
        if ball.xcor() < -280:
            print("GameOver")
            scoreR.score += 1
            scoreR.createscoreboardR()
            game = 0
            ball.goto(0,0)
            start.startgame()
            screen.onkey(Start, "")


screen.onkey(Start, "")
screen.listen()

screen.exitonclick()
