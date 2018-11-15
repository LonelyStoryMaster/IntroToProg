class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.cost = self.item_price * self.item_quantity
        self.item_description = item_description
        self.attributes = ['Item Name', 'Item Description', 'Item Price', 'Item Quantity']
        self.saves = {'name': self.item_name, 'desc': self.item_description, 'price': self.item_price, 'quantity': self.item_quantity}

    def print_item_cost(self):
        print("%s %0.2f @ $%0.2f = $%0.2f" % (self.item_name, self.item_quantity, self.item_price, self.cost))

    def print_item_description(self):
        print("%s: %s" % (self.item_name, self.item_description))