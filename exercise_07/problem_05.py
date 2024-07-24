# Write a program and ask user to enter number, 5 times using while loop. store each value in list.
# calculate the sum of all values in a list

num_list = []

x = 0

count = 0
while x < 5:
    x += 1
    num = int(input("Enter any number : "))
    num_list.append(num)

for i in num_list:
    count += i

print(count)