class ItemToPurchase:
    def __init__(self, item_name='', item_price=0, item_quantity=0, item_description=None):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.cost = self.item_price * self.item_quantity
        self.description = item_description

    def print_item_cost(self):
        print("%s %d @ $%d = $%d" % (self.item_name, self.item_quantity, self.item_price, self.cost))