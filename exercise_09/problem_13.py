# Create a function that takes a datetime object as input and formats it as "Month Day, Year" (e.g., "August 25, 2023") using strftime().

from datetime import datetime

def format_datetime(datetime_obj):
    formatted_date = datetime_obj.strftime("%B %d, %Y")
    return formatted_date

current_datetime = datetime.now()
formatted_date = format_datetime(current_datetime)
print(formatted_date)  