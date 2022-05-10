def employee(company, name, id_number, position, mobile, address, email_id, salary):
    print("\n\t\t*******************SALARY SLIP************************")

    print("\t\tCompany Name  :", company)
    print("\t\tEmployee Name :", name)
    print("\t\tEmployee Id   :", id_number)
    print("\t\tPosition      :", position)
    print("\t\tMobile        :", mobile)
    print("\t\tEmail Id      :", email_id)
    print("\t\tAddress       :", address)
    print("\t\t*******************SALARY DETAILS************************")
    print("\t\tTA            :", TA)
    print("\t\tDA            :", DA)
    print("\t\tHRA           :", HRA)
    print("\t\tPF            :", PF)
    print("\t\tNet           :", Net)
    print("\t\tSalary        :", salary)
    print("\t\tTotal Salary  :", Total)


Company = input("Enter your company name : ")
Name = input("Enter your name : ")
Id_Number = int(input("Enter your ID Number : "))
Position = input("Enter your Position : ")
Mobile = int(input("Enter your Mobile Number : "))
Address = input("Enter your Address : ")
Email_Id = input("Enter your Email Id : ")
Salary = int(input("Enter your Salary : "))
TA = (0.02 * Salary)  # TA = Travel Allowance
DA = (0.05 * Salary)  # DA = Dearness Allowance
HRA = (0.2 * Salary)  # HRA = House Rent Allowance
PF = (0.18 * Salary)  # PF = Provident Fund
Net = (Salary + TA + DA + HRA)
Total = (Net - PF)
employee(Company, Name, Id_Number, Position, Mobile, Address, Email_Id, Salary)
