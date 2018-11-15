import csv, os

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

class ShoppingCart:
    def __init__(self, customer_name="none", current_date='January 1, 2016', save_file_path='save_file.csv'):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

        # For saving the cart in a csv file in the same directory
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        self.save_file_path = os.path.join(__location__, save_file_path)

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

    def __clear_cart(self):
        self.cart_items.clear()

    def save_cart(self):
        with open(self.save_file_path, 'w', newline='') as csvfile:
            cart_writer = csv.writer(csvfile)
            save_item = ItemToPurchase()
            cart_writer.writerow(save_item.attributes)
            for item in self.cart_items:
                current_line = []
                for attribute_value in item.saves.values():
                    current_line.append(attribute_value)
                cart_writer.writerow(current_line)

    def load_save(self):
        if os.path.exists(self.save_file_path):
            self.__clear_cart()
            with open(self.save_file_path, 'r') as csvfile:
                cart_reader = csv.reader(csvfile)
                first_line = True
                for line in cart_reader:
                    if first_line:
                        first_line = False
                        continue
                    new_item = ItemToPurchase(line[0], float(line[2]), float(line[3]), line[1])
                    self.add_item(new_item)
        else:
            print("There is no existing save file found")

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

def print_menu():
    print("\nMENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("s - Save cart contents")
    print("l - Load saved cart contents")
    print("q - Quit")
    menu_op = input("\nChoose an option:\n")
    return menu_op

if __name__ == '__main__':
    name = input("Enter customer's name:\n")
    date = input("Enter today's date:\n")
    print("\nCustomer name: %s\nToday's date: %s" % (name, date))

    new_cart = ShoppingCart(name, date)

    op = print_menu()

    while op != 'q':
        if op == 'o':
            print("\nOUTPUT SHOPPING CART")
            new_cart.print_total()
        elif op == 'i':
            print("\nOUPUT ITEM's DESCRIPTIONS")
            new_cart.print_descriptions()
        elif op == 'a':
            print("\nADD ITEM TO CART\n")
            name = input("Enter the item name:\n")
            description = input("Enter the item description:\n")
            price = float(input("Enter the item price:\n"))
            quantity = int(input("Enter the item quantity:\n"))
            new_item = ItemToPurchase(name, price, quantity, description)
            new_cart.add_item(new_item)
        elif op == 'r':
            print("\nREMOVE ITEM FROM CART\n")
            name = input("Enter name of item to remove:\n")
            new_cart.remove_item(name)
        elif op == 'c':
            print("\nCHANGE ITEM QUANTITY\n")
            name = input("Enter the item name:\n")
            quantity = int(input("Enter the new quantity:\n"))
            modified_item = ItemToPurchase(item_name=name, item_quantity=quantity)
            new_cart.modify_item(modified_item)
        elif op == 's':
            print("\nSAVING CART CONTENTS")
            new_cart.save_cart()
        elif op == 'l':
            print("\nLOADING SAVED CART")
            new_cart.load_save()
        else:
            op = input("\nChoose an option:\n")
        op = print_menu()
    else:
        print("\nGOODBYE. THANKS FOR SHOPPING")