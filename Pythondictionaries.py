inventory = {
    "Laptop": 15,
    "Phone": 8,
    "Headphones": 25,
    "Charger": 5,
    "Monitor": 12
}
print("Initial Inventory:", inventory)

inventory["Keyboard"] = 20
inventory["Phone"] = 10
print("\nAfter adding and updating:", inventory)

def low_stock_products(inv):
    return [product for product, qty in inv.items() if qty < 10]

print("\nProducts with stock less than 10:", low_stock_products(inventory))

del inventory["Charger"]
print("\nAfter removing discontinued product:", inventory)

print("\nFinal Inventory List:")
for product, qty in inventory.items():
    print(product, ":", qty)
