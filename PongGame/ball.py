from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.Bangle = 0
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("slowest")
        self.shapesize(0.5,0.5)
        self.xinc = 10
        self.yinc = 10
    def move(self):
        self.goto(self.xcor() + self.xinc, self.ycor() + self.yinc)
    def collide_y(self):
        self.yinc *= -1
    def collide_x(self):
        self.xinc *= -1
