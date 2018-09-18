auto_services = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7}

desired_service = input("Enter desired auto service:\n")
print("You entered:", desired_service)
if desired_service in auto_services:
    print("Cost of %s: $%d" % (desired_service.lower(), auto_services[desired_service]))
else:
    print("Error: Requested service is not recognized")
