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
            product.to_dict() for product in LISTofITEMS
        ]

        with open(self.__filename, 'w') as file:
            json.dump(data, file, indent=4)   
            print("Inventory saved successfully. ")



class Main_Program:

    def __init__(self,inventory, file_handler):
        self.__inventory = inventory
        self.__file_handler = file_handler

    def main_menu(self):
        while True:
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
                self.__inventory.display_products()

            if option_num == 2:
                self.__inventory.add_product()

            if option_num == 3:
                self.__inventory.update_Stock()

            if option_num == 4:
                self.__inventory.search_product()

            if option_num == 5:
                # Save the list of Product objects
                file_handler.save_inventory(products)

            if option_num == 6:
                print("Exitting now \n")
                file_handler.save_inventory(products)



class Inventory:
    def __init__(self):
        self.__products = []

    def load_products(self,products):
        self.__products = products

    def get_products(self):
        return self.__products

    def display_products(self) -> None:
        if not self.__products:
            print("No products  in inventory.")
            return

        print("----------Current Inventory---------")
        for product in self.__products:
            ID, name, price, stock = product.get_ALL_product()
            print(f'ID : {ID}')
            print(f'Name : {name}')
            print(f'Price : ${price:.2f}') 
            print(f'Stock : {stock}\n')

    def search_product(self):
            print("")
            print("Search Product")
            ID = str(input("Enter Product ID: ")).strip()
            print("")
    
            for item in self.__products:
                if item.get_ID() == ID:
                    print("Product Found: ")
                    print("------------------------------------------")
                    ID, name, price, stock = item.get_ALL_product()
                    print(f"ID: {ID}")
                    print(f"Name: {name}")
                    print(f"Price: ${price:.2f}")
                    print(f"Stock: {stock}")
                    print("------------------------------------------")
                    return item, ID
            print("Product not found.")
            return None, ID

    def update_Stock(self):
        item, ID = self.search_product()
        if item is None:
            print("Product ID not found.")
            return
        
        item.update_stock(int(input("Put new stock value here: ")))

    def add_product(self):
            print("\nAdd New Product")
    
            product_items, search_ID = self.search_product()

            if not search_ID:
                print("Product ID cannot be empty.")
                return

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
            self.display_products()



if __name__ == "__main__":

    file_handler = File_Handling()
    products, total_inventory = file_handler.load_inventory()

    inventory = Inventory()
    inventory.load_products(products)

    main_menu = Main_Program(inventory, file_handler)
    main_menu.main_menu()


