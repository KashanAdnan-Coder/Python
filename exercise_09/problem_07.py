# Create a program that takes a year and a month as input and prints the number of days in that month.
# without using calender module

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))

if month == 2 and year % 4 :
    print("February has 29 days")
elif month in [4, 6, 9, 11]:
    print(f"{month} has 30 days")
else:
    print(f"{month} has 31 days")
