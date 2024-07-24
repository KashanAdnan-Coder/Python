# problem 3
"""
Problem Statement:

Prompt the user to enter a sentence.
Ask user to replace the word
ask user to replace the word with

Print the modified sentence
"""

sentence = input("Write a sentence : ")
where_to_replace = input("What word you want to replace : ")
what_to_replace = input("What word you want to replace with : ")

modified_sentence = sentence.replace(where_to_replace , what_to_replace)
print("Modified Sentence =", modified_sentence)
