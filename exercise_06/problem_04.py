"""
consider the list of dicts
book_list = [{"name": "The Great Gatsby", "quantity": 4}, {"name": "1984", "quantity": 6}, {"name": "To Kill a Mockingbird", "quantity": 3}, {"name": "Moby Dick", "quantity": 2}]
Write a for loop to assign one more detail "stock" based on the number of copies available:
Copies >= 5: "Popular"
Copies >= 3 and < 5: "Available"
Copies < 3: "Limited"
Store these stock categories in a same dict i.e book_list.
"""
book_list = [
    {"name": "The Great Gatsby", "quantity": 4},
    {"name": "1984", "quantity": 6},
    {"name": "To Kill a Mockingbird", "quantity": 3},
    {"name": "Moby Dick", "quantity": 2}
]

for book in book_list:
    if book["quantity"] >= 5:
        book["stock"] = "Popular"
    elif 3 <= book["quantity"] < 5:
        book["stock"] = "Available"
    else:
        book["stock"] = "Limited"

print(book_list)
