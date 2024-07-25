# Write a Python program that uses the date module to print the current date in the format "YYYY-MM-DD".
from datetime import datetime

def get_current_date():
    current_date = datetime.now().strftime("%Y-%m-%d")
    print(current_date)

get_current_date()