print("Welcome To Our Restaurant. Here's the menu")
MENU = {'Pizza': '180', 'Pasta': '80', 'Burger': '120', 'Maggi': '30', 'Sandwich': '60', 'Cappucino': '40',
        'Oreo': '120', 'Chocolate': '150', 'KitKat': '120', 'Almond': '140', 'Strawberry': '145',
        'Coke': '70', 'Pepsi': '80', 'Redbull': '110'}

# Display the menu
for item, price in MENU.items():
    print(f'{item}: Rs{price}')

order_total = 0

# Initial order
items_1 = str(input("Enter the item you want to order: ")).capitalize()
if items_1 in MENU:
    order_total += int(MENU[items_1])
    print(f'Your item {items_1} has been added.')
else:
    print(f"Ordered item {items_1} is not available yet!")

# Ask for additional items
while True:
    order_item2 = str(input("Do you want something else? (Yes/No): ")).upper()
    if order_item2 == 'YES':
        items_1 = str(input("Enter the item you want to order: ")).capitalize()
        if items_1 in MENU:
            order_total += int(MENU[items_1])
            print(f'Your item {items_1} has been added.')
        else:
            print(f"Ordered item {items_1} is not available yet!")
    else:
        print(f"Your total order amount is Rs{order_total} of {items_1}")
        break
