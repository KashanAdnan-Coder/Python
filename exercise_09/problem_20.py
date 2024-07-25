# Create a function that takes a timezone name as input and prints the current date time object in that timezone.


from datetime import datetime, timezone, timedelta

def format_timezone(timezone):
    current_datetime = datetime.now(timezone)
    print(current_datetime)

format_timezone(timezone(timedelta(hours=5)))  