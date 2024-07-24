# Write a program that accepts 3 input from user and check the second largest.
# for example:
# input1 is 5 and input2 is 10 and input3 is 15
# output should be 10 as this number is larger than 5 and smaller than 15

num1 = int(input("Enter any number: "))
num2 = int(input("Enter any number: "))
num3 = int(input("Enter any number: "))

if (num1 >= num2 and num1 <= num3) or (num1 <= num2 and num1 >= num3):
    print(num1, "It is the second largest number")
elif (num2 >= num1 and num2 <= num3) or (num2 <= num1 and num2 >= num3):
    print(num2, "It is the second largest number")
else:
    print(num3, "It is the largest number")
