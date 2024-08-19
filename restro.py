# Defining menu
menu = {
    'Pizza' : 40,
    'Pasta' : 50,
    'Burger' : 60,
    'Salad' : 70,
    'Coffee' : 80
}

# Greet the customer
print('Welcome to our restaurant')

# Display the menu
print('Menu:')
print('Pizza: Rs40\nPasta: Rs50\nBurger: Rs60\nSalad: Rs70\nCoffee: Rs80')

# Asking user for their first order
order1 = input("What do you want to order?")

# Initialize the total cost of the order
order_total = 0

# Check if the first order is in the menu
if order1 in menu:
    # Add the price of the first item to the total
    order_total += menu[order1]
    print(f"Your item {order1} has been added to your order!")
else:
    # Notify the user if the item is not on the menu
    print("Invalid order\nTry again")

# Ask if the customer wants to add another item to the order
choice = input("Do you still want to place your order (Yes/No)?")

# Check the user's response
if choice.upper() == "YES":
    # Asking user for their second order
    order2 = input("What do you want to order?")
    
    # Check if the second order is in the menu
    if order2 in menu:
        # Add the price of the second item to the total
        order_total += menu[order2]
        print(f"Your item {order2} has been added to your order!")
    else:
        # Notify the user if the item is not on the menu
        print("Invalid order\nTry again")
    
    # Display the total amount to be paid
    print(f"The total amount to pay is Rs{order_total}")
else:
    # If no additional order, display the current total
    print(f"The total amount to pay is Rs{order_total}")
