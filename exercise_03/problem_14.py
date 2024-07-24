# Write a python program that accept user an input. The valid input should be of following
# - GREEN or gREEN or green etc 
# - RED or red or rEd etc 
# - YELLOW or yellow or yELlOw etc
# program should display the following message on checking above input
# Car is allowed to go
# Car has to wait
# Car has to stop
# invalid input

color = input("Enter a color: ")

if color.lower() == "red":
    print("You selected red color!")
elif color.lower() == "green":
    print("You selected green color!")
elif color.lower() == "yellow":
    print("You selected yellow color!")
