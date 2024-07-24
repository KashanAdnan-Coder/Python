# Write a program that accepts 1 input from user and check if the number is divisible by 2 and 3 both.
# for example
# input1 is 10
# output should be "10 is only divisible by 2"
# input1 is 9
# output should be "9 is only divisible by 3"
# input1 is 12
# output should be "12 is divisible by 2 and 3"


num = int(input("Enter any number: "))


divisible_by_2 = num % 2
divisible_by_3 = num % 3

if divisible_by_2 == 0 and divisible_by_3 == 0:
    print("The number is divisible by 2 and 3")
elif divisible_by_2 == 0:
    print("The number is divisible by 2")
elif divisible_by_3 == 0:
    print("The number is divisible by 3")
