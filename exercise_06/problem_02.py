"""
Create a dictionary named employee_data with the following key-value pairs:
"John": 55000
"Emma": 60000
"Harry": 70000
"Sophia": 65000
"Mike": 48000

1. Write a for loop with an if statement to identify employees who earn more than $60,000. Print their names.
2. Write a for loop to increase the salary of each employee by 10%. Update the dictionary accordingly.


"""

employ_data = {
    "John": 55000,
    "Emma": 60000,
    "Harry": 70000,
    "Sophia": 65000,
    "Mike": 48000
}

for employ in employ_data:
    salary = employ_data[employ]
    if salary > 60000:
        print(employ) 

for employ in employ_data:
    employ_data[employ] *= 1.1

print(employ_data)