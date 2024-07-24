"""
Create a dictionary named library_books with the following key-value pairs:
"The Great Gatsby": 4
"1984": 6
"To Kill a Mockingbird": 3
"The Catcher in the Rye": 5
"Moby Dick": 2

1. Write a for loop to add 2 more copies to each book. Update the dictionary accordingly.
2. Write a for loop to calculate the total number of books in the library. Print the total count.
"""

library_books = {
    "The Great Gatsby": 4,
    "1984": 6,
    "To Kill a Mockingbird": 3,
    "The Catcher in the Rye": 5,
    "Moby Dick": 2
}

for book in library_books:
    library_books[book] += 2

print(library_books)

x = 0
for book in library_books:
    x += library_books[book]    

print(x)