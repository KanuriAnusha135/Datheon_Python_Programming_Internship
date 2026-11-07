
class Inventory:

    def __init__(self):
        self.products = {}

    # Add a new product
    def add_product(self):
        name = input("Enter product name: ").strip()

        if not name:
            print("Product name cannot be empty!")
            return

        if name in self.products:
            print("Product already exists!")
            return

        try:
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))

            if quantity < 0 or price < 0:
                print("Quantity and price cannot be negative!")
                return

            self.products[name] = {
                "quantity": quantity,
                "price": price
            }

            print("Product added successfully!")

        except ValueError:
            print("Please enter valid numbers!")

    # View all products
    def view_products(self):
        if not self.products:
            print("Inventory is empty!")
            return

        print("\n===== PRODUCT LIST =====")

        for name, details in self.products.items():
            print("Product:", name)
            print("Quantity:", details["quantity"])
            print("Price: Rs.", details["price"])
            print("----------------------")

    # Update product stock
    def update_stock(self):
        name = input("Enter product name: ").strip()

        if name not in self.products:
            print("Product not found!")
            return

        try:
            quantity = int(input("Enter new quantity: "))

            if quantity < 0:
                print("Quantity cannot be negative!")
                return

            self.products[name]["quantity"] = quantity
            print("Stock updated successfully!")

        except ValueError:
            print("Please enter a valid quantity!")

    # Delete a product
    def delete_product(self):
        name = input("Enter product name: ").strip()

        if name in self.products:
            del self.products[name]
            print("Product deleted successfully!")
        else:
            print("Product not found!")


# Main program
inventory = Inventory()

while True:

    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Stock")
    print("4. Delete Product")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        inventory.add_product()

    elif choice == "2":
        inventory.view_products()

    elif choice == "3":
        inventory.update_stock()

    elif choice == "4":
        inventory.delete_product()

    elif choice == "5":
        print("Thank you for using Inventory Management System!")
        break

    else:
        print("Invalid choice! Please try again.")
