class ItemToPurchase:
    def __init__(self, item_name='', item_price=0, item_quantity=0, item_description=None):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.cost = self.item_price * self.item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        print("%s %0.2f @ $%0.2f = $%0.2f" % (self.item_name, self.item_quantity, self.item_price, self.cost))

    def print_item_description(self):
        print("%s: %s" % (self.item_name, self.item_description))

class ShoppingCart:
    def __init__(self, customer_name=None, current_date='January 1, 2016'):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def __get_item_names(self):
        item_names = []
        for item in self.cart_items:
            item_names.append(item.item_name)
        # print(item_names)
        return item_names

    def __check_for_item(self, item_names, search_item):
        # print("Search Item: %s, Item Names: %s" % (search_item, item_names))
        if search_item in item_names:
            return True
        return False

    def __get_index_by_name(self, item_name):
        index = None
        for item in self.cart_items:
            if item_name == item.item_name:
                index = self.cart_items.index(item)
        return index

    def __print_cart_info(self):
        print("\n%s's Shopping Cart - %s" % (self.customer_name, self.current_date))

    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    def remove_item(self, search_item):
        if self.__check_for_item(self.__get_item_names(), search_item):
            self.cart_items.pop(self.__get_index_by_name(search_item))
        else:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, ItemToPurchase):
        item_names = self.__get_item_names()
        if self.__check_for_item(item_names, ItemToPurchase.item_name):
            item_index = item_names.index(ItemToPurchase.item_name)
            if ItemToPurchase.item_description != None:
                self.cart_items[item_index].item_description = ItemToPurchase.item_description
            if ItemToPurchase.item_price != 0:
                self.cart_items[item_index].item_price = ItemToPurchase.item_price
            if ItemToPurchase.item_quantity != 0:
                self.cart_items[item_index].item_quantity = ItemToPurchase.item_quantity
        else:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_items = 0
        for item in self.cart_items:
            total_items += item.item_quantity
        return total_items
    
    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.cost
        return total_cost

    def print_total(self):
        self.__print_cart_info()
        print("Number of Items: %d\n" % self.get_num_items_in_cart())
        for item in self.cart_items:
            item.print_item_cost()
        print("\nTotal: $%0.2f" % self.get_cost_of_cart())

    def print_descriptions(self):
        print()
        for item in self.cart_items:
            item.print_item_description()
