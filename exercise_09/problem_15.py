# create a datetime object from the string "26-08-2023 15:18:33.983780-07:00" 
# hint: https://strftime.org/

from datetime import datetime

date = datetime.strptime("26-8-2023 15:18:33.983780-07:00", '%d-%m-%Y %H:%M:%S.%f%z')

print(date)