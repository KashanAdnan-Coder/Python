# 2. create a list from 0 to 100 using range function and iterate over the list
# display the number that satisfied following conditions
# The number must be divisible by 5
# If the number is greater than 30 and less than 50 then skip it
# If the number is greater than 80, then stop the loop


lists = []


for i in range(0, 101):
    if i > 80:
        break
    if i  > 30 and i < 50:
        continue
    if i % 5 == 0:
        lists.append(i)

print(lists)