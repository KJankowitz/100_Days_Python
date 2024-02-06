machine_on = True

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


def check_resources(drink):
    if resources["water"] < MENU[drink]["ingredients"]["water"]:
        return "Not enough water"
    elif resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
        return "Not enough coffee"
    elif resources["milk"] < MENU[drink]["ingredients"]["milk"]:
        return "Not enough milk"


def check_money(drink):
    all_money = (quarters*0.25) + (dimes*0.1) + (nickels*0.05) + (pennies*0.01)
    if all_money < MENU[drink]["cost"]:
        return "Not enough money. Refunding coins."
    elif all_money > MENU[drink]["cost"]:
        change = round(all_money - MENU[drink]["cost"], 2)
        return f"Please take your ${change} change"


def make_coffee(drink):
    water = resources["water"] - MENU[drink]["ingredients"]["water"]
    coffee = resources["coffee"] - MENU[drink]["ingredients"]["coffee"]
    milk = resources["milk"] - MENU[drink]["ingredients"]["milk"]
    return water, milk, coffee


while machine_on:
    instruction = input("What would you like? (espresso/latte/cappuccino):\n")
    if instruction == "report":
        print(resources)
    elif instruction == "off":
        machine_on = False
    print(check_resources(instruction))

    if check_resources(instruction) == "None":
        quarters = int(input("Please insert coins.\nHow many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))

        print(check_money(instruction))

        resources = {
            "water": make_coffee(instruction)[0],
            "milk": make_coffee(instruction)[1],
            "coffee": make_coffee(instruction)[2],
        }
