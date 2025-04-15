from turtle import Turtle
POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.segments = []
        self.createsnake()
        self.head = self.segments[0]
    def createsnake(self):
        for position in POSITIONS:
            newsegment = Turtle("square")
            newsegment.color("white")
            newsegment.penup()
            newsegment.goto(position)
            newsegment.speed("fastest")
            self.segments.append(newsegment)
        self.lastseg = self.segments[len(self.segments) - 1]
    def addsegment(self):
        newsegment = Turtle("square")
        newsegment.color("white")
        newsegment.penup()
        lastX = self.lastseg.xcor()
        lastY = self.lastseg.ycor()
        if self.head.heading() == UP or self.head.heading() == DOWN:
            newsegment.goto(lastX, lastY -20)
            self.segments.append(newsegment)
        else:
            newsegment.goto(lastX - 20, lastY)
        self.segments.append(newsegment)
    def move(self):
        for seg in range(len(self.segments)- 1,0,-1):
            newY = self.segments[seg - 1].ycor()
            newX = self.segments[seg - 1].xcor()
            self.segments[seg].goto(newX,newY)
        self.head.forward(MOVE_DISTANCE)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
