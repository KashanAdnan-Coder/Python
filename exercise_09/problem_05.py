# Write a program that calculates and displays the number of days between two given dates.

from datetime import datetime

date_time = input("Enter a date 1 : ")
dateTime = datetime.strptime(date_time, '%Y-%m-%d')
date_time1 = input("Enter a date 2 : ")
dateTime2 = datetime.strptime(date_time1, '%Y-%m-%d')

date =  dateTime2 - dateTime 
print("The diffrent between two dates is" ,date)