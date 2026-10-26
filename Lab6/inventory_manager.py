import json

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
        print(f'Name : {self.__product}')
        print(f'Price : ${self.__cost:.2f}') 
        print(f'Stock : {self.__stock}')

    def update_stock(self,quantity):
        if quantity < 0:
            print("Stock cannot be negative")
            return
        self.__stock = quantity

    def get_ID(self):
        return self.__ID

    def get_stock(self):
        return self.__stock

    def get_ALL_product(self):
        return self.__ID , self.__product, self.__cost, self.__stock

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



class Main_Program:

    def __init__(self):
        pass

    def main_menu(self):
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
        option_num = int(option_num)
        if option_num not in range(1,7):
            print("Please choose a number in range")
            return None
 
        if option_num == 1:
            if not products:
                print("No products in inventory.")
            else:
                for product in products:
                    print("")
                    product.display_information()

        if option_num == 2:
            self.add_product(products)

        if option_num == 3:
            self.update_Stock(products)

        if option_num == 4:
            self.search_product(products)

        if option_num == 5:
            # Save the list of Product objects
            file_handler.save_inventory(products)

        if option_num == 6:
            print("Exitting now \n")
            file_handler.save_inventory(products)


    def update_Stock(self,products):
        item, ID = self.search_product(products)
        if item != None:
            item.update_stock(int(input("New stock number here:")))


    def search_product(self,products):
        print("")
        print("Search Product")
        ID = str(input("Enter Product ID: "))
        print("")

        for item in products:
            if item.get_ID() == ID:
                print("Product Found: ")
                print("------------------------------------------")
                item.display_information()
                print("------------------------------------------")
                return item
        print("Product not found.")
        return None, ID


    def add_product(self, products):
        print("\nAdd New Product")

        product_items, search_ID = self.search_product(products)

        # Check if ID already exists
        if product_items != None:
            print("\nUnable to add. Item ID already exists. Returning to Menu. \n")
            return

        NEW_product_name = input("Add New Product Name: ").strip()
        if not NEW_product_name:
            print("Product name cannot be empty.")
            return

        while True:
            try:
                New_price = float(input("Price: "))
                if New_price < 0:
                    print("Price cannot be negative.")
                    continue
                break
            except ValueError:
                print("Please enter a valid price.")

        while True:
            try:
                New_stock = int(input("Stock Quantity: "))
                if New_stock < 0:
                    print("Stock cannot be negative.")
                    continue
                break
            except ValueError:
                print("Please enter a whole number.")

        new_product = Product(
            search_ID,
            NEW_product_name,
            New_price,
            New_stock
        )

        products.append(new_product)
        print("\nProduct added successfully!")
        new_product.display_information()




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

main_menu = Main_Program()
main_menu.main_menu()


main_menu.main_menu()

