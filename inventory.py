class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        pass

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"Shoe [Country: {self.country}, Code: {self.code}, \
            Product: {self.product}, Cost: {self.cost}, Quantity: {self.quantity}]"
        pass


'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []



def read_shoes_data():
    opened_file = open("inventory.txt", "r")
    lines = opened_file.readlines()
    for line in lines[1:]:
        try:
            country, code, product, cost, quantity = line.strip().split(",")
            shoe = Shoe(country, code, product, float(cost), int(quantity))
            shoe_list.append(shoe)
        except ValueError:
            continue
    opened_file.close()


def capture_shoes():
    country = input("Enter the country: ")
    code = input("Enter the code: ")
    product = input("Enter the product: ")
    cost = float(input("Enter the cost: "))
    quantity = int(input("Enter the quantity: "))
    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)
    pass


def view_all():
    for shoe in shoe_list:
        print(shoe)
    pass
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''

def re_stock():
    if not shoe_list:
        print("No shoes in inventory.")
        return
    min_shoe = min(shoe_list, key=lambda x: x.quantity)
    print(f"Low stock alert! {min_shoe.product} (Code: {min_shoe.code}) \
        has only {min_shoe.quantity} left.")
    restock = input("Do you want to add more? (yes/no): ")
    if restock.lower() == "yes":
        quantity = int(input("Enter quantity to add: "))
        min_shoe.quantity += quantity
        print(f"New quantity for {min_shoe.product} is {min_shoe.quantity}.")
    # This quantity should be updated on the file for this shoe.


def search_shoe():
    code = input("Enter the shoe code to search: ")
    for shoe in shoe_list:
        if shoe.code == code:
            print(shoe)
            return shoe
    else:
        print("Shoe not found.")


def value_per_item():
    for shoe in shoe_list:
        value = shoe.get_cost() * shoe.get_quantity()
        print(f"Total value for {shoe.product} (Code: {shoe.code}) is {value}.")
    

def highest_qty():
    max_shoe = max(shoe_list, key=lambda x: x.quantity)
    print(f"Highest quantity shoe is {max_shoe.product} \
        (Code: {max_shoe.code}) with {max_shoe.quantity} in stock.")
    print(f"This shoe is available for sale.")


'''
Create a menu that executes each function above.
'''


def main():
    read_shoes_data()
    while True:
        print("\nShoe Inventory Management System")
        print("1. View all shoes")
        print("2. Capture new shoe")
        print("3. Re-stock low inventory")
        print("4. Search for a shoe")
        print("5. Calculate value per item")
        print("6. Show highest quantity shoe")
        print("7. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            view_all()
        elif choice == '2':
            capture_shoes()
        elif choice == '3':
            re_stock()
        elif choice == '4':
            search_shoe()
        elif choice == '5':
            value_per_item()
        elif choice == '6':
            highest_qty()
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
