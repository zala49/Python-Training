# Tuition Management System

Trainer_Id = ["1", "2", "3", "4"]
Trainer = ["AERON", "SHUBHAM", "ANKIT", "ZALA"]
Trainer_Subject = ["C++", "Java", "PHP", "Python"]
Trainer_Salary = 10000
Incentive = [5000, 6000, 7000, 8000]

TA = 0.1 * Trainer_Salary
DA = 0.07 * Trainer_Salary
HRA = 0.2 * Trainer_Salary
PF = 0.18 * Trainer_Salary
Net = Trainer_Salary + TA + DA + HRA
Trainer1_Total = Net - PF

while True:
    Name = input("Enter the Id or Name of Tuition Sir : ").upper()
    if Name == Trainer[0]:
        Trainer1_Taken_Lecture = int(input("Enter the number of taken lecture by Aeron : "))
        Trainer1_Student = input("How many student teach by Aeron : ")
        if Trainer1_Taken_Lecture >= 12:
            Salary = Trainer1_Total + Incentive[0]
            print("\t\t=====================DETAILS======================")
            print("\t\t Id            : ", Trainer_Id[0])
            print("\t\t Name          : ", Trainer[0])
            print("\t\t Subject       : ", Trainer_Subject[0])
            print("\t\t Taken Lecture : ", Trainer1_Taken_Lecture)
            print("\t\t Teach Student : ", Trainer1_Student)
            print("\t\t ******************SALARY DETAILS*****************")
            print("\t\t TA  : ", TA)
            print("\t\t DA  : ", DA)
            print("\t\t HRA : ", HRA)
            print("\t\t PF  : ", PF)
            print("\t\t Salary       : ", Trainer_Salary)
            print("\t\t Incentive    : ", Incentive[0])
            print("\t\t Total Salary : ", Salary)
            print("\t\t==================================================")
        elif Trainer1_Taken_Lecture < 12:
            Salary = Trainer1_Total - 2000
            print("\t\t=====================DETAILS======================")
            print("\t\t Id            : ", Trainer_Id[0])
            print("\t\t Name          : ", Trainer[0])
            print("\t\t Subject       : ", Trainer_Subject[0])
            print("\t\t Taken Lecture : ", Trainer1_Taken_Lecture)
            print("\t\t Teach Student : ", Trainer1_Student)
            print("\t\t ******************SALARY DETAILS*****************")
            print("\t\t TA  : ", TA)
            print("\t\t DA  : ", DA)
            print("\t\t HRA : ", HRA)
            print("\t\t PF  : ", PF)
            print("\t\t Basic Salary : ", Trainer_Salary)
            print("\t\t Total Salary : ", Salary)
            print("\t\t==================================================")
        else:
            print("Enter Correct Value!!")
            break
    elif Name == Trainer[1]:
        Trainer2_Taken_Lecture = int(input("Enter the number of taken lecture by Shubham : "))
        Trainer2_Student = input("How many student teach by Shubham : ")
        if Trainer2_Taken_Lecture >= 12:
            Salary = Trainer1_Total + Incentive[1]
            print("\t\t=====================DETAILS======================")
            print("\t\t Id            : ", Trainer_Id[1])
            print("\t\t Name          : ", Trainer[1])
            print("\t\t Subject       : ", Trainer_Subject[1])
            print("\t\t Taken Lecture : ", Trainer2_Taken_Lecture)
            print("\t\t Teach Student : ", Trainer2_Student)
            print("\t\t ******************SALARY DETAILS*****************")
            print("\t\t TA  : ", TA)
            print("\t\t DA  : ", DA)
            print("\t\t HRA : ", HRA)
            print("\t\t PF  : ", PF)
            print("\t\t Salary       : ", Trainer_Salary)
            print("\t\t Incentive    : ", Incentive[1])
            print("\t\t Total Salary : ", Salary)
            print("\t\t==================================================")
        elif Trainer2_Taken_Lecture < 12:
            Salary = Trainer1_Total - 2000
            print("\t\t=====================DETAILS======================")
            print("\t\t Id            : ", Trainer_Id[1])
            print("\t\t Name          : ", Trainer[1])
            print("\t\t Subject       : ", Trainer_Subject[1])
            print("\t\t Taken Lecture : ", Trainer2_Taken_Lecture)
            print("\t\t Teach Student : ", Trainer2_Student)
            print("\t\t ******************SALARY DETAILS*****************")
            print("\t\t TA  : ", TA)
            print("\t\t DA  : ", DA)
            print("\t\t HRA : ", HRA)
            print("\t\t PF  : ", PF)
            print("\t\t Basic Salary : ", Trainer_Salary)
            print("\t\t Total Salary : ", Salary)
            print("\t\t==================================================")
        else:
            print("Enter Correct Value!!")
            break
    elif Name == Trainer[2]:
        Trainer3_Taken_Lecture = int(input("Enter the number of taken lecture by Ankit : "))
        Trainer3_Student = input("How many student teach by Ankit : ")
        if Trainer3_Taken_Lecture >= 12:
            Salary = Trainer1_Total + Incentive[1]
            print("\t\t=====================DETAILS======================")
            print("\t\t Id            : ", Trainer_Id[2])
            print("\t\t Name          : ", Trainer[2])
            print("\t\t Subject       : ", Trainer_Subject[2])
            print("\t\t Taken Lecture : ", Trainer3_Taken_Lecture)
            print("\t\t Teach Student : ", Trainer3_Student)
            print("\t\t ******************SALARY DETAILS*****************")
            print("\t\t TA  : ", TA)
            print("\t\t DA  : ", DA)
            print("\t\t HRA : ", HRA)
            print("\t\t PF  : ", PF)
            print("\t\t Salary       : ", Trainer_Salary)
            print("\t\t Incentive    : ", Incentive[2])
            print("\t\t Total Salary : ", Salary)
            print("\t\t==================================================")
        elif Trainer3_Taken_Lecture < 12:
            Salary = Trainer1_Total - 2000
            print("\t\t=====================DETAILS======================")
            print("\t\t Id            : ", Trainer_Id[2])
            print("\t\t Name          : ", Trainer[2])
            print("\t\t Subject       : ", Trainer_Subject[2])
            print("\t\t Taken Lecture : ", Trainer3_Taken_Lecture)
            print("\t\t Teach Student : ", Trainer3_Student)
            print("\t\t ******************SALARY DETAILS*****************")
            print("\t\t TA  : ", TA)
            print("\t\t DA  : ", DA)
            print("\t\t HRA : ", HRA)
            print("\t\t PF  : ", PF)
            print("\t\t Basic Salary : ", Trainer_Salary)
            print("\t\t Total Salary : ", Salary)
            print("\t\t==================================================")
        else:
            print("Enter Correct Value!!")
            break
    elif Name == Trainer[3]:
        Trainer4_Taken_Lecture = int(input("Enter the number of taken lecture by Zala : "))
        Trainer4_Student = input("How many student teach by Zala : ")
        if Trainer4_Taken_Lecture >= 12:
            Salary = Trainer1_Total + Incentive[1]
            print("\t\t=====================DETAILS======================")
            print("\t\t Id            : ", Trainer_Id[3])
            print("\t\t Name          : ", Trainer[3])
            print("\t\t Subject       : ", Trainer_Subject[3])
            print("\t\t Taken Lecture : ", Trainer4_Taken_Lecture)
            print("\t\t Teach Student : ", Trainer4_Student)
            print("\t\t ******************SALARY DETAILS*****************")
            print("\t\t TA  : ", TA)
            print("\t\t DA  : ", DA)
            print("\t\t HRA : ", HRA)
            print("\t\t PF  : ", PF)
            print("\t\t Salary       : ", Trainer_Salary)
            print("\t\t Incentive    : ", Incentive[3])
            print("\t\t Total Salary : ", Salary)
            print("\t\t==================================================")
        elif Trainer4_Taken_Lecture < 12:
            Salary = Trainer1_Total - 2000
            print("\t\t=====================DETAILS======================")
            print("\t\t Id            : ", Trainer_Id[3])
            print("\t\t Name          : ", Trainer[3])
            print("\t\t Subject       : ", Trainer_Subject[3])
            print("\t\t Taken Lecture : ", Trainer4_Taken_Lecture)
            print("\t\t Teach Student : ", Trainer4_Student)
            print("\t\t ******************SALARY DETAILS*****************")
            print("\t\t TA  : ", TA)
            print("\t\t DA  : ", DA)
            print("\t\t HRA : ", HRA)
            print("\t\t PF  : ", PF)
            print("\t\t Basic Salary : ", Trainer_Salary)
            print("\t\t Total Salary : ", Salary)
            print("\t\t==================================================")
        else:
            print("Enter Correct Value!!")
            break

