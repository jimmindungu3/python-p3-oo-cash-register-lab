#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        # Initialize CashRegister with optional discount
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, title, price, quantity=1):
        # Add items to the register, considering quantity
        self.total += price * quantity
        self.items.extend([title] * quantity)

    # Updated apply_discount method
    def apply_discount(self):
        # Apply discount to the total
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            # Ensure the printed total has two decimal places
            print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        # Void the last transaction by subtracting the last item's price from the total
        if self.items:
            last_item_price = self.items.pop()
            self.total -= last_item_price
        else:
            print("No transactions to void.")
