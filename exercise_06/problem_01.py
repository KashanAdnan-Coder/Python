"""
Create a dictionary named student_scores with the following key-value pairs:
"Alice": 85
"Bob": 78
"Charlie": 92
"Diana": 88
"Evan": 76


1. Write a for loop to iterate through the student_scores dictionary and print each student's name and their score in the format: Student: [Name], Score: [Score].

2. Write a for loop to calculate the average score of the students. Print the average score.

3. Write a for loop to assign grades based on the following criteria:
Score >= 90: Grade A
Score >= 80 and < 90: Grade B
Score >= 70 and < 80: Grade C
Score < 70: Grade D
Store these grades in a new dictionary called student_grades.

4. Modify the student_scores dictionary by adding 5 bonus points to each student's score. 
Print the updated student_scores dictionary.
"""

student_scores = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "Diana": 88,
    "Evan": 76
}

for score  in student_scores:
    print(f"Student: {score}, Score: {student_scores[score]}")

for student in student_scores:
    score = student_scores[student]
    average = score + 500 / 2
    print(average)

for student in student_scores:
    score = student_scores[student]
    if score >= 90:
        print("Grade A")
    elif 80 <= score < 90:
        print("Grade B")
    elif 70 <= score < 80:
        print("Grade C")
    elif score < 70:
        print("Grade D")


for i in student_scores:
    score = student_scores[i]
    student_scores[i] = score + 5

print(student_scores)