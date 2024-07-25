# Create a new text file named "student_records.txt" with the following initial content:

initial_content =   """ Student ID | Student Name | Grade
101       | Alice        | A
102       | Bob          | B
103       | Carol        | C
"""

f = open("student_records.txt", "w")

f.write(initial_content)

f.close()

# Open the "student_records.txt" file in read mode ('r') and read its contents line by line. Print each line to the console.

file = open("student_records.txt", "r")
for line in file:
    print( line.strip())
file.close()

# Create a new text file named "updated_records.txt" in write mode('w').
# Read the content of "student_records.txt" again and write only the lines containing students with grades 'A' or 'B' to the "updated_records.txt" file.
# Close both files.

updated_file = open("updated_records.txt", "w")
file = open("student_records.txt", "w+")
for line in file:
    student_id, student_name, grade = line.strip().split("|")
    if grade in ['A', 'B']:
        file.write(grade)