# Create a function that takes a datetime object as input and formats it as "Day-Month-Year" (e.g., "25-August-2023") using strftime().

from datetime import datetime

def format_date(date_obj):
    formatted_date = date_obj.strftime("%d-%B-%Y")
    return formatted_date

current_date = datetime.now()
formatted_date = format_date(current_date)

print(formatted_date)