# Create a function that takes a datetime object as input and displays the day of the week (e.g., "Monday") using strftime().
# hint: https://strftime.org/

from datetime import datetime

def display_day_of_week(date_time_object):
    day_of_week = date_time_object.strftime("%A")
    print(day_of_week)

current_datetime = datetime.now()
display_day_of_week(current_datetime)