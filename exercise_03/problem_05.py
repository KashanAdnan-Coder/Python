# Write a program to display the grade of the user in subject A, ask user marks obtained out of 100
# Python program that asks the user for their marks in Subject A and then displays the corresponding grade:
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 50:
    print("D")
elif marks >= 40:
    print("E")
elif marks >= 30:
    print("F")