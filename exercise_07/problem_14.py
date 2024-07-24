# Write a function called get_highest that takes 2 numbers as parameters and returns the highest of the 2 numbers.

def get_highest(num1 , num2):
    if num1 > num2:
        print(f"{num1} is the highest")
    elif num2 > num1:
        print(f"{num2} is the highest")


get_highest(2 ,5)