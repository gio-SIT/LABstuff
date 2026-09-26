DATA_product = []

def load_inventory():
    print("-- Current Orders: --")
    print('')
    try:
        with open('inventory.txt','r') as file:
            
            DATA_product = [line.strip().split(',') for line in file]

            for item in DATA_product:
                print(",".join(item))
            print('')

            return DATA_product

    except FileNotFoundError:
        with open('inventory.txt','w') as file:
            print("New inventory Created. ")
            return []

def save_inventory(LISTofITEMS):
    with open('inventory.txt', 'w') as file:
        for item in LISTofITEMS:
            file.write(",".join(item))
            file.write("\n")
    print("Order successfully save to inventory.txt.")

def process_delivery(DATA_product, Product_Name, inv_quantity):
    iteration = 0
    for items in DATA_product:
        if items[1].lower().replace(" ","") == Product_Name.lower().replace(" ",""):
            DATA_product[iteration][2] = str(int(inv_quantity)+int(items[2]))
            print("New Order Added:")
            print(DATA_product[iteration])
            print("")
            save_inventory(DATA_product)

            return
        iteration += 1

    #if product does not exist in current list
    if DATA_product:
        highest_id = max(int(item[0]) for item in DATA_product)
        new_id = highest_id + 1
    else:
        new_id = 1003

    new_item = [str(new_id),Product_Name,str(inv_quantity)]

    DATA_product.append(new_item)

    print("New Product Added: ")
    print(new_item)
    print('')

    save_inventory(DATA_product)
    
    

def get_valid_inputs():
    Product_Name = input("Enter Product Name to Order(q or quit to quit): ")
    if Product_Name.lower() == "quit" or Product_Name.lower() == "q":
        
        return "quit","quit"

    if Product_Name.replace(' ','') == '' or Product_Name == '':
        print("Invalid Product name. Type again. ")
        return "quit","quit"

    inv_quantity = input("Enter Quantity (q or quit to quit): ").strip()

    if inv_quantity.lower() == "quit" or inv_quantity.lower() == "q":
        return "quit","quit"
    if inv_quantity.isdigit() == False or inv_quantity == None:
        print("Error, please input a number")
    
    return Product_Name,inv_quantity


while True:

    DATA_product = load_inventory()
    
    Product_Name,inv_quantity = get_valid_inputs()

    if Product_Name == "quit" or inv_quantity == "quit":
        break

    if inv_quantity.isdigit() == False:
        continue

    process_delivery(DATA_product, Product_Name, inv_quantity)

    print("")
    
    
