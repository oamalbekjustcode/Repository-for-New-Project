from shopping_cart import ShoppingCart

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cart = ShoppingCart()

    def add_to_cart(self, product, quantity):
        self.cart.add_item(product, quantity)

    def view_cart(self):
        self.cart.display_cart()

    def checkout(self):
        total_cost = self.cart.calculate_total()
        print(f"Checkout completed. Total cost: ${total_cost}")
