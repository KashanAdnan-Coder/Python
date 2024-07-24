# problem 8
"""
Problem: Ask the user to input a sentence. 
Replace all spaces with underscores 
and split the sentence into words.

NOTE: Concepts Covered: replace(), split(), input(), print()
"""

sentence = input("Enter a sentence : ")

modified_sentence = sentence.replace(" " , "_")
splitted_sentence = sentence.split()
print(modified_sentence)
print(splitted_sentence)