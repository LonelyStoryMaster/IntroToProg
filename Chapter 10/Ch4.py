auto_services = {"Oil change": 35, "Tire rotation": 19, "Car wash": 7, "Car wax": 12}
selections = {"Service 1": '', "Service 2": ''}
total = 0

print("Davy's auto shop services")
for service in auto_services:
    print("%s -- $%d" % (service, auto_services[service]))
    
selections["Service 1"] = input("\nSelect first service:\n")
selections["Service 2"] = input("Select second service:\n")

print("\nDavy's auto shop invoice\n")

for selection in selections:
    if selections[selection] == '-':
        print("%s: No service" % selection)
    else:
        price = 0.0
        try:
            price = auto_services[selections[selection]]
        except KeyError:
            print("\nService was not recognized")
            print("%s: No service" % selection)
        else:
            print("%s: %s, $%d" % (selection, selections[selection], price))
        total += price
              
print("\nTotal: $%d" % total)
