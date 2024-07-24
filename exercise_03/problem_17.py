"""
Write a program that takes an employee's salary and years of service as input. Calculate the bonus as follows:

If the years of service are less than 5, no bonus.
If the years of service are between 5 and 10, bonus is 10% of the salary.
If the years of service are more than 10, bonus is 20% of the salary.
Print the bonus amount.
"""


employ_salary = int(input("Enter Employ Salary : "))
service_year = int(input("Enter Service Year : "))


if (service_year <= 5):
    print("no bonus")
elif service_year >= 10:
    print("you have 20% of bonus, and your salry will be", round(employ_salary * 0.20))
elif service_year > 5:
    print("you have 10% of bonus, and your salry will be", round(employ_salary * 0.10))
    