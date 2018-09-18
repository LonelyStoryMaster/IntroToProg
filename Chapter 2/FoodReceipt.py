receipt = []
receipt_total = 0.0
item = ['', 0, 0]
item2 = ['', 0, 0]

name = input("Enter food item name:\n")
price = float(input("Enter item price:\n"))
quantity = int(input("Enter item quantity:\n"))

item[0] = name
item[1] = price
item[2] = quantity

receipt.append(item)

print("\nRECEIPT")
for thing in receipt:
    print(thing[2], thing[0], "@ $", thing[1], "= $", thing[2] * thing[1])
    receipt_total += thing[2] * thing[1]
print("Total cost: $", receipt_total)

print('\n')

name = input("Enter second food item name:\n")
price = float(input("Enter item price:\n"))
quantity = int(input("Enter item quantity:\n"))

item2[0] = name
item2[1] = price
item2[2] = quantity

receipt.append(item2)
receipt_total = 0.0

print("\nRECEIPT")
for thing in receipt:
    print(thing[2], thing[0], "@ $", thing[1], "= $", thing[2] * thing[1])
    receipt_total += thing[2] * thing[1]
print("Total cost: $", receipt_total)

receipt_tip = receipt_total * 0.15
receipt_total += receipt_tip

print("15% gratuity: $", receipt_tip)
print("Total with tip: $", receipt_total)
