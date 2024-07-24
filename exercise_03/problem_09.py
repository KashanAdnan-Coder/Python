# Write a program that accepts 3 inputs from user. input 1 and input 2 should be numbers and the third input should be mathematical operator. 
# Perform operation accordingly
# for example
# input1 is 5 and input2 is 10 and input3 is +
# then output should be 15
# input1 is 5 and input2 is 10 and input3 is *
# then output should be 50


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
mathamtical_operator = input("Enter any methametical operator: ")

if mathamtical_operator == "+":
    print(num1 + num2)
if mathamtical_operator == "-":
    print(num1 - num2)
if mathamtical_operator == "*":
    print(num1 * num2)
if mathamtical_operator == "/":
    print(num1 / num2)
if mathamtical_operator == "%":
    print(num1 % num2)