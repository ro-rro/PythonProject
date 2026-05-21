# Object-Oriented Programming
# 10.1 Assignment: Cash Register
# Rosie Navarro
# May 20 2026

import locale

products = {
    "1": ("Apple", .99),
    "2": ("Banana", .99),
    "3": ("Bread", 1.50),
    "4": ("Pasta", 2.50),
    "5": ("Chicken", 8.00),
    "6": ("Eggs", 4.99),
    "7": ("Cheese", 5.50),
    "8": ("Tomato", .85),
    "9": ("Tea", 1.00),
    "10": ("Soda", 10.00)
}

def welcome_message():
    """
    Welcome message to the user.
    Explains that they need to add a numeric value or e to exit the store.
    """

    print("Welcome to the online store!")
    print("For items that you want to purchase place them into your cart.")
    print("If you are finished shopping please click 'e' to checkout.")
    print("=" *50)


def display_products():
    """
    Displays the products and their price, with an item number
    """
    print("\n Product Menu:")
    for key, (name, price) in products.items():
        formatted_price = locale.currency(price, grouping=True)
        print(f"{key}. {name}: {formatted_price}")
    print("="*70)


class CashRegister:
    """
    Class to Stimulate a cash register for an online store.
    Tracks the number of items added and the total price.
    Getter methods to retrieve the item count and total price.
    """

    def __init__(self):
        self.total_price = 0
        self.item_count = 0 # number of items added to the cart

    def add_item(self, price):
        self.total_price += price # adds price to the total
        self.item_count += 1 # item counter

    def get_total(self):
        return self.total_price

    def get_item_count(self):
        return self.item_count


def main():
    """
    Entry to the cash register program.
    Displays the welcome message and tells to user to input values
    Prints the total item count and total price at checkout
    """

    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8') # currency formating

    welcome_message()
    display_products()


    register = CashRegister() # cash register class
    cart = []

    while True:

        user_choice = input("Entre an item or 'e' to finish shopping:").lower()

        if user_choice == "e": # Exit for the user
            break

        if user_choice in products:
            name, price = products[user_choice]
            register.add_item(price)
            cart.append((name, price))
            formatted_price = locale.currency(register.get_total(), grouping=True)
            print(f"\n '{name}' was added to your cart")
        else:
            print(f"\n Invalid please enter a number from the menu")


    print("="*70)
    print("receipt: ")# start of receipt for user
    print(f"Total number of items: {register.get_item_count()}")
    total_price = locale.currency(register.get_total(), grouping=True)
    print(f"Total price: {total_price}")
    print("Thank you for shopping at our online store!! :)")



if __name__ == "__main__":
    main()