# Write a program to check if year is leap year.
# NOTE: search on google of what leap year is.

# the year number must be divisible by four – except for end-of-century years, which must be divisible by 400

year = int(input("Enter the year : "))

if (year % 4) == 0:
    print("It is the leap year!")
else:
    print("It is not the leap year!")