import json

DATA_product = []
total_inventory = 0
rejected_entry = 0

#add_product(),update_stock(),search_product(),display_all()

def display_menu():
    print("---------MENU----------")
    txt_menu_options = ["1. Display All Products",
                    "2. Add Product",
                    "3. Update Stock",
                    "4. Search Product",
                    "5. Save Inventory",
                    "6. Exit"
                    ]
    [print(i) for i in txt_menu_options]

    option_num = input("Choose Option:  ")
    if option_num.isdigit() == False:
        print("Please select a number. ")
        return 

    return int(option_num)


def load_inventory():
    print("-------------------------------")
    print("-------------------------------")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("-------------------------------")
    print("-------------------------------")
    print('')
    try:
        with open('inventory.json','r') as file:
            total_inventory = 0

            # File exists but contains nothing
            if file.read().strip() == "":
                print("inventory.json is empty.")
                print("Starting with empty inventory.")
                return [], 0

            # Go back to beginning of file
            file.seek(0)

            product_ids = json.load(file)
            DATA_product = product_ids

            #Update total inventory
            for item in DATA_product:
                Stock = item["Stock"]
                total_inventory += Stock
            
            print("inventory.json found.")
            print("Inventory loaded successfully.")
            print("")

            return DATA_product,total_inventory

    except FileNotFoundError:
        with open('inventory.json','w') as file:
            print("New inventory Created. ")
            return [],[]


def display_all(product_items):
    for item in product_items:
        ID = item["ID"]
        Name = item["Name"]
        Price = item["Price"]
        Stock = item["Stock"]

        print(f"ID: {ID} | Name: {Name} | Price: {Price} | Stock: {Stock}")
    print("")


def search_product():
    print("")
    print("Search Product")
    ID = str(input("Enter Product ID: "))
    print("")

    for item in DATA_product:
        if item["ID"] == ID:
            print("Product Found: ")
            print("------------------------------------------")
            print(f"ID: {ID} | Name: {item["Name"]} | Price: {item["Price"]} | Stock: {item["Stock"]}")
            print("------------------------------------------")
            return ID
    print("Product not found.")
    return None


def update_stock(ID):
    new_val = int(input("New Stock Quantity: "))
    for item in DATA_product:
        if item["ID"] == ID:
            item["Stock"] = new_val
            return ID,new_val
    return None


def save_inventory(LISTofITEMS):
    with open('inventory.json', 'w') as file:
        json.dump(LISTofITEMS, file, indent=4)   
    print("Inventory saved successfully. ")


def add_product(product_items):
    print("Add New Product")

    product_id = input("Product ID: ").strip()

    # Check if ID already exists
    for item in product_items:
        if item["ID"] == product_id:
            print("Error: Product ID already exists.")
            return

    product_name = input("Product Name: ").strip()

    while True:
        try:
            price = float(input("Price: "))
            if price < 0:
                print("Price cannot be negative.")
                continue
            break
        except ValueError:
            print("Please enter a valid price.")

    while True:
        try:
            stock = int(input("Stock Quantity: "))
            if stock < 0:
                print("Stock cannot be negative.")
                continue
            break
        except ValueError:
            print("Please enter a whole number.")

    new_product = {
        "ID": product_id,
        "Name": product_name,
        "Price": price,
        "Stock": stock
    }

    product_items.append(new_product)

    print("Product added successfully!")


def Menu_OPERATIONS(option):
    if option == 1:
        display_all(DATA_product)

    if option == 2:
        add_product(DATA_product)

    if option == 3:
        print("Update Stock ")

        ID = search_product()

        if ID is None:
            return "continue"

        result = update_stock(ID)

        if result is not None:
            ID, new_val = result
            print(f"Stock updated: {ID} -> {new_val}")

        return "continue"
            

    if option == 4:
        exist = search_product()
        if exist == 0:
            print("Product not found. ")
            return "continue"

    if option == 5:
        print("Saving inventory... ")
        save_inventory(DATA_product)

    if option == 6:
        print("Saving inventory before exit...")
        save_inventory(DATA_product)
        return "quit"


while True:

    if DATA_product == []:
        DATA_product,total_inventory = load_inventory()
    task = Menu_OPERATIONS(display_menu())

    if task == "quit":
        break
    if task == "continue":
        continue



    print("")
    
    
