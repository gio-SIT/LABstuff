DATA_product = []
total_inventory = 0
rejected_entry = 0

#add_product(),update_stock(),search_product(),display_all()


def show_tax_inventory(total_inventory):
    tax = 0.1*total_inventory
    print("Tax: $",tax," | Total Inventory: ",total_inventory)
    return tax

def generate_report(current_total, failed_entry):
    print("")
    print("=== Audit Report ===")
    print("Total Transactions Recorded: ", current_total)
    print("Total Units Processed: ", current_total)
    print("Number of Failed/Rejected Entries: ", failed_entry)
    print("")

def load_inventory():
    print("-- Current Orders: --")
    print('')
    try:
        with open('inventory.txt','r') as file:
            total_inventory = 0
            DATA_product = [line.strip().split(',') for line in file]

            for item in DATA_product:
                print(",".join(item))
                total_inventory += int(item[2])
            print('')

            return DATA_product,total_inventory

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
    update_inventory = total_inventory
    for items in DATA_product:
        if items[1].lower().replace(" ","") == Product_Name.lower().replace(" ",""):
            DATA_product[iteration][2] = str(int(inv_quantity)+int(items[2]))
            print("New Order Added:")
            print(DATA_product[iteration])
            print("")
            update_inventory += int(inv_quantity)
            show_tax_inventory(update_inventory)
            save_inventory(DATA_product)

            return update_inventory
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

    DATA_product,total_inventory = load_inventory()

    Product_Name,inv_quantity = get_valid_inputs()

    if Product_Name == "quit" or inv_quantity == "quit":
        generate_report(total_inventory,rejected_entry)
        break

    if inv_quantity.isdigit() == False:
        continue

    total_inventory = process_delivery(DATA_product, Product_Name, inv_quantity)

    print("")
    
    
