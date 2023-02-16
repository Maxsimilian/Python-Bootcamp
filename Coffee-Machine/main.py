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
def resource_check(order_ingredients):
    for items in order_ingredients:
        if order_ingredients[items] >= resources[items]:
            print(f"Sorry there is not enough {items}.")
            return False
        return True

def coin_operator():
    """Returns the total calculation from the coins"""
    print("Please insert coins.")
    total = int(input("how many quaters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def transaction(coin, drink_cost):
    """Return True when the payment is accepted or False if the money is insufficient."""
    global profit
    if coin >= drink_cost:
        change = round(coin - drink_cost, 2)
        print(f"Here is ${change} in change.")
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
def make_drink(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for items in order_ingredients:
        resources[items] -= order_ingredients[items]
    print(f"Here is your {drink_name} ☕")

profit = 0
print("Thank you for choosing this Coffee Machine!")
print("You can simply turn off the machine by typing 'off' in the drink selection")
end_program = False
while not end_program:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        print("Goodbye!")
        end_program = True
    elif choice == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if resource_check(drink["ingredients"]):
           payment = coin_operator()
           if transaction(payment,drink["cost"]):
               make_drink(choice, drink["ingredients"])
