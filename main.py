from turtle import Turtle, Screen
import turtle as turt
import random
turt.colormode(255)
screen = Screen()
screen.setup(1000,500)
tim = Turtle()
tom = Turtle()
tam = Turtle()
tum = Turtle()
turtles = [tim,tom,tam,tum]
names = {
    tim : "Tim",
    tom : "Tom",
    tam : "Tam",
    tum : "Tum"
}

posY = -80

def Colors():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

def SetRace(cturt,pos):
    cturt.shape("turtle")
    cturt.color(Colors())
    cturt.penup()
    cturt.setx(-450)
    cturt.sety(pos)
    cturt.pendown()

SetRace(tim,posY)
tim.write("Tim", True, align = "center", font=('Arial',14,'normal'))
posY += 50
SetRace(tom,posY)
tom.write("Tom", True, align = "center", font=('Arial',14,'normal'))
posY += 50
SetRace(tam,posY)
tam.write("Tam", True, align = "center", font=('Arial',14,'normal'))
posY += 50
SetRace(tum,posY)
tum.write("Tum", True, align = "center", font=('Arial',14,'normal'))

user_bet = screen.textinput("Make your bet", "Which turtle will win the race(tim,tom,tam,tum)")
if user_bet:
    running = 1
    while running:
        for turtle in turtles:
            if turtle.xcor() < 450:
                turtle.forward(random.randint(0,10))
            else:
                print(f"{names[turtle]} won the race!")
                if user_bet.lower() == names[turtle].lower():
                    print("Congrats, you made the right bet!") 
                else:
                    print("You lost.")
                running = 0

screen.exitonclick()
