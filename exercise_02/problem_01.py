# problem 1
"""
Problem Statement:

Prompt the user to enter a float number.
Use the round() function to round the number to 2 decimal places.
Print the original number and the rounded number.
Use the len() function to find the length of a string entered by the user and print the result.
"""

float_number = float(input("Enter a float number : "))
print("Float Number" , float_number , "Rounded Number" , round(float_number) )
print("The length of the float number is =", len(str(float_number)))