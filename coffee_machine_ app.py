# coffee_machine.py
# Coffee Machine Project (beginner-friendly)
# Features:
# - MENU with three drinks (espresso, latte, cappuccino)
# - track resources (water, milk, coffee)
# - accept coins and calculate change
# - check resources before making drink
# - "report" command to print resources and profit
# - "off" command to stop the machine

MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0.0


def is_resource_sufficient(order_ingredients):
    """Return True when order can be made, False if ingredients are insufficient.
    If insufficient, prints which ingredient is lacking."""
    for item, required_amount in order_ingredients.items():
        available = resources.get(item, 0)
        if required_amount > available:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    try:
        quarters = int(input("How many quarters? "))  # 0.25
        dimes = int(input("How many dimes? "))        # 0.10
        nickels = int(input("How many nickels? "))    # 0.05
        pennies = int(input("How many pennies? "))    # 0.01
    except ValueError:
        print("Invalid coin input. Treating as zero.")
        quarters = dimes = nickels = pennies = 0

    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return round(total, 2)


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, False if insufficient.
    If payment is sufficient, calculates change and updates profit."""
    global profit
    if money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False

    change = round(money_received - drink_cost, 2)
    if change > 0:
        print(f"Here is ${change} in change.")
    profit += drink_cost
    return True


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources and 'serve' the coffee."""
    for item, amount in order_ingredients.items():
        resources[item] -= amount
    print(f"Here is your {drink_name} ☕. Enjoy!")


def report():
    """Print current resource levels and profit."""
    print("Machine report:")
    print(f"Water: {resources.get('water', 0)}ml")
    print(f"Milk: {resources.get('milk', 0)}ml")
    print(f"Coffee: {resources.get('coffee', 0)}g")
    print(f"Money: ${profit:.2f}")


def coffee_machine():
    is_on = True
    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if choice == "off":
            print("Turning off. Goodbye!")
            is_on = False

        elif choice == "report":
            report()

        elif choice in MENU:
            drink = MENU[choice]
            if is_resource_sufficient(drink["ingredients"]):
                payment = process_coins()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])
        else:
            print("Invalid choice. Please choose espresso, latte, cappuccino, report, or off.")


if __name__ == "__main__":
    coffee_machine()
