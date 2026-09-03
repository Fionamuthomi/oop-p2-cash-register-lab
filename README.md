# Cash Register

A simple Python OOP project that models a cash register for an e-commerce
site. Built to practice class design, properties/decorators, and managing
object state over a sequence of actions.

## What it does

The `CashRegister` class lets you add items with a price and quantity,
apply a percentage discount to the total, and void the last transaction
if needed.

- `discount` — percentage off the total (e.g. `20` means 20% off). Defaults
  to `0`, and only accepts integers between 0 and 100.
- `total` — running total price of everything added. Starts at `0`.
- `items` — list of item names currently in the register.
- `previous_transactions` — history of items added, used to support voiding.

### Methods

- `add_item(item, price, quantity)` — adds the item to the register and
  updates the total.
- `apply_discount()` — applies the current discount percentage to the total.
- `void_last_transaction()` — undoes the most recent `add_item()` call.

## Usage

```python
from cash_register import CashRegister

register = CashRegister()

register.add_item("apple", 2, 3)   # 3 apples at $2 each
register.add_item("bread", 5, 1)   # 1 loaf of bread at $5

register.discount = 20
register.apply_discount()          # 20% off the current total

register.void_last_transaction()   # undoes the last add_item()
```