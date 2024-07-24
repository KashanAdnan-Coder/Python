# Count Even and Odd Numbers in a List
# Objective: Write a Python program that counts the number of even and odd numbers in a given list.
# Example list
# numbers = [12, 7, 9, 24, 18, 5, 3, 20]


numbers = [12, 7, 9, 24, 18, 5, 3, 20]

x = 0

for num in numbers:
    if num % 2 == 0:
        print(num, "Even number!")
    else : 
        print(num, "Odd number!")