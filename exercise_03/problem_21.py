"""
create the same ATM machine program that we do in last class.

Features:
Affiliated Card Requirement:
Allow transactions only if the user has an affiliated card (affiliated_card is True) and the user's age is less than 60 years (age < 60).

Senior Citizen Exception:
Allow transactions for senior citizens (is_senior_citizen is True) regardless of their affiliated card status.

Government Employee Exception:
Allow transactions for government employees (is_govt_employee is True) regardless of their age and affiliated card status.

Additional Charge for Low Grade:
Charge an additional 10 Rs for transactions if the user's grade (grade) is less than 18.

# hint: filename: if_statement/if_with_nested_if.py
"""

# Features

grade = int(input("Enter your grade : "))
affiliated_card = input("Do you have affiliated card? (yes/no): ")
age = int(input("Enter your age: "))
senior_citizen = input("Are you a senior citizen? (yes/no): ")
gov_employ = input("Are you a goverment employ? (yes/no): ")

if grade < 18:
    print('10 Rs for transactions')
if affiliated_card.upper() == "YES" and age < 60:
    print("Transiction Successfull, for Affiliated Card!")
if senior_citizen.lower() == "yes":
    print("Transiction Successfull, for Senior Citizen!")
if gov_employ.lower() == "yes":
    print("Transiction Successfull, for Goverment Employ!")