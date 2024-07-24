# Write a function called fuel_cost that takes 2 numbers as parameter "distance" as required arg 
# and "fuel_per_liter" as optional arg that has default value to 280. 
# The function should return the cost in Rs.


def fuel_cost(distance, fuel_per_liter=280):
    cost = distance * fuel_per_liter
    return cost

# Examples of calling the function
distance = 100  # Example distance in kilometers
cost = fuel_cost(distance)
print(f"The fuel cost for {distance} km is Rs. {cost}")