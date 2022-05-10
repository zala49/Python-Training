Student_file = open("Student_file.txt", "w")


class Student:
    clg_name = input("Enter collegue Name : ")
    name = input("Enter student Name : ")
    Roll_number = int(input("Enter your Roll Number : "))
    Enrollment_number = int(input("Enter your Enrollment Number : "))
    Semester = input("Enter your Semester : ")
    Python = int(input("Python Marks : "))
    Java = int(input("Java Marks : "))
    C = int(input("C Marks : "))
    Total = Python + Java + C
    Average = (Total / 300) * 100


class Student2(Student):
    def adddata(self):
        Student_file.write("\nCollegue             : "f"{Student.clg_name}")
        Student_file.write("\nName                 : "f"{Student.name}")
        Student_file.write("\nRoll Number          : "f"{Student.Roll_number}")
        Student_file.write("\nEnrollment           : "f"{Student.Enrollment_number}")
        Student_file.write("\nSemester             : "f"{Student.Semester}")
        Student_file.write("\nPython Marks         : "f"{Student.Python}")
        Student_file.write("\nJava Marks           : "f"{Student.Java}")
        Student_file.write("\nC++ Marks            : "f"{Student.C}")
        Student_file.write("\nTotal                : "f"{Student.Total}")
        Student_file.write("\nAverage              : "f"{Student.Average}")

        #print("Collegue    : ", Student.clg_name)
        #print("Name        : ", Student.name)
        #print("Roll Number : ", Student.Roll_number)
        #print("Enrollment  : ", Student.Enrollment_number)
        #print("Semester    : ", Student.Semester)
        #print("Python Marks: ", Student.Python)
        #print("Java Marks  : ", Student.Java)
        #print("C++ Marks   : ", Student.C)
        #print("Total marks : ", Student.Total)
        #print("Percentage  : ", Student.Average)


obj = Student2()
obj.adddata()
