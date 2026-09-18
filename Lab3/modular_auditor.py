inventory = 0
inventoryy = ""
total = 0
rejected = 0

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
    inventoryy = input("Enter stock quantity (or 'quit' to exit.): ").strip()

    if inventoryy.lower() == "quit":
        generate_report(inventory,rejected)
        return "quit"
    if inventoryy.isdigit() == False:
        print("Error, please input a number")
    
    return inventoryy

while inventory >= 0 and inventory <= 500 :
    
    The_input = get_valid_inputs()

    if The_input == "quit":
        break

    if The_input.isdigit() == False:
        rejected += 1
        continue

    if inventory+int(The_input) > 500:
        difference = int(The_input)+inventory-500
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
        