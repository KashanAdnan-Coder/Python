# Write a program that takes a user-entered date in the format "MM/DD/YYYY" and prints it in the format "YYYY-MM-DD".

from datetime import datetime

def convert_date_format(date_string):
        date_object = datetime.strptime(date_string, "%m/%d/%Y")
        formatted_date = date_object.strftime("%Y-%m-%d")
        print(f"Converted date: {formatted_date}")
    

convert_date_format("01/25/2022")

