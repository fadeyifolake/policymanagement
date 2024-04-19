class ProductManagement:
    def __init__(self):
        self.products = {}  # Dictionary to store product information

    def create_product(self, product_id, name, description, premium):
        if product_id not in self.products:
            self.products[product_id] = {"name": name, "description": description, "premium": premium, "status": "Active"}
            return True
        else:
            print("Product with the same ID already exists.")
            return False

    def update_product(self, product_id, name=None, description=None, premium=None):
        if product_id in self.products:
            if name:
                self.products[product_id]["name"] = name
            if description:
                self.products[product_id]["description"] = description
            if premium:
                self.products[product_id]["premium"] = premium
            return True
        else:
            print("Product not found.")
            return False

    def suspend_product(self, product_id):
        if product_id in self.products:
            self.products[product_id]["status"] = "Suspended"
            return True
        else:
            print("Product not found.")
            return False

    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            return True
        else:
            print("Product not found.")
            return False

    def display_product_details(self, product_id=None):
        if product_id is None:
            return self.products
        else:
            if product_id in self.products:
                return {product_id: self.products[product_id]}
            else:
                return None