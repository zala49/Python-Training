import calculation

a = calculation.ta(0.1)
b = calculation.da(0.2)
c = calculation.hra(0.3)
d = calculation.pf(0.18)


def salary(id_1, company_name, name, position, mobile, email_id, address, salaryy, ta, da, hra, pf, net):
    print("\n\t\t*******************SALARY SLIP************************")
    print("\t\tEmployee Id   :", id_1)
    print("\t\tCompany Name  :", company_name)
    print("\t\tEmployee Name :", name)
    print("\t\tPosition      :", position)
    print("\t\tMobile        :", mobile)
    print("\t\tEmail Id      :", email_id)
    print("\t\tAddress       :", address)
    print("\t\t*******************SALARY DETAILS************************")
    print("\t\tTA            :", ta)
    print("\t\tDA            :", da)
    print("\t\tHRA           :", hra)
    print("\t\tPF            :", pf)
    print("\t\tNet           :", net)
    print("\t\tSalary        :", salaryy)
    print("\t\tTotal Salary  :", total_salary)


ID = str(input("Enter Employee Id : "))
COMPANY_NAME = input("Enter Your Company Name : ")
Name = input("Enter Employee Name : ")
Position = input("Enter Employee Position : ")
Mobile = int(input("Mobile Number : "))
Address = input("Enter Employee Address : ")
Email_id = input("Employee Email id : ")
Salary = int(input("Enter Employee Salary : "))
ta1 = a * Salary
da1 = b * Salary
hra1 = c * Salary
pf1 = d * Salary
net1 = ta1 + da1 + hra1 + Salary
total_salary = net1 - pf1
salary(ID, COMPANY_NAME, Name, Position, Mobile, Email_id, Address, Salary, ta1, da1, hra1, pf1, net1)
