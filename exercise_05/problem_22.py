# 4. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements using for loop. Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'] Expected Output : ['Green', 'White', 'Black']

lists = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
filtered_list = []

for index,i in enumerate(lists):
    if index not in  [0,4,5]:
        filtered_list.append(i)

    
print(filtered_list)