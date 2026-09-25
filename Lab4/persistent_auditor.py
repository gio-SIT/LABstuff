inventory = 0
rejected = 0

def load_inventory():

    with open('inventory.txt','r') as file:
        file.seek(0)
        data = file.read()
    print("-- Current inventory --")
    print("")
    print(data)
    print("")

# def save_inventory():
#     print("Save inventory.")
#     with open('inventory.txt', 'w') as file:
#         file.writelines(orders)

def calculate_tax(amount):
    tax = 0.1*amount
    print("Total Tax Required to Pay: $",tax)
    return tax

def generate_report(current_total, failed_attempts):
    print("")
    print("=== Audit Report ===")
    print("Total Units Processed: ", current_total)
    print("Number of Failed/Rejected Entries: ", failed_attempts)
    calculate_tax(current_total)
    print("")

def process_delivery(current_total, new_value):
    current_total += new_value
    inventory = current_total # Update total inventory units
    print("Current units: ", inventory)
    return current_total

def get_valid_inputs():
    inventoryy = input("Enter Product Name to Order(q or quit to quit): ")

    if inventoryy.lower() == "quit" or inventoryy.lower() == "q":
        generate_report(inventory,rejected)
        return "quit"
    if inventoryy.isdigit() == False:
        print("Error, please input a number")
    
    return inventoryy

while inventory >= 0 and inventory <= 500 :

    load_inventory()
    
    The_input = get_valid_inputs()

    if The_input == "quit":
        break

    if The_input.isdigit() == False:
        rejected += 1
        continue

    if inventory+int(The_input) > 500:
        difference = 500-inventory
        if inventory == 500:
            print("You are at maximum value of 500 units.")
            continue
        print("Stock input will exceed 500, you can only input maximum of" , str(difference) + " units.")
        continue

    inventory = process_delivery(inventory, int(The_input))

else:
    if inventory > 500:
        print("Warning, inventory exceed 500 units. No further inputs allowed.")
        rejected += 1
        generate_report(inventory, rejected)