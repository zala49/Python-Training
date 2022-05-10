# Employee Management System

COMPANY_NAME = input("Enter Your Company Name : ")

Name = input("Enter Employee Name : ")
ID = input("Enter Employee Id : ")
Position = input("Enter Employee Position : ")
Mobile = int(input("Mobile Number : "))
Address = input("Enter Employee Address : ")
Email_id = input("Employee Email id : ")
Salary = int(input("Enter Employee Salary : "))

TA = (0.02 * Salary)  # TA = Travel Allowance
DA = (0.05 * Salary)  # DA = Dearness Allowance
HRA = (0.2 * Salary)  # HRA = House Rent Allowance
PF = (0.18 * Salary)  # PF = Provident Fund
Net = (Salary + TA + DA + HRA)
Total = (Net - PF)

print("\n\t\t*******************SALARY SLIP************************")

print("\t\tCompany Name  :", COMPANY_NAME)
print("\t\tEmployee Name :", Name)
print("\t\tEmployee Id   :", ID)
print("\t\tPosition      :", Position)
print("\t\tMobile        :", Mobile)
print("\t\tEmail Id      :", Email_id)
print("\t\tAddress       :", Address)
print("\t\t*******************SALARY DETAILS************************")
print("\t\tTA            :", TA)
print("\t\tDA            :", DA)
print("\t\tHRA           :", HRA)
print("\t\tPF            :", PF)
print("\t\tNet           :", Net)
print("\t\tSalary        :", Salary)
print("\t\tTotal Salary  :", Total)
