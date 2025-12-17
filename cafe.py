# Print a list called menu that stores at least four items sold in your cafe
menu = ["menu1", "menu2", "menu3", "menu4"]
print("Menu items available in the cafe:")
for item in menu:
    print("-", item)

# '''Print a dictionary called stock that should contain the stock
# value for each item on your menu.'''
stock = {
    "menu1": 13,
    "menu2": 1,
    "menu3": 3,
    "menu4": 7
}
print("Stock availability:")
for item, quantity in stock.items():
    print(f"{item}: {quantity}")

# '''Print a dictionary called price that should contain the prices for each
# item on your menu.'''
price = {
    "menu1": 25.39,
    "menu2": 15.10,
    "menu3": 30.00,
    "menu4": 40.99
}
print("Price list:")
for item, cost in price.items():
    print(f"{item}: R {cost:.2f}")

# '''Calculate the total value of the stock in the café and then
# store the results inside a variable called total_stock.'''
total_stock = sum(stock[item] * price[item] for item in stock)
print(f"Total stock worth: R {total_stock:.2f}")
