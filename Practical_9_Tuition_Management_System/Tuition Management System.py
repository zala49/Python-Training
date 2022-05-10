# Tuition Management System

# Name
Trainer1_Name = "Shubham"
Trainer2_Name = "Aeron"

# Id
Trainer1 = 1
Trainer2 = 2
Trainer1_Subject = "Maths"
Trainer2_Subject = "Python"

# Salary
Trainer1_Salary = 20000
Trainer2_Salary = 25000
Incentive_For_Trainer1 = 5000
Incentive_For_Trainer2 = 10000
TA = 0.1 * Trainer1_Salary  # TA = Travel Allowance
DA = 0.07 * Trainer1_Salary  # DA = Dearness Allowance
HRA = 0.2 * Trainer1_Salary  # HRA = House Rent Allowance
PF = 0.18 * Trainer1_Salary  # PF = Provident Fund
Net1 = Trainer1_Salary + TA + DA + HRA
Trainer1_Total = (Net1 - PF)
Net2 = Trainer2_Salary + TA + DA + HRA
Trainer2_Total = Net2 - PF

while True:
    Name = input("Enter the Id or Name of Tuition Sir : ")
    if Name == Trainer1_Name or Name == Trainer1:
        Trainer1_Taken_Lecture = int(input("Enter the number of taken lecture by " f"{Trainer1_Name} : "))
        Trainer1_Student = input("How many student teach by Shubham Sir : ")
        if Trainer1_Taken_Lecture >= 12:
            Salary = Trainer1_Total + Incentive_For_Trainer1
            print("\t\t=====================DETAILS======================")
            print("\t\t Id            : ", Trainer1)
            print("\t\t Name          : ", Trainer1_Name)
            print("\t\t Subject       : ", Trainer1_Subject)
            print("\t\t Taken Lecture : ", Trainer1_Taken_Lecture)
            print("\t\t Teach Student : ", Trainer1_Student)
            print("\t\t ******************SALARY DETAILS*****************")
            print("\t\t TA  : ", TA)
            print("\t\t DA  : ", DA)
            print("\t\t HRA : ", HRA)
            print("\t\t PF  : ", PF)
            print("\t\t Salary       : ", Trainer1_Salary)
            print("\t\t Incentive    : ", Incentive_For_Trainer1)
            print("\t\t Total Salary : ", Salary)
            print("\t\t==================================================")
        elif Trainer1_Taken_Lecture < 12:
            Salary = Trainer1_Total - 2000
            print("\t\t=====================DETAILS======================")
            print("\t\t Id            : ", Trainer1)
            print("\t\t Name          : ", Trainer1_Name)
            print("\t\t Subject       : ", Trainer1_Subject)
            print("\t\t Taken Lecture : ", Trainer1_Taken_Lecture)
            print("\t\t Teach Student : ", Trainer1_Student)
            print("\t\t ******************SALARY DETAILS*****************")
            print("\t\t TA  : ", TA)
            print("\t\t DA  : ", DA)
            print("\t\t HRA : ", HRA)
            print("\t\t PF  : ", PF)
            print("\t\t Basic Salary : ", Trainer1_Salary)
            print("\t\t Total Salary : ", Salary)
            print("\t\t==================================================")
        else:
            print("Enter the Correct Number!!")
            break
    elif Name == Trainer2_Name or Name == Trainer2:
        Trainer2_Taken_Lecture = int(input("Enter the number of taken lecture by " f"{Trainer2_Name} : "))
        Trainer2_Student = input("How many student teach by Aeron Sir : ")
        if Trainer2_Taken_Lecture >= 16:
            Salary = Trainer2_Total + Incentive_For_Trainer2
            print("\t\t=====================DETAILS======================")
            print("\t\t Id            : ", Trainer2)
            print("\t\t Name          : ", Trainer2_Name)
            print("\t\t Subject       : ", Trainer2_Subject)
            print("\t\t Taken Lecture : ", Trainer2_Taken_Lecture)
            print("\t\t Teach Student : ", Trainer2_Student)
            print("\t\t ******************SALARY DETAILS*****************")
            print("\t\t TA  : ", TA)
            print("\t\t DA  : ", DA)
            print("\t\t HRA : ", HRA)
            print("\t\t PF  : ", PF)
            print("\t\t Salary       : ", Trainer2_Salary)
            print("\t\t Incentive    : ", Incentive_For_Trainer2)
            print("\t\t Total Salary : ", Salary)
            print("\t\t==================================================")
        elif Trainer2_Taken_Lecture < 16:
            Salary = Trainer2_Total - 8000
            print("\t\t=====================DETAILS======================")
            print("\t\t Id            : ", Trainer2)
            print("\t\t Name          : ", Trainer2_Name)
            print("\t\t Subject       : ", Trainer2_Subject)
            print("\t\t Taken Lecture : ", Trainer2_Taken_Lecture)
            print("\t\t Teach Student : ", Trainer2_Student)
            print("\t\t ******************SALARY DETAILS*****************")
            print("\t\t TA  : ", TA)
            print("\t\t DA  : ", DA)
            print("\t\t HRA : ", HRA)
            print("\t\t PF  : ", PF)
            print("\t\t Basic Salary : ", Trainer2_Salary)
            print("\t\t Total Salary : ", Salary)
            print("\t\t==================================================")
        else:
            print("Enter the Correct Number!!")
            break
    else:
        print("Enter the Correct Details!!")
        break
