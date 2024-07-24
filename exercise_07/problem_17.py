"""
Take a variable store i.e
Store = {“name”: “my store”, “inventory”: [], “orders”: []}

Add 5 items in the inventory using a function “add_item”
id, name, price and quantity

Take user input unless it says “done”
Display user updated inventory items every time
Ask user to type id of the item to purchase or type “done” to checkout
Each time only 1 quantity will by subtracted from the item

Functions: add_item_in_inventory, add_item_in_basket(), checkout()
On checkout, print “{quantity} {item} sold in {store}”
"""
def add_item_in_inventory(store, item_id, item_name, item_price, item_quantity):
    item = {
        "id": item_id,
        "name": item_name,
        "price": item_price,
        "quantity": item_quantity
    }
    store["inventory"].append(item)

def add_item_in_basket(store, item_id):
    for item in store["inventory"]:
        if item["id"] == item_id:
            if item["quantity"] > 0:
                item["quantity"] -= 1
                store["orders"].append(item)
                print(f"Added {item['name']} to the basket. Remaining quantity: {item['quantity']}")
                return
            else:
                print("Item is out of stock.")
                return
    print("Item not found.")

def checkout(store):
    item_counts = {}
    for item in store["orders"]:
        if item["name"] in item_counts:
            item_counts[item["name"]] += 1
        else:
            item_counts[item["name"]] = 1
    for item_name, quantity in item_counts.items():
        print(f"{quantity} {item_name} sold in {store['name']}")
    store["orders"].clear()

# Initialize the store
store = {
    "name": "my store",
    "inventory": [],
    "orders": []
}

# Adding 5 items to the inventory
add_item_in_inventory(store, 1, "apple", 10, 100)
add_item_in_inventory(store, 2, "banana", 5, 50)
add_item_in_inventory(store, 3, "orange", 8, 75)
add_item_in_inventory(store, 4, "milk", 15, 30)
add_item_in_inventory(store, 5, "bread", 20, 25)

# Displaying initial inventory
print("Initial Inventory:")
for item in store["inventory"]:
    print(item)

# Taking user input for purchases
while True:
    user_input = input("Enter the id of the item to purchase or type 'done' to checkout: ")
    if user_input.lower() == "done":
        break
    else:
        try:
            item_id = int(user_input)
            add_item_in_basket(store, item_id)
            print("Updated Inventory:")
            for item in store["inventory"]:
                print(item)
        except ValueError:
            print("Invalid input. Please enter a valid item id or 'done'.")

# Checkout
checkout(store)
