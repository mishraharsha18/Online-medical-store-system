class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, product, quantity):
        self.items.append({"product": product, "quantity": quantity})

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item["product"].price * item["quantity"]
        return total

class MedicalStore:
    def __init__(self):
        self.products = []
        self.shopping_cart = ShoppingCart()

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        print("Available Products:")
        for product in self.products:
            print(f"ID: {product.id}, Name: {product.name}, Price: ${product.price}, Quantity: {product.quantity}")

    def search_product(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product
        return None

    def purchase(self):
        while True:
            self.display_products()
            product_id = int(input("Enter product ID to purchase (0 to exit): "))
            if product_id == 0:
                break
            quantity = int(input("Enter quantity: "))
            product = self.search_product(product_id)
            if product:
                if product.quantity >= quantity:
                    self.shopping_cart.add_to_cart(product, quantity)
                    print("Product added to cart.")
                    product.quantity -= quantity
                else:
                    print("Insufficient stock.")
            else:
                print("Product not found.")

        total = self.shopping_cart.calculate_total()
        print(f"Total amount: ${total}")
        confirm = input("Confirm purchase? (yes/no): ")
        if confirm.lower() == "yes":
            print("Purchase successful.")
            self.shopping_cart = ShoppingCart()  # Clear the shopping cart after purchase
        else:
            print("Purchase cancelled.")

if __name__ == "__main__":
    store = MedicalStore()
    
    # Sample products
    store.add_product(Product(1, "Paracetamol", 5.99, 100))
    store.add_product(Product(2, "Bandages", 3.49, 50))
    store.add_product(Product(3, "Cough Syrup", 7.99, 30))

    while True:
        print("\nWelcome to the Online Medical Store")
        print("1. Purchase Products")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            store.purchase()
        elif choice == "2":
            print("Thank you for visiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
