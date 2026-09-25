inventory = 0
rejected = 0
DATA_product = []

def load_inventory():

    try:
        with open('Lab4/inventory.txt','r') as file:
            print("-- Current inventory --")
            print("")
            DATA_product = [line.strip().split(',') for line in file]
            print(DATA_product)
            print("")
            return DATA_product

    except FileNotFoundError:
        with open('Lab4/inventory.txt','w') as file:
            print("New inventory Created. ")
            return []

    

def save_inventory(LISTofITEMS):
    print("Saved inventory.")
    with open('Lab4/inventory.txt', 'w') as file:
        for item in LISTofITEMS:
            file.write(",".join(item))
            file.write("\n")

def calculate_tax(amount):
    tax = 0.1*amount
    print("Total Tax Required to Pay: $",tax)
    return tax

def generate_report(current_total, failed_attempts):
    print("")
    print("=== Audit Report ===")
    print("Number of Failed/Rejected Entries: ", failed_attempts)
    calculate_tax(current_total)
    print("")

def process_delivery(current_total, new_value):
    current_total += new_value
    inventory = current_total # Update total inventory units
    print("Current units: ", inventory)
    return current_total

def get_valid_inputs():
    Product_Name = input("Enter Product Name to Order(q or quit to quit): ")
    if Product_Name.lower() == "quit" or Product_Name.lower() == "q":
        
        return "quit","quit"

    inv_quantity = input("Enter Quantity (q or quit to quit): ").strip()

    if inv_quantity.lower() == "quit" or inv_quantity.lower() == "q":
        generate_report(inventory,rejected)
        return "quit","quit"
    if inv_quantity.isdigit() == False:
        print("Error, please input a number")
    
    return Product_Name,inv_quantity


while True:

    DATA_product = load_inventory()
    
    Product_Name,inv_quantity = get_valid_inputs()

    if Product_Name == "quit" or inv_quantity == "quit":
        generate_report(1,rejected)
        break

    if inv_quantity.isdigit() == False:
        rejected += 1
        continue

    iteration = 0
    for items in DATA_product:
        print(items)
        if items[1].lower().replace(" ","") == Product_Name.lower().replace(" ",""):
            DATA_product[iteration][2] = str(int(inv_quantity)+int(items[2]))
            save_inventory(DATA_product)
        iteration += 1
        print(DATA_product, "66666666666666666666666666666666666666")
        #note make all variation of product names all work.
    print("")
    
    
