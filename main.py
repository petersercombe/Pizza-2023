# This is a program that will allow me to order pizza
# Copyright Peter Sercombe 2022
# CC-BY-SA-4.0

from menu import *

def listMenu(options):
    for i, (key, value) in enumerate(options.items()):
        print("{} - {} (+${:.2f})".format(i, key, value))

def userInput(options):
    global price
    # List the menu items:
    listMenu(options)
    # Check the input is a number - integer
    while True:
        try:
            selection = int(input("Input your choice: "))
            # Check that the number is a menu option.
            if 0 <= selection < len(options):
                price += list(options.values())[selection]
                return list(options)[selection]
            print("Please enter a valid choice.")
        except ValueError:
            print("Please enter a number")


print("Welcome to Pete's a Pizza!")

pizzas = []
price = 0.0

while True:
    # size
    size = userInput(sizeOptions)
    # topping
    topping = userInput(toppingOptions)
    # sauce
    sauce = userInput(sauceOptions)
    # base
    base = userInput(baseOptions)

    pizzas.append(f"{size} {topping} with {sauce} sauce on {base} base")
    if input("Would you like more pizza? y/n: ").lower() == "y":
        continue
    else:
        break

# sides
sides = []
while True:
    sides.append(userInput(sideOptions))
    if input("Would you like another side? y/n: ").lower() == "y":
        continue
    else:
        break

# drinks
drinks = []
while True:
    drinks.append(userInput(drinkOptions))
    if input("Would you like another side? y/n: ").lower() == "y":
        continue
    else:
        break

print("Your order is: ")
for pizza in pizzas:
    print(pizza)
for side in sides:
    print(side)
for drink in drinks:
    print(drink)


print("For a total of ${:.2f}".format(price) )
