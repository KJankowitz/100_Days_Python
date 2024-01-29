MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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
    "milk": 20,
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
    if MENU[drink]["ingredients"]["milk"]:
        if resources["milk"] < MENU[drink]["ingredients"]["milk"]:
         return "Not enough milk"


print(check_resources(instruction))

# TODO: 5 Process coins - if sufficient resources, prompt user to insert coins
# TODO: 6 Check successful transaction - either refunded if insufficient or added to machine as profit,
#  or offered change
# TODO: 7 Make coffee - deduct ingredients from resources and present to user
