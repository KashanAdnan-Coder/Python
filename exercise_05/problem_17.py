# Find Common Elements Between Two Lists
# Objective: Write a Python program that finds and prints the common elements between two lists.
# Example lists
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]


for list in list1:
    if list in list2:
        print(f"The common number on the both list is: {list}")