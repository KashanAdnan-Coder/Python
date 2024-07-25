# Create a function that takes a starting date and a number of days as input, and then calculates and prints the date that is the specified number of days in the future.


from datetime import datetime, timedelta


def calculate_future_date(start_date, num_days):
    start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")  
    future_date = start_date_obj + timedelta(days=num_days)
    future_date_str = future_date.strftime("%Y-%m-%d") 
    print(f"The future date is: {future_date_str}")


start_date = "2022-01-01"
num_days = 50

calculate_future_date(start_date, num_days)