#!/usr/bin/env python3

class CashRegister:
    """Models a simple cash register: add items, apply a discount,
    and void the last sale."""

    def __init__(self, discount=0):
        self.discount = discount        # goes through the property setter below
        self.total = 0                  # running total
        self.items = []                 # every item title, repeated per quantity
        self.previous_transactions = [] # history, used to undo the last add_item()

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        # "Ensure discount is an integer. Ensure it's between 0-100 inclusive.
        # If not, print 'Not valid discount'."
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity

        # append the title once for EACH unit bought, so self.items
        # reflects quantities too (e.g. 2 eggs -> ["eggs", "eggs"])
        for _ in range(quantity):
            self.items.append(title)

        self.previous_transactions.append({
            "title": title,
            "price": price,
            "quantity": quantity,
        })

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            # int() keeps the total a whole number when the inputs are
            # whole numbers, so the printed total is $800, not $800.0
            discount_amount = int(0.01 * self.discount * self.total)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        # "If no transactions are in the array, print
        # 'There is no transaction to void.'"
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        last_transaction = self.previous_transactions.pop()
        self.total -= last_transaction["price"] * last_transaction["quantity"]

        # remove as many copies of that title as were added
        for _ in range(last_transaction["quantity"]):
            self.items.pop()