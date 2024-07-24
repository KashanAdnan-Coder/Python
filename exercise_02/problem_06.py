# problem 6
"""
Problem: Create a small program that asks the user for their first name and last name, 
converts them to uppercase, 
replaces spaces with hyphens
and calculates the length of their full name.

print 3 variables i.e
print("Your full name in uppercase is: " + full_name_upper)
print("Modified sentence: " + modified_sentence)
print("The length of your full name is: " + str(full_name_length))

NOTE: Concepts Covered: input(), string methods (upper, replace), len(), print()
"""
full_name = input("Enter your full_name : ")
full_name_upper = full_name.upper()
modified_sentence = full_name.replace(" " , "-")
full_name_length = len(full_name)

print("Your full name in uppercase is: " + full_name_upper)
print("Modified sentence: " + modified_sentence)
print("The length of your full name is: " + str(full_name_length))
