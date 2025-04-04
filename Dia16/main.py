from menu import Menu
from coffe_maker import CoffeeMaker
from money_machine import MoneyMachine

print("Welcome to an OOP Coffee Machine")
print(f"Flavors: {Menu().get_items()}")
while True:
    order = input("Make an order: ")
    if order == "report":
        CoffeeMaker().report()
        MoneyMachine().report()
    elif order in Menu().get_items():
        drink = Menu().find_drink(order)
        print(drink.name, " costs: ", drink.cost)
        print(drink.name, " ingredients: ", drink.ingredients)
        if input("Want to buy it?(y/n) ") == "y":
            if CoffeeMaker().is_resource_sufficient(drink):
                if MoneyMachine().make_payment(drink.cost):
                    CoffeeMaker().make_coffee(drink)
        else:
            continue
    elif order == "break":
        break
