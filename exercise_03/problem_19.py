"""
Write a program that takes a person's age as input and prints the age group they belong to:

If the age is less than 13, print "Child".
If the age is between 13 and 19 (inclusive), print "Teenager".
If the age is 20 or above:
    If the age is less than 65, print "Adult".
    If the age is 65 or above, print "Senior".
"""

age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif age > 13 and age < 19:
    print("Teenager")
elif age > 20 and age < 65:
    print("Adult") 
elif age > 65:
    print("Senior")