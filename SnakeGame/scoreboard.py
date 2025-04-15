from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0,200)
        self.score = 0
        self.pencolor("white")
        self.writescore()
    def writescore(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center",font=("Arial",24,"normal"))
    def writegameover(self):
        self.penup()
        self.goto(0,0)
        self.pendown()
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))
