from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(1,3)
        self.penup()
        self.setheading(90)
        self.setx(x)
        self.y = self.ycor()
    def moveup(self):
        self.y += 10
        self.sety(self.y)
    def movedown(self):
        self.y -= 10
        self.sety(self.y)
