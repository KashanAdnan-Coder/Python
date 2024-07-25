# Create a function that takes a datetime in the format "MM/DD/YYYY HH:MM:SS" as string  formats it as "YYYY-MM-DD HH:MM:SS".


from datetime import datetime

def convert_datetime_format(datetime_string):
    datetime_object = datetime.strptime(datetime_string, "%m/%d/%Y %H:%M:%S")
    formatted_datetime = datetime_object.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_datetime

print(convert_datetime_format("12/31/2021 15:30:00"))  # Output: 2021-12-31 15:30:00