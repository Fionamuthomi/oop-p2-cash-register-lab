class CashRegister:
    """Models a cash register: add items, apply a discount, void the
    last sale, and report back what's been rung up."""

    def __init__(self, discount=0):
        # "takes one optional argument, a discount, on initialization"
        self.discount = discount

        # "sets an instance variable total to zero on initialization"
        self.total = 0

        # "sets an instance variable items to empty list on initialization"
        self.items = []

        # keeps the full history of sales, so we can undo them and
        # rebuild an "including multiples" list later on
        self.previous_transactions = []

    def add_item(self, title, price, quantity=1):
        # "accepts a title and a price and increases the total"
        # "also accepts an optional quantity"  -> defaults to 1 above
        # "doesn't forget about the previous total" -> we save it before changing it
        previous_total = self.total
        self.total += price * quantity

        # one entry per sale, NOT multiplied out
        self.items.append(title)

        # everything needed to undo this exact sale later
        self.previous_transactions.append({
            "title": title,
            "price": price,
            "quantity": quantity,
            "previous_total": previous_total,
        })

    def apply_discount(self):
        # "applies the discount to the total price"
        # "prints success message with updated total"
        self.total -= self.total * (self.discount / 100)
        print(f"Discount applied. New total: {self.total}")

    def void_last_transaction(self):
        # "prints a string error message that there is no discount to apply"
        if not self.previous_transactions:
            print("There is no discount to apply.")
            return

        # "subtracts the last item from the total"  -> "reduces the total"
        last_transaction = self.previous_transactions.pop()
        self.items.pop()
        self.total -= last_transaction["price"] * last_transaction["quantity"]

        # "returns the total to 0.0 if all items have been removed"
        if not self.items:
            self.total = 0.0

    def get_items(self):
        # "returns an array containing all items that have been added"
        return self.items

    def get_items_with_multiples(self):
        # "returns an array containing all items that have been added,
        # including multiples" -> e.g. quantity=3 apples becomes
        # ['apple', 'apple', 'apple']
        expanded = []
        for transaction in self.previous_transactions:
            expanded.extend([transaction["title"]] * transaction["quantity"])
        return expanded