# Student Management System

Collegue = input("Enter Your College Name : ")
Name = input("Enter Student Name : ")
Semester = input("Enter Student Semester : ")
Enrollment = int(input("Enter Enrollment Number : "))
Roll_Number = int(input("Enter Roll No : "))

Subjects = {"PYTHON", "Java", "C"}
Subjcode = ["11", "22", "33"]
Python = int(input("Python Marks : "))
Java = int(input("Java Marks : "))
C = int(input("C Marks : "))

Total = Python + Java + C

average = (Total / 300) * 100

print("\t\t==================================================================")
print("\n\t\t********************** YOUR RESULT *****************************")
print("\t\tCOLLEGE         : ", Collegue)
print("\t\tNAME            : ", Name)
print("\t\tROLL NUMBER     : ", Roll_Number)
print("\t\tENROLLMENT      : ", Enrollment)
print("\t\t===================================================================")
print("\t\tSUBJECTS           MARKS ")
print("\t\t===================================================================")
print("\t\tPython          : ", Python)
print("\t\tJava            : ", Java)
print("\t\tC               : ", C)
print("\t\tTotal Marks is  : ", Total)
print("\t\tPercentage is   : ", average)
print("\t\t===================================================================")
