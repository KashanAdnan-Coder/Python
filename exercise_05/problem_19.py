# 1. Write a Python program to multiply all the items in a list and use for loop. consider the list [3, 5, 2, 1, 4].
# output should be 360
# hint: use a variable x outside the loop and assign the first value of list
# inside the loop * the value of x with the local variable of loop
# x *= 

list = [3, 5, 2, 1, 4]
x = 3

for i in list:
    x *= i 

print(x)