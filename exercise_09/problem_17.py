# create a current datetime and then displays it in the format "HH:MM AM/PM"

from datetime import datetime

current_time = datetime.now().strftime("%H:%M %p")
print(current_time)
