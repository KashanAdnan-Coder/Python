# Write a program to check char is vowel or not.

char = input("Enter a char: ")

vowels = ["a","e","i","o","u"]

for vowel in vowels:
    if char == vowel:
        print("There is a vowel!")
        break
    else:
        print("There is an't any vowel!")
        break