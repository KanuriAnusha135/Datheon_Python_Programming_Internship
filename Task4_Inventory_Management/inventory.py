
from models import Book, Magazine, DigitalMedia


class InventoryManager:

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print("Item added successfully!")

    def remove_item(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                self.items.remove(item)
                print("Item removed successfully!")
                return

        print("Item not found!")

    def display_inventory(self):
        print("\n===== INVENTORY REPORT =====")

        if not self.items:
            print("Inventory is empty!")
            return

        for item in self.items:
            print(item.display_metadata())
            print("Price:", item.price)
            print("Fee:", item.calculate_fee())
            print("----------------------")

        print("Total Items:", len(self.items))
        print("Total Inventory Value:", sum(item.price for item in self.items))

    def __len__(self):
        return len(self.items)


def main():

    inventory = InventoryManager()

    while True:

        print("\n===== SMART INVENTORY SYSTEM =====")
        print("1. Add Book")
        print("2. Add Magazine")
        print("3. Add Digital Media")
        print("4. View Inventory")
        print("5. Remove Item")
        print("6. Exit")

        choice = input("Enter your choice: ")

        try:

            if choice == "1":
                item_id = input("Enter Book ID: ")
                title = input("Enter Book Title: ")
                price = float(input("Enter Book Price: "))
                author = input("Enter Author Name: ")

                inventory.add_item(
                    Book(item_id, title, price, author)
                )

            elif choice == "2":
                item_id = input("Enter Magazine ID: ")
                title = input("Enter Magazine Title: ")
                price = float(input("Enter Magazine Price: "))
                issue = input("Enter Issue Number: ")

                inventory.add_item(
                    Magazine(item_id, title, price, issue)
                )

            elif choice == "3":
                item_id = input("Enter Media ID: ")
                title = input("Enter Media Title: ")
                price = float(input("Enter Media Price: "))
                file_format = input("Enter File Format: ")

                inventory.add_item(
                    DigitalMedia(item_id, title, price, file_format)
                )

            elif choice == "4":
                inventory.display_inventory()

            elif choice == "5":
                item_id = input("Enter Item ID to remove: ")
                inventory.remove_item(item_id)

            elif choice == "6":
                print("Thank you for using Smart Inventory System!")
                break

            else:
                print("Invalid choice! Try again.")

        except ValueError as error:
            print("Invalid input:", error)


if __name__ == "__main__":
    main()