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
    "milk": 200,
    "coffee": 100,
}
order_continue=True
money=0


def get_details(drink):
    ingredients= MENU[drink]['ingredients']
    water=ingredients.get("water",0)
    milk=ingredients.get("milk",0)
    coffee=ingredients.get("coffee",0)
    cost=MENU[drink]["cost"]

    return milk,water,coffee,cost

def generate_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def is_resource_sufficient(drink):
    ingredients= MENU[drink]['ingredients']
    for item in ingredients:
        if ingredients[item]> resources[item]:
            print(f"sorry,not enough {item}.")
            return False

    return True

def make_coffee(drink):
    ingredients= MENU[drink]['ingredients']
    for item in ingredients:
        resources[item]-=ingredients[item]

def money_handle(drink):
    print("please insert coins:")
    quarters=int(input("How many quarters?"))
    dimes=int(input("How many dimes?"))
    nickles=int(input("How many nickles?"))
    pennies=int(input("How many pennies?"))
    total=quarters*0.25+dimes*0.10+nickles*0.05+pennies*0.01
    cost=MENU[drink]["cost"]
    if total>=cost:
        change=round(total-cost,2)
        print(f"Here is ${change} in change")
        return True , cost
    else:
        print("Sorry that's not enough money.Money refunded ")
        return False,0









while order_continue:
    order = input("What would you like? (espresso/latte/cappuccino):").lower()
    if order== "report":
        generate_report()
    elif order=="off":
        order_continue=False
    elif order in MENU:
        if is_resource_sufficient(order):
            success, cost_paid=money_handle(order)
            if success:
                make_coffee(order)
                money+=cost_paid
                print(f"Here is your {order}. Enjoy!")


    else:
        print("Invalid selection.")






