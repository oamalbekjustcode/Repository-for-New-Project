class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append({'product': product, 'quantity': quantity})

    def display_cart(self):
        print("Shopping Cart:")
        for item in self.items:
            print(f"{item['product'].name} - Quantity: {item['quantity']}")

    def calculate_total(self):
        total_cost = sum(item['product'].price * item['quantity'] for item in self.items)
        return total_cost
