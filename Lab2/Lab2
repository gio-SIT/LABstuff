inventory = 0
inventoryy = ""
total = 0
rejected = 0

def finalreport():
    print("=== Audit Report ===")
    print("Total Units Processed: ", inventory)
    print("Number of Failed/Rejected Entries: ", rejected)

while inventory >= 0 and inventory <= 500 :
    inventoryy = input("Enter stock quantity (or 'quit' to exit.): ").strip()

    if inventoryy.lower() == "quit":
        finalreport()
        break

    if inventoryy.isdigit() == False:
        print("Error, please input a number")
        rejected += 1
        continue

    if 500-int(inventoryy)-inventory < 0:
        difference = -(500-int(inventoryy)-inventory)
        if inventory == 500:
            print("You are at maximum value of 500 units.")
            continue

        print("Stock input will exceed 500, you can only input maximum of" , str(difference) + " units.")
        continue

    inventory += int(inventoryy)
    print("Current units: ", inventory)

    if inventory > 500:
        print("Warning, inventory exceed 500 units. ")
        rejected += 1
        finalreport()
        break
