# 9. consider the list ['hi', 'hello', 'hi', 'good morning', 'hi', 'bye']
# use for loop and find the count that how many times the word "hi" present in list.
# output should be 3


list =  ['hi', 'hello', 'hi', 'good morning', 'hi', 'bye']
l1 = []
for i in list:
    if i == "hi":
        l1.append(i)


print(len(l1))