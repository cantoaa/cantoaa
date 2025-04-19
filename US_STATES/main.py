import turtle
import pandas

with open("50_states.csv") as states_data:
    data = pandas.read_csv(states_data)
    states = data["state"].to_list()

screen = turtle.Screen()
screen.title("US STATES GAME")
screen.setup(700,500)
image = "blank_states_img.gif"
turtle.addshape(image)

turtle.shape(image)
correct_guessed = []
while len(correct_guessed) < 50:
    answer = screen.textinput(f"Guess the states({len(correct_guessed)}/50)", "State name:").title()
    if answer == "Exit":
        break
    if answer in states:
        text = turtle.Turtle()
        text.hideturtle()
        text.penup()
        statex = data[data.state == answer].x.item()
        statey = data[data.state == answer].y.item()
        text.goto(statex,statey)
        text.write(f"{answer}", align = "center", font=("Arial", 20, "normal"))
        print("Correct")
        correct_guessed.append(answer)
    else:
        print("Wrong")
screen.bye()
wrong_guessed = []
for wrong_guesses in states:
    if wrong_guesses not in correct_guessed:
        wrong_guessed.append(wrong_guesses)

states_to_learn = {"states to learn" : wrong_guessed}
df = pandas.DataFrame(states_to_learn)
if input("Want to show missing guesses?(y/n)") == "y":
    print(df)
df.to_csv("states_to_learn.csv")
