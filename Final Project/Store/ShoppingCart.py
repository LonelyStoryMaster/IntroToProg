class Cart:
    def __init__(self):
        self.items = []
        self.total_item_count = 0
        self.total_cost = 0.0
    
    def count_total_items(self):
        for item in self.items:
            self.total_cost += item.price