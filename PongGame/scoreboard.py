from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.pencolor("white")
        self.penup()
    def createscoreboardR(self):
        self.clear()
        self.goto(40,240)
        self.write(f"{self.score}",align="center",font=("Press Start 2P", 24, "normal"))
    def createscoreboardL(self):
        self.clear()
        self.goto(-40,240)
        self.write(f"{self.score}",align="center",font=("Press Start 2P",24,"normal"))
    def drawline(self):
        self.goto(0,-280)
        self.setheading(90)
        for i in range(15):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
    def startgame(self):
        self.write("Press ENTER to start", align="center", font=("Press Start 2P", 40, "normal"))
