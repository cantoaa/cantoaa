import random


ecards = [1, 2, 3, 4 , 5 , 6 , 7 , 8 , 9, 10, 10, 10, 10]
ecards.extend(ecards*3)
sumcardsP = 0
playercards = []
dealercards = []
bet = 0
sumcardsD = 0
money = 1000
action = ""
start = 0
doubled = 0

def AddCard():
    global playercards, sumcardsP, ecards
    currentcard = random.choice(ecards)
    playercards.append(currentcard)
    sumcardsP += currentcard
    ecards.remove(currentcard)

def Double():
    global bet, sumcardsP, ecards, playercards 
    bet += bet
    currentcard = random.choice(ecards)
    playercards.append(currentcard)
    sumcardsP += currentcard
    ecards.remove(currentcard)

def DistributeCards():
    global playercards, sumcardsP, ecards, dealercards, sumcardsD 
    for i in range(0,2): 
        currentcard = random.choice(ecards)
        playercards.append(currentcard)
        sumcardsP += currentcard
        ecards.remove(currentcard)
        currentcard = random.choice(ecards)
        dealercards.append(currentcard)
        sumcardsD += currentcard
        ecards.remove(currentcard)

PlayerActions = {
        "add" : AddCard,
        "double" :  Double,
}

print("Welcome to Blackjack")
print("Instructions: \nDo a bet \nCheck the cards \nMake an action: \n Add = Get one more card \n Double = You double your bet but cant make other commands after that \n Stay = You stay with your cards \n \n Objective: Get your sum of cards higher than the dealer, but not beyond 21. \n \n \n")
print("Game started")
start = 1
while money > 0:
        bet = int(input("Insert bet: "))
        DistributeCards()
        
        print(f"Dealer card: {dealercards}")
        print(f"Your cards: {playercards}")
        while sumcardsP < 21 and action.lower() != "stay" and doubled == 0:
            action = input("What will be your action \n Add\n Double \n Stay\n")
            if action.lower() == "stay" :
                while sumcardsD < 17:
                    currentcard = random.choice(ecards)
                    dealercards.append(currentcard)
                    sumcardsD += currentcard
                    ecards.remove(currentcard)
            elif action.lower() == "double":
                    doubled = 1
                    PlayerActions[action.lower()]()
                    while sumcardsD < 17:
                            currentcard = random.choice(ecards)
                            dealercards.append(currentcard)
                            sumcardsD += currentcard
                            ecards.remove(currentcard)
            elif action.lower() == "add":
                PlayerActions[action.lower()]()
                print(f"Your cards {playercards}")
        if sumcardsP > 21:
            print(f"Dealer cards: {dealercards}")
            print(f"Your cards: {playercards}")
            print("Busted")
            money -= bet
        elif sumcardsD > sumcardsP and  sumcardsD <= 21:
            print(f"Dealer cards: {dealercards}")
            print(f"Your cards: {playercards}")
            print("Dealer won")
            money -= bet
        elif sumcardsD == sumcardsP and sumcardsP <= 21:
            print(f"Dealer cards: {dealercards}")
            print(f"Your cards: {playercards}")
            print("Tie")
        elif sumcardsP > sumcardsD and sumcardsP <= 21:
            print(f"Dealer cards: {dealercards}")
            print(f"Your cards: {playercards}") 
            print("You won")
            money += 2*bet
        elif sumcardsD > 21:
            print(f"Dealer cards: {dealercards}")
            print(f"Your cards: {playercards}")
            print("Dealer Busted. You won.")
            money += 2*bet
        action = ""
        playercards = []
        dealercards = []
        sumcardsP = 0
        sumcardsD = 0
        doubled = 0
        ecards = [1,2,3,4,5,6,7,8,9,10,10,10,10]
        ecards.extend(ecards*3)
        print(f"Money: {money}")
