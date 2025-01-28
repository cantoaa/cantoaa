import os
import platform

dictionary = {}
people = []
Nperson = 0
Start = True
print("Welcome to the secret auction program.")
if input("Do you want to join the audiction? ").lower() == "yes":
    people.append(input("What is your name? "))
    dictionary[people[Nperson]] = input("What will be your bid? $")
    Nperson += 1
else:
    Start = False
while Start == True:
    if input("Do you want to add more people? ").lower() == "yes":
        os.system("cls")
        people.append(input("What is your name? "))
        dictionary[people[Nperson]] = input("What will be your bid? $")
        Nperson += 1
    else:
        Bvalue = 0
        values = []
        winners = []
        tie = 0
        for people_on_audiction in dictionary:
            values.append(dictionary[people_on_audiction])
        for competition in range(len(values)):
            if competition != 0:
                print(values[competition])
                if int(values[competition]) > int(Bvalue):
                    Bvalue = values[competition]
            else:
                Bvalue = values[competition]
        for finals in dictionary:
                if int(dictionary[finals]) == int(Bvalue):
                    winners.append(finals)
                    tie += 1
        if tie == 1:
            print(f"The winner of the audiction is {winners[0]} with a bid of ${Bvalue}")
        else:
            print(f"Its a tie on ${Bvalue} between {' and '.join(winners)}")
        Start = False