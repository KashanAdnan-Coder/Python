# Extracting Sublist from a List of Temperatures
# Objective: Given a list of daily temperatures for a month, extract the temperatures for a specific week (e.g., week 2).
temperatures = [22, 24, 20, 25, 23, 26, 24, 25, 27, 29, 30, 28, 26, 27, 24, 23, 22, 21, 25, 24, 26, 27, 29, 28, 26, 25, 24, 23, 22, 21]

week_days = 7
index = week_days - 1

print(temperatures[index:13])