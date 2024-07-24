# Create a List of Even Numbers from 1 to 20
# Objective: Write a Python program that creates a list of all even numbers from 1 to 20.

list = []

for i in range(0, 20):
    if (i + 1) % 2 == 0:
        list.append(i+1)

print(list)