import json

products = []

class Product:

    def __init__(self,ID:str,product_Name:str,cost:float,stock:int):
        self.__ID = ID
        self.__product = product_Name
        self.__cost = cost
        self.__stock = stock

    def to_dict(self):
        return {
            "ID" : self.__ID,
            "Name" : self.__product,
            "Price" : self.__cost,
            "Stock" : self.__stock
        }

    def display_information(self) -> None:
        print(f'ID : {self.__ID}')
        print(f'Name : {self.__Name}')
        print(f'Price : ${self.__cost:.2f}') 
        print(f'Stock : {self.__quantity}')

    def update_stock(self,quantity):
        if quantity < 0:
            print("Stock cannot be negative")
            return
        self.__stock = quantity

    @classmethod
    def from_dict(cls, data):
        # Convert a dictionary from JSON into a list
        return cls(
            data["ID"],
            data["Name"],
            data["Price"],
            data["Stock"]
        )


class File_Handling:

    def __init__(self, filename = "inventory.json", ):
        self.__filename = filename
        

    def load_inventory(self):
        print("-------------------------------")
        print("-------------------------------")
        print("INVENTORY MANAGEMENT SYSTEM")
        print("-------------------------------")
        print("-------------------------------")
        print('')
        try:
            with open(self.__filename,'r') as file:
                total_inventory = 0

                # File exists but contains nothing
                if file.read().strip() == "":
                    print("inventory.json is empty.")
                    print("Starting with empty inventory.")
                    return [],0

                # Go back to beginning of file
                file.seek(0)

                product_ids = json.load(file)
                DATA_product = product_ids

                #Update total inventory
                products = [
                    Product.from_dict(item) for item in DATA_product
                ]

                for item in DATA_product:
                    Stock = item["Stock"]
                    total_inventory += Stock
                
                print("inventory.json found.")
                print("Inventory loaded successfully.")
                print("")

                return products,total_inventory

        except FileNotFoundError:
            with open('inventory.json','w') as file:
                print("No existing inventory, new inventory Created. ")

                self.save_inventory([])
                return [],0


    def save_inventory(self,LISTofITEMS):

        data = [
            Product.to_dict() for Product in LISTofITEMS
        ]

        with open(self.__filename, 'w') as file:
            json.dump(data, file, indent=4)   
            print("Inventory saved successfully. ")





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

    option_num = input("Choose Option(1-6):  ")
    if option_num.isdigit() == False:
        print("Please select a number. ")
        return None
    if option_num not in range(1,6):
        print("Please choose a number in range")
        return None

    return int(option_num)


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
            print(f"ID: {ID} | Name: {item['Name']} | Price: {item['Price']} | Stock: {item['Stock']}")
            print("------------------------------------------")
            return ID
    print("Product not found.")
    return None




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


# while True:

#     if DATA_product == []:
#         DATA_product,total_inventory = load_inventory()
#     task = Menu_OPERATIONS(display_menu())

#     if task == "quit":
#         break
#     if task == "continue":
#         continue

#     print("")
    
file_handler = File_Handling()

products, total_inventory = file_handler.load_inventory()

# Save the list of Product objects
file_handler.save_inventory(products)
