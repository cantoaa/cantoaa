Drinks = {

        'espresso': [1.5,50, 18,0],
        'latte' : [2.5,200, 24, 150],
        'cappuccino' : [3, 250, 24, 100]
        
        }
Machine = [300, 100, 200]
money = 0
coins = {
        'penny' : 0.01,
        'nickel' : 0.05,
        'dime' : 0.10,
        'quarter' : 0.25
        }
order = ""
print("Welcome to a program that simulates a Coffee Machine")
print("Drinks: Espresso, Latte, Cappuccino")
while True:
    order = input("What drink will you have: ").lower()
    if order in Drinks and Machine[0] >= Drinks[order][1] and Machine[1] >= Drinks[order][2] and Machine[2] >= Drinks[order][3]: 
        money += coins['penny'] * int(input("How many penny coins: "))
        money += coins['nickel'] * int(input("How many nickel coins: "))
        money += coins['dime'] * int(input("How many dime coins: "))
        money += coins['quarter'] * int(input("How many quarter coins: "))
        if money >= Drinks[order][0]:
            Drinks[order]
            for i in range(0, len(Machine)):
               Machine[i] -= Drinks[order][i + 1]
            print(f"You ordered a {order}")
            money -= Drinks[order][0] 
            print(f"Here is your change.{money}")
        else:
            print("Not enough resources on the machine")
    elif order == "report":
        print(f"Machine: \n Water: {Machine[0]}\n Coffe: {Machine[1]}\n Milk: {Machine[2]}")
    elif order == "off":
        break
    else:
        print("Invalid drink or order. Please try a valid one")
    money = 0
    order = ""
