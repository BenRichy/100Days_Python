#final replit is here: https://replit.com/@appbrewery/coffee-machine-final?embed=1&output=1#main.py

# import data from coffee_menu file
from coffee_menu import resources
from coffee_menu import MENU

# get the starting resources for the coffee machine
current_water = resources['water']
current_milk = resources['milk']
current_coffee = resources['coffee']

# check that there are enough resources in the machine for the drink that wants to be ordered
def check_resources(drink):
    # say that current_ingredients are global variables so we can edit them
    global current_water, current_milk, current_coffee
    # get the resources required for the drink
    drink_water = MENU[drink]['ingredients']['water']
    drink_milk = MENU[drink]['ingredients']['milk']
    drink_coffee = MENU[drink]['ingredients']['coffee']

    # check that there are enough of each resource, if not, exit the code and say what there is not enough of
    # if there is enough, deduct from total pool
    if current_water >= drink_water:
        if current_milk >= drink_milk:
            if current_coffee >= drink_coffee:
                current_water -= drink_water
                current_milk -= drink_milk
                current_coffee -= drink_coffee
            else:
                print("Sorry, there's not enough coffee")
                quit()
        else:
            print("Sorry, there's not enough milk")
            quit()
    else:
        print("Sorry, there's not enough water")
        quit()

# get the payment for the drink
def get_check_payment(drink):
    global order_again
    quarters = int(input("How many quarters would you like to pay?: "))
    nickels = int(input("How many nickels would you like to pay?: "))
    dimes = int(input("How many dimes would you like to pay?: "))
    cents = int(input("How many cents would you like to pay?: "))

    total_payment = quarters*0.25 + nickels*0.10 + dimes*0.05 + cents*0.01

    drink_cost = MENU[drink]['cost']

    if total_payment >= drink_cost:
        print(f"Here is your change of {total_payment-drink_cost}.")
        print(f"Enjoy your {drink}.")
        another_drink = input("Would you like to order again? Y/N: ")
        if another_drink == "Y":
            order_again = True
        else:
            order_again = False
    else:
        print("Sorry, you have not paid enough, transaction failed.")


order_again = True

while order_again:
    print("Welcome to the coffee machine, what would you like to order?")
    user_order = input("Espresso, latte or cappuccino?: ").lower()

    # check resources are enough
    check_resources(user_order)
    get_check_payment(user_order)







