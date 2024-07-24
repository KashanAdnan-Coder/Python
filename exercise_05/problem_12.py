# 8. Write a Python program to get the largest number from a list and use for loop consider the list [3, 5, 2, 1, 4]
# output should be 5
# hint:
# create a variable x outside the loop and assign the value 0
# inside the loop compare the variable x with the local variable of loop


l1 = [3, 5, 2, 1, 4]

x = 0

for i in l1:
    if i > x:
     x = i

print("the largest number is:" ,x)