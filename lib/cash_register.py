#!/usr/bin/env python3

class CashRegister:
  pass

class CashRegister:
    """A simple cash register that can add items, apply a discount,
    and void the most recent transaction."""

    def __init__(self, discount=0):
        # discount goes through the @discount.setter below, so it gets
        # validated even when it's set for the first time here.
        self.discount = discount

        self.total = 0                  # running total price of everything in the register
        self.items = []                 # flat list of item names currently "in" the register
        self.previous_transactions = [] # history of add_item() calls, used for undo

    @property
    def discount(self):
        # Getter just hands back the stored value.
        return self._discount

    @discount.setter
    def discount(self, value):
        # A property lets us run validation every time someone does
        # register.discount = something, instead of trusting the caller.
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity):
        # Total cost of this line = unit price * how many they're buying.
        line_total = price * quantity
        self.total += line_total

        # Track the item itself so self.items mirrors what's in the register.
        self.items.append(item)

        # Save everything needed to reverse this exact action later.
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity,
        })

    def apply_discount(self):
        # discount is stored as a whole-number percent (e.g. 20 == 20%),
        # so divide by 100 to turn it into a fraction before applying it.
        self.total -= self.total * (self.discount / 100)

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There is no transaction to voidnp.")
            return

        # Pull the most recent transaction back off the history...
        last_transaction = self.previous_transactions.pop()

        # ...undo its effect on the total...
        self.total -= last_transaction["price"] * last_transaction["quantity"]

        # ...and remove the matching item so self.items stays in sync.
        self.items.remove(last_transaction["item"])