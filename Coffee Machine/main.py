MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO: 1 Start machine with prompt "What would you like? (espresso/latte/cappuccino):"
instruction = input("What would you like? (espresso/latte/cappuccino):\n")
# TODO: 2 Turn off by entering "off"
# TODO: 3 Print report on "report" prompt to show current resources
if instruction == "report":
    print(resources)
# TODO: 4 Check for sufficient resources to make drink


def check_resources(drink):
    if resources["water"] < MENU[drink]["ingredients"]["water"]:
        return "Not enough water"
    elif resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
        return "Not enough coffee"
    elif resources["milk"] < MENU[drink]["ingredients"]["milk"]:
         return "Not enough milk"


print(check_resources(instruction))

# TODO: 5 Process coins - if sufficient resources, prompt user to insert coins
#25c
quarters = int(input("Please insert coins.\nHow many quarters?: "))
#10c
dimes = int(input("How many dimes?: "))
#5c
nickels = int(input("How many nickels?: "))
#1c
pennies = int(input("How many pennies?: "))
def check_money(drink):
    all_money = (quarters*0.25) + (dimes*0.1) + (nickels*0.05) + (pennies*0.01)
    if all_money < MENU[drink]["cost"]:
        return "Not enough money. Refunding coins."

print(check_money(instruction))
# TODO: 6 Check successful transaction - either refunded if insufficient or added to machine as profit,
#  or offered change
# TODO: 7 Make coffee - deduct ingredients from resources and present to user
