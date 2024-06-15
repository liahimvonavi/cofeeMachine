from drinks import MENU, resources
profit = 0
def check_resources(ingridients):
    for item in ingridients:
        if resources[item]>= ingridients[item]:
            return True
        else:
            print(f"Sorry not enough {item}")
            return False

def proccess_coins():
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total_input_amount = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies *0.01
    return total_input_amount

def check_payment(payment):
    if payment >= drink["cost"]:
        global profit
        if payment!=drink["cost"]:
            change = payment - drink["cost"]
            print(f"Here is ${change:.2f} in change.")
        profit+=drink["cost"]
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_cofee(ingredient):
    for item in ingredient:
        resources[item] -= ingredient[item]
    print(f"Here is your {user_choice}. Enjoy")


should_continue=True
while should_continue:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "off":
        exit()
    elif user_choice == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[user_choice]
        if check_resources(drink["ingredients"]):
            print ("Please insert coins.")
            payment = proccess_coins()
            if check_payment(payment):
                make_cofee(drink["ingredients"])

