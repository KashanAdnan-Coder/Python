from datetime import datetime


birth_year = int(input("Enter your birth year: "))
today =  datetime.now()
current_year = today.year
age_in_years = current_year - birth_year

print("Your current age is", age_in_years, "years,")