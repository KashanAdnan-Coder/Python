#Create a program that takes a date as string and returns the corresponding day of the week (e.g., Monday, Tuesday, etc.).


from datetime import datetime
date = input("Enter a date: ")a
date_time = datetime.strptime(date, '%Y-%m-%d')

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_of_week = days[date_time.weekday()]

print(day_of_week)