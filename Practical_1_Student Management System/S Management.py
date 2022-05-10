def student(collegue, name, semester, enrollment, roll_number, subjects, python, java, c):
    print("\t\t==================================================================")
    print("\n\t\t********************** YOUR RESULT *****************************")
    print("\t\tCOLLEGUE    : ", collegue)
    print("\t\tNAME        : ", name)
    print("\t\tSEMESTER    : ", semester)
    print("\t\tENROLLMENT  : ", enrollment)
    print("\t\tROLL NUMBER : ", roll_number)
    print("\t\t===================================================================")
    print("\t\tSUBJECTS          MARKS ")
    print("\t\t===================================================================")
    print("\t\tPython          : ", python)
    print("\t\tJava            : ", java)
    print("\t\tC               : ", c)
    print("\t\tTotal Marks is  : ", Total)
    print("\t\tPercentage is   : ", average)
    print("\t\t===================================================================")


clg = input("Enter your Collegue Name : ")
Name = input("Enter your Name : ")
Semester = input("Enter your Sem : ")
Enrollment = int(input("Enter your Enrollment : "))
Roll_Number = int(input("Enter your Roll_Number : "))
Subjects = ["Python", "Java", "C"]
Python = int(input("Enter Python's Marks : "))
Java = int(input("Enter Java's Marks : "))
C = int(input("Enter C's Marks : "))
Total = Python + Java + C
average = (Total / 300) * 100
student(clg, Name, Semester, Enrollment, Roll_Number, Subjects, Python, Java, C)
