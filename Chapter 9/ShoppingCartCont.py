class ItemToPurchase:
    def __init__(self, item_name='', item_price=0, item_quantity=0, item_description=None):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.cost = self.item_price * self.item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        print("%s %d @ $%d = $%d" % (self.item_name, self.item_quantity, self.item_price, self.cost))

    def print_item_description(self):
        if self.item_description == None:
            print("There is no description for that item")
        else:
            print("%s: %s" % (self.item_name, self.item_description))

class ShoppingCart:
    def __init__(self, customer_name=None, todays_date='January 1, 2016'):
        self.customer_name = customer_name
        self.todays_date = todays_date
        self.cart_items = []
        
    def add_item(self):
        pass

    def remove_item(self, item_name):
        pass
    
    def modify_item(self):
        pass

    def get_num_items_in_cart(self):
        pass
    
    def get_cost_of_cart(self):
        pass

    def print_total(self):
        pass

    def print_descriptions(self):
        pass

if __name__ == '__main__':
    pass