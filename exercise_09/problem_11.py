# Write a program that calculates the time difference between two given datetime objects and displays it in hours, minutes, and seconds.

from datetime import datetime

date_time_1 = input("Enter a datetime object to calculate the time difference between given format is hours, minutes, and seconds : ")
date_time_2 = input("Enter a datetime object to calculate the time difference between given format is hours, minutes, and seconds : ")

date_time_obj_1 = datetime.strptime(date_time_1, "%H:%M:%S")

date_time_obj_2 = datetime.strptime(date_time_2, "%H:%M:%S")

date_time_diff = date_time_obj_1 - date_time_obj_2
hours, remainder = divmod(date_time_diff.seconds, 3600)

minutes, seconds = divmod(remainder, 60)

print(f"Time difference between {date_time_1} and {date_time_2} is: {hours} hours, {minutes} minutes, and {seconds} seconds.")

