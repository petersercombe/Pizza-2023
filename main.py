# This is a program that will allow me to order pizza
# Copyright Peter Sercombe 2022
# CC-BY-SA-4.0

def listMenu(options):
    for i, (key, value) in enumerate(options.items()):
        print("{} - {} (+${:.2f})".format(i, key, value))

def userInput(options):
    # Check the input is a number - integer
    while True:
        try:
            selection = int(input("Input your choice: "))
            # Check that the number is a menu option.
            if 0 <= selection < len(options):
                return list(options)[selection]
            print("Please enter a valid choice.")
        except ValueError:
            print("Please enter a number")


print("Welcome to Pete's a Pizza!")

pizzas = []
price = 0.0

while True:
    # size
    sizeOptions = {"New Yorker":9.00,
                   "Large":6.00,
                   "Small":4.00}
    listMenu(sizeOptions)
    size = userInput(sizeOptions)
    # topping
    toppingOptions = {"Meatlovers":0.0,
                      "Pepperoni":0.0,
                      "Vegan":3.0,
                      "Vegorama":1.0,
                      "Avocado":4.0,
                      "Margherita":0.0,
                      "Cheese":0.0,
                      "Gourmet Fish Breath":15.0}
    listMenu(toppingOptions)
    topping = userInput(toppingOptions)
    # sauce
    sauceOptions = {"BBQ":0.0,
                    "Tomato":0.0,
                    "Bechemal":1.0,
                    "None":-1.0}
    listMenu(sauceOptions)
    sauce = userInput(sauceOptions)
    # base
    baseOptions = {"Classic Crust":0.0,
                   "Deep Pan": 0.0,
                   "Thin 'n' Crispy":0.0,
                   "Gluten Free": 2.0}
    listMenu(baseOptions)
    base = userInput(baseOptions)

    pizzas.append(f"{size} {topping} with {sauce} sauce on {base} base")

    if input("Would you like more pizza? y/n: ").lower() == "y":
        continue
    else:
        break


# sides

# drinks


print("Your order is: ")
for pizza in pizzas:
    print(pizza)

