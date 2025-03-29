import random

dificuldade = ""
rnumber = 0
pguess =0
attempts = 0
KeepGoing = True

def Guessing():
    global attempts, rnumber, pguess
    while attempts > 0:
        pguess = int(input("Guess a number: "))
        if pguess == rnumber:
            print("You won!")
            break
        elif pguess > rnumber:
            print("Too High")
            attempts -= 1
            print(f"{attempts} attempts left")
        elif pguess < rnumber:
            print("Too Low")
            attempts -= 1
            print(f"{attempts} attempts left")
    if attempts == 0:
        print("You lost")

print("Welcome to the Number Guessing Game")

while KeepGoing:    
    print("Guess a number between 1 and 100")
    rnumber = random.randint(1,100)
    dificuldade = input("Insert a difficulty(easy or hard): ").lower()
    if dificuldade == "easy":
        attempts = 10
        print(f"You have {attempts} attempts")
    elif dificuldade == "hard":
        attempts = 5
        print(f"You have {attempts} attempts")
    else:
        print("Invalid difficulty")
    Guessing()
    if input("Want to continue player(y/n)").lower() == "y":
        KeepGoing = True
        rnumber = 0
        pguess = 0
        dificuldade = ""
        attempts = 0
    else:
        KeepGoing = False
