# create a datetime object from the string "08-26-2023 08:10:00 PM"
# hint: https://strftime.org/
from datetime import datetime

date = datetime.strptime("08-26-2023 08:10:00 PM", '%m-%d-%Y %H:%M:%S %p')

print(date)   
