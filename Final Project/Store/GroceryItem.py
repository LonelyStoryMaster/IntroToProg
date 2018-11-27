class GroceryItem:
    """
    Enter True for count_by_lb if item is priced by lb otherwise it will be priced by quantity
    """
    def __init__(self, name='none', cost_by_lb=0.0, cost_by_count=0.0, weight=0.0, quantity=0.0, count_by_lb=False):
        self.name = name
        self.weight = weight
        self.cost_by_count = cost_by_count
        self.cost_by_lb = cost_by_lb
        self.weight = weight
        self.quantity = quantity
        self.price = 0.0
        self.count_by_lb = count_by_lb

        # Calculating price
        self.calc_price()

    def calc_price(self):
        if self.count_by_lb:
            self.price = self.cost_by_lb * self.weight
        else:
            self.price = self.quantity * self.cost_by_count
    
    def __str__(self):
        if self.count_by_lb:
            return ("%0.2flb(s) of %s @ $%0.2f/lb = $%0.2f" % (self.weight, self.name, self.cost_by_lb, self.price))
        else: 
            return ("%d %s(s) @ $%0.2f = $%0.2f" % (self.quantity, self.name, self.cost_by_count, self.price))