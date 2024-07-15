def print_report(water, milk, coffee, money):
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${{:0.2f}}".format(money))


def make_coffee(water, milk, coffee, money):
    global machine_water
    global machine_milk
    global machine_coffee
    global machine_money
    if machine_water >= water and machine_milk >= milk and machine_coffee >= coffee:
        machine_water -= water
        machine_milk -= milk
        machine_coffee -= coffee
        machine_money += money
        print("Making coffee... please wait")
        return True
    else:
        return False


def start_process():
    sum_of_coins = 0
    quarters = 0
    dimes = 0
    nickles = 0
    pennies = 0
    choice = input("What would you like? (espresso/latte/cappuccino) ").lower()
    if choice == 'report':
        print_report(machine_water, machine_milk, machine_coffee, machine_money)
        return True
    elif choice == 'exit' or choice == '':
        return False
    else:
        water = coffee_list[choice]['water']
        coffee = coffee_list[choice]['coffee']
        milk = coffee_list[choice]['milk']
        price = coffee_list[choice]['price']
        while sum_of_coins < price:
            print("Please insert coins.")
            try:
                quarters = int(input("How many quarters?: ")) * .25
                dimes = int(input("How many dimes?: ")) * .10
                nickles = int(input("How many nickles?: ")) * .05
                pennies = int(input("How many pennies?: ")) * .01
            except ValueError:
                print("Incorrect amount. Restarting...")

            sum_of_coins = quarters + dimes + nickles + pennies

            if sum_of_coins >= price:
                coffee_made = make_coffee(water, milk, coffee, price)
                if coffee_made:
                    change = sum_of_coins - price
                    print(f"Here is ${round(change, 2)} in change.\nHere is your {choice} 🍵 Enjoy!")
                else:
                    print("Not enough materials. Refunding money.")
        return True


coffee_list = {
    "espresso": {"water": 50, "coffee": 18, "milk": 0, "price": 1.50},
    "latte": {"water": 200, "coffee": 24, "milk": 150, "price": 2.50},
    "cappuccino": {"water": 250, "coffee": 24, "milk": 150, "price": 3.00}
}

machine_water = 300
machine_milk = 200
machine_coffee = 100
machine_money = float(100)

while start_process():
    print()
