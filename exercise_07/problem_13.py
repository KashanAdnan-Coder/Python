# Write a function called is_divisable_by_11 that takes an integer as an parameter and returns whether it is divisible by 11 or not.


def is_divisable_by_11(num):
    if num % 11 == 0:
        print("It is divisible by 11")
    else:
        print("It is not divisible by 11")


is_divisable_by_11(23)