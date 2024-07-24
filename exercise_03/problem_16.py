"""
Write a program that takes a password as input and checks its strength:

If the password length is less than 6, print "Weak password".
If the password length is between 6 and 12, print "Moderate password".
If the password length is more than 12, print "Strong password".
"""

password = input("Enter your password :: ")

if len(password) <= 6:
    print("Weak password")
elif len(password) >= 12:
    print("Strong password")
elif len(password) > 6:
    print("Moderate password")
