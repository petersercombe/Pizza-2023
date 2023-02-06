# This is a program that will allow me to order pizza
# Copyright Peter Sercombe 2022
# CC-BY-SA-4.0

def listMenu(options):
    for i, (key, value) in enumerate(options.items()):
        print("{} - {} (+${:.2f})".format(i, key, value))

print("Welcome to Pete's a Pizza!")
# size
sizeOptions = {"New Yorker":5.00,
               "Large":3.00,
               "Small":0.00}
listMenu(sizeOptions)
size = input("What size pizza would you like? ")
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
topping = input("What kind of topping would you like? ")
# sauce
sauce = input("What sauce would you like? ")
# base
base = input("What base would you like? ")
# extra toppings
extraToppings = input("What extra toppings would you like? ")


# sides

# drinks




