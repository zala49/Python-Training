# Salary Slip
ID = str(input("Enter Employee Id : "))
COMPANY_NAME = input("Enter Your Company Name : ")
Name = input("Enter Employee Name : ")
Position = input("Enter Employee Position : ")
Mobile = int(input("Mobile Number : "))
Address = input("Enter Employee Address : ")
Email_id = input("Employee Email id : ")
Salary = int(input("Enter Employee Salary : "))

# First Employee
TA1 = 0.1 * Salary  # TA = Travel Allowance
DA1 = 0.2 * Salary  # DA = Dearness Allowance
HRA1 = 0.3 * Salary  # HRA = House Rent Allowance
PF1 = 0.18 * Salary  # PF = Provident Fund
Net1 = Salary + TA1 + DA1 + HRA1
Total1 = Net1 - PF1

# Second Employee
TA2 = 0.03 * Salary  # TA = Travel Allowance
DA2 = 0.1 * Salary  # DA = Dearness Allowance
HRA2 = 0.3 * Salary  # HRA = House Rent Allowance
PF2 = 0.18 * Salary  # PF = Provident Fund
Net2 = Salary + TA2 + DA2 + HRA2
Total2 = Net1 - PF2

if ID == "1":
    print("\n\t\t*******************SALARY SLIP************************")
    print("\t\tEmployee Id   :", ID)
    print("\t\tCompany Name  :", COMPANY_NAME)
    print("\t\tEmployee Name :", Name)
    print("\t\tPosition      :", Position)
    print("\t\tMobile        :", Mobile)
    print("\t\tEmail Id      :", Email_id)
    print("\t\tAddress       :", Address)
    print("\t\t*******************SALARY DETAILS************************")
    print("\t\tTA            :", TA1)
    print("\t\tDA            :", DA1)
    print("\t\tHRA           :", HRA1)
    print("\t\tPF            :", PF1)
    print("\t\tNet           :", Net1)
    print("\t\tSalary        :", Salary)
    print("\t\tTotal Salary  :", Total1)
elif ID == "2":
    print("\n\t\t*******************SALARY SLIP************************")
    print("\t\tEmployee Id   :", ID)
    print("\t\tCompany Name  :", COMPANY_NAME)
    print("\t\tEmployee Name :", Name)
    print("\t\tPosition      :", Position)
    print("\t\tMobile        :", Mobile)
    print("\t\tEmail Id      :", Email_id)
    print("\t\tAddress       :", Address)
    print("\t\t*******************SALARY DETAILS************************")
    print("\t\tTA            :", TA2)
    print("\t\tDA            :", DA2)
    print("\t\tHRA           :", HRA2)
    print("\t\tPF            :", PF2)
    print("\t\tNet           :", Net2)
    print("\t\tSalary        :", Salary)
    print("\t\tTotal Salary  :", Total2)
else:
    print("Enter correct Details!!")
