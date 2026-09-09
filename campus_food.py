class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Customer:
    def __init__(self, name):
        self.name = name


class Order:
    menu = [
        MenuItem("Burger", 350),
        MenuItem("Pizza", 450),
        MenuItem("Fries", 150),
        MenuItem("Milkshake", 200),
    ]

    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def show_menu(self):
        print("\nMENU")
        for i, item in enumerate(self.menu, 1):
            print(f"{i}. {item.name}: KSh {item.price}")

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total

    def show_order(self):
        print(f"\nCustomer: {self.customer.name}")
        print("Items Ordered:")
        if not self.items:
            print("  (No items ordered yet)")
        else:
            for item in self.items:
                print(f"  - {item.name}: KSh {item.price}")
        print(f"Total: KSh {self.calculate_total()}")


Customer_name = input("Enter your name: ")
customer = Customer(Customer_name)

order1 = Order(customer)

order1.show_menu()

print("\nWhat would you like to order?")
print("Enter item numbers one at a time (or type 'done' to finish):")

while True:
    choice = input("Enter item number (or 'done' to finish): ")

    if choice.lower() == "done":
        break

    try:
        item_number = int(choice)

        if 1 <= item_number <= len(order1.menu):
            selected_item = order1.menu[item_number - 1]
            order1.add_item(selected_item)
            print(f"✓ Added {selected_item.name} to your order!")
        else:
            print(f"✗ Invalid number! Please choose between 1 and {len(order1.menu)}")

    except ValueError:
        print("✗ Please enter a valid number or 'done'")

order1.show_order()
