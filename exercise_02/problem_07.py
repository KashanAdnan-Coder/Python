# problem 7
"""
Problem: Ask the user to input two numbers. 
Calculate their average 
and print the average rounded to 2 decimal places.

NOTE: Concepts Covered: round(), input(), print(), type casting
"""
first_number = int(input("Enter the first nubmer: "))
second_number = int(input("Enter the second nubmer: "))

average = (first_number + second_number)  / 2

round_average = round(average)
print(round_average)