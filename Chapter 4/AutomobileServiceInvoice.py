auto_services = {"Oil change": 35, "Tire rotation": 19, "Car wash": 7, "Car wax": 12}

print("Davy's auto shop services")
for service in auto_services:
    print("%s -- $%d" % (service, auto_services[service]))
    
selection_one = input("\nSelect first service:\n")
selection_two = input("Select second service:\n")

print("\nDavy's auto shop invoice\n")

if selection_one == '-':
    selection_one_price = 0
    print("Service 1: No service")
else:
    selection_one_price = auto_services[selection_one]
    print("Service 1: %s, $%d" % (selection_one, selection_one_price))

if selection_two == '-':
    selection_two_price = 0
    print("Service 2: No service")
else:
    selection_two_price = auto_services[selection_two]
    print("Service 2: %s, $%d" % (selection_two, selection_two_price))
