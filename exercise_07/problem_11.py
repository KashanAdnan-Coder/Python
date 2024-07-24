# Write function that accepts different values as parameters and returns a list
# consider the below varables
# a = 4
# b = 8
# c = 10
# d = 12
# pass above values to the function and return the list
# output: [4, 8, 10, 12]

a = 4
b = 8
c = 10
d = 12

list = []

def return_list (a, b, c, d) :
    list.append(a)
    list.append(b)
    list.append(c)
    list.append(d)
    print(list)

return_list(a,b,c,d)
