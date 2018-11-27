class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.cost = self.item_price * self.item_quantity

    def print_item_cost(self):
        print("%s %d @ $%d = $%d" % (self.item_name, self.item_quantity, self.item_price, self.cost))

if __name__ == '__main__':
    items = []
    for i in range(2):
        print("Item %d" % (i + 1))
        item_name = input("Enter the item name:\n")
        try:
            item_price = int(input("Enter the item price:\n"))
        except ValueError:
            item_price = 0
        try:
            item_quantity = int(input("Enter the item quantity:\n"))
        except ValueError:
            item_quantity = 0
        print()
        new_item = ItemToPurchase(item_name, item_price, item_quantity)
        items.append(new_item)
    print("TOTAL COST")
    items[0].print_item_cost()
    items[1].print_item_cost()
    print("\nTotal: $%d" % (items[0].cost + items[1].cost))