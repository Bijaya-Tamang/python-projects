menu = {
    'Pizza' : 40,
    'Pasta' : 50,
    'Burger' : 60,
    'Salad' : 70,
    'Coffee' : 80
}

print('Welcome to our resturant')
print('Menu:')
print('Pizza: Rs40\nPasta: Rs50\nBurger: Rs60\nSalad: Rs70\nCoffee: Rs80')

order1 = input("What do you want to order?")

order_total = 0

if order1 in menu:
    order_total += menu[order1]
    print(f"Your item {order1} has been added to your order!")
else:
    print("Invalid order\nTry again")

choice = input("Do you still want to place your order(Yes/No)?")

if choice.upper() == "YES":
    order2 = input("What do you want to order?")
    if order2 in menu:
        order_total += menu[order2]
        print(f"Your item {order2} has been added to your order!")
    else:
        print("Invalid order\nTry again")
    print(f"The total amount to pay is Rs{order_total}")
else:
    print(f"The total amount to pay is Rs{order_total}")