# problem 5
"""
Write a program that:

Asks the user to enter their full name.
Converts the full name to uppercase and prints it.
Asks the user for their favorite number.
Multiplies the number by 2, converts it to a string, and concatenates it to a message.

Prints the message "Your favorite number multiplied by 2 is X.", where X is the new number.
"""

full_name = input("Enter your full name: ")
print(full_name.upper())
favorite_num = int(input("Enter your favorite number: "))
print("Your favorite number multiplied by 2 is",favorite_num * 2,".\nwhere",favorite_num * 2,"is the new number.")