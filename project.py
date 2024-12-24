class Person:
    def __init__(self, name, email=None, address=None):
        self.name = name
        self.email = email
        self.address = address

class Customer(Person):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)
        self.balance = 0
        self.orders = []

    def view_menu(self, menu):
        print("\n")
        print("---Restaurant Menu---")
        for item, price in menu.items():
            print(f"{item}: ${price}")

    def place_order(self, menu):
        items = input("Enter the items you want to orders: ").split(',')
        items = [item.strip() for item in items] 
        total_cost = sum(menu[item] for item in items if item in menu)
        if total_cost > self.balance:
            print("Insufficient balance. Please add balance.")
        else:
            self.balance=self.balance-total_cost
            self.orders.append(items)
            print("Order placed successfully.")

    def check_balance(self):
        print(f"Available balance: ${self.balance}")

    def view_past_orders(self):
        print("\n")
        print("Past Orders:")
        for i, order in enumerate(self.orders, start=1):
            print(f"Order {i}: {', '.join(order)}")

    def add_funds(self):
        amount = float(input("Enter the amount to add: "))
        if amount > 0:
            self.balance += amount
            print(f"${amount} added to balance.")
        else:
            print("Amount must be greater than 0.")

class Admin(Person):
    def __init__(self, name):
        super().__init__(name)

    def add_customer(self, customers):
        name = input("Enter customer name: ")
        email = input("Enter customer email: ")
        address = input("Enter customer address: ")
        customer = Customer(name, email, address)
        customers.append(customer)
        print(f"Customer {name} added successfully.")

    def view_customers(self, customers):
        print("\n")
        print("---Customer List---")
        for i, customer in enumerate(customers, start=1):
            print(f"{i}. Name: {customer.name}, Email: {customer.email}, Address: {customer.address}")

    def remove_customer(self, customers):
        email = input("Enter the email of the customer to remove: ")
        for customer in customers:
            if customer.email == email:
                customers.remove(customer)
                print(f"Customer {customer.name} removed successfully.")
                return
        print("Customer not found.")

    def modify_menu(self, menu):
        action = input("Enter action (add/remove/update): ").lower()
        if action == "add":
            item = input("Enter item name: ")
            try:
                price = float(input("Enter item price: "))
                menu[item] = price
                print(f"{item} added to menu at ${price}.")
            except ValueError:
                print("Invalid price.")

        elif action == "remove":
            item = input("Enter item name to remove: ")
            if item in menu:
                del menu[item]
                print(f"{item} removed from menu.")
            else:
                print(f"{item} not found in menu.")

        elif action == "update":
            item = input("Enter item name to update: ")
            if item in menu:
                try:
                    price = float(input("Enter new price: "))
                    menu[item] = price
                    print(f"{item} updated to ${price}.")
                except ValueError:
                    print("Invalid price.")
            else:
                print(f"{item} not found in menu.")
        else:
            print("Invalid action.")

class Restaurant:
    def __init__(self):
        self.menu = {}
        self.customers = []

    def show_menu(self):
        print("\n")
        print("---Restaurant Menu---")
        for item, price in self.menu.items():
            print(f"{item}: ${price}")

    def check_customer_details(self):
        for i, customer in enumerate(self.customers, start=1):
            print(f"Customer {i}: {customer.name}, Email: {customer.email}, Address: {customer.address}, Balance: ${customer.balance}")

if __name__ == "__main__":
    restaurant = Restaurant()
    admin = Admin("Admin")

    while True:
        print("\n")
        print("---Restaurent Management System---")
        print("1. Admin Login")
        print("2. Customer Login")
        print("3.Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            admin_name = input("Enter admin name to login: ")
            if admin_name == admin.name:
                while True:
                    print("\n")
                    print("--Welcome Admin--")
                    print("--Admin Menu--")
                    print("1. Create Customer Account") 
                    print("2. Remove Customer Account")
                    print("3. View All Customers")
                    print("4. Modify Menu")
                    print("5. Show Menu")
                    print("6. Exit")
                    admin_choice = input("Enter your choice: ")

                    if admin_choice == "1":
                        admin.add_customer(restaurant.customers)
                    elif admin_choice == "2":
                        admin.remove_customer(restaurant.customers)
                    elif admin_choice == "3":
                        admin.view_customers(restaurant.customers)
                    elif admin_choice == "4":
                        admin.modify_menu(restaurant.menu)
                    elif admin_choice == "5":
                        restaurant.show_menu()
                    elif admin_choice == "6":
                        break 
                    else:
                        print("Invalid choice.")
            else:
                print(f"Invalid admin name. Please enter the correct name.")

        elif choice == "2":
            if not restaurant.customers:
                print("No customers available. Please ask the admin to add a customer.")
                continue

            name = input("Enter Customer Username: ")
            email = input("Enter cuatomer Useremail: ")
            customer = next((c for c in restaurant.customers if c.name == name and c.email == email), None)

            if customer:
                while True:
                    print("\n")
                    print(f"--{customer.name} Menu--")
                    print("1. View Restaurent Menu")
                    print("2. Add Banlance")
                    print("3. Place Order")
                    print("4. View Balance")
                    print("5. View Past Orders")
                    print("6. Exit")
                    customer_choice = input("Enter your choice: ")

                    if customer_choice == "1":
                        customer.view_menu(restaurant.menu)
                    elif customer_choice == "2":
                        customer.add_funds()
                    elif customer_choice == "3":
                        customer.place_order(restaurant.menu)
                    elif customer_choice == "4":
                        customer.check_balance()
                    elif customer_choice == "5":
                        customer.view_past_orders()
                    elif customer_choice == "6":
                        break
                    else:
                        print("Invalid choice.")
            else:
                print("Invalid name or email.")

        elif choice == "3":
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")
