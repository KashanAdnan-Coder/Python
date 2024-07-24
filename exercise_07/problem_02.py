# Write a program that find common values between 2 lists and also tells how many times the common value occurs.
# consider the list l1 = ['a', 'b', 'c', 'd'] and l2 = ['e', 'b', 'g', 'd', 'f', 'h']
# output:
# {"a": 1, "b": 2, "c": 1, "d": 2, "e": 1, "f": 1, "g": 1, "h": 1}
# hint: use nested loop

l1 = ['a', 'b', 'c', 'd'] 
l2 = ['e', 'b', 'g', 'd', 'f', 'h']

common_list = []

for item in l1:
    if item in l2:
        common_list.append(item)


print(common_list)