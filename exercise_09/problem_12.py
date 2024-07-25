# Create a function that takes a datetime object and a number of hours as input, then returns a new datetime object with the added hours.


from datetime import datetime , timedelta

def add_hours(datetime_obj, hours): 
    
    return datetime_obj + timedelta(hours=hours)

# Example usage:

current_datetime = datetime.now()
hours_to_add = 8
new_datetime = add_hours(current_datetime, hours_to_add)

print(new_datetime)  # Output: 2023-06-12 10:45:12.738168
