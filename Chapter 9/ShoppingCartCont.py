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
        self.total_items = 0
        self.total_cost = 0
        self.menu_op = ''
        
    def __count_totals(self):
        self.get_num_items_in_cart()
        self.get_cost_of_cart()

    def __print_cart_info(self):
        print("%s's Shopping Cart - %s" % (self.customer_name, self.todays_date))

    def get_num_items_in_cart(self):
        for item in self.cart_items:
            self.total_items += item.quantity
    
    def get_cost_of_cart(self):
        for item in self.cart_items:
            self.total_cost += item.cost

    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item_name in item.item_name:
                self.cart_items.remove(item)
                break
    
    def modify_item(self, ItemToPurchase):
        pass

    def print_total(self):
        self.__print_cart_info()
        self.__count_totals()
        if self.total_items == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print("Number of Items: %d\n" % self.total_items)
            for item in self.cart_items:
                item.print_item_cost()
            print("\nTotal: $%d" % self.total_cost)

    def print_descriptions(self):
        self.__print_cart_info()
        print("\nItem descriptions")
        for item in self.cart_items:
            item.print_item_description()

    def print_menu(self):
        print("MENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Print items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        self.menu_op = ("\nChoose an option:\n")

if __name__ == '__main__':
    customer_name = input("Enter customer's name:\n")
    date = input("Enter today's date:\n")
    cart = ShoppingCart(customer_name, date)
    print("\nCustomer name: %s\nToday's date: %s" % (cart.customer_name, cart.todays_date))
    while cart.menu_op != 'q':
        cart.print_menu()
        if cart.menu_op == 'q':
            break
        elif cart.menu_op == 'a':
            print("ADD ITEM TO CART")
            item_name = input("Enter the item name:\n")
            item_description = input("Enter the item description\n")
            item_price = int(input("Enter the item price:\n"))
            item_quantity = int(input("Enter the item quantity:\n"))
            new_item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            cart.add_item(new_item)
        elif cart.menu_op == 'r':
            print("REMOVE ITEM FROM CART")
            item = input("Enter name of item to remove:\n")
            cart.remove_item(item)
        elif cart.menu_op == 'c':
            modified_item = ItemToPurchase()
            cart.modify_item(modified_item)
        elif cart.menu_op == 'i':
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
        elif cart.menu_op == 'o':
            print("OUTPUT SHOPPING CART")
            cart.print_total()
    # pass