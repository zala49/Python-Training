Company_Name = []
for x in range(0, 1):
    company_Name = input("Enter the Company name : ")
    Company_Name.append(company_Name)

Name = []
for x in range(0, 1):
    name = input("Enter your Name : ")
    Name.append(name)

ID = []
for x in range(0, 1):
    i_name = int(input("Enter you ID : "))
    ID.append(i_name)

Position = []
for x in range(0, 1):
    position = input("Enter your Position : ")
    Position.append(position)

Email_id = []
for x in range(0, 1):
    email_id = input("Enter your Email-id : ")
    Email_id.append(email_id)

Mobile = []
for x in range(0, 1):
    mobile = int(input("Enter your Mobile Number : "))
    Mobile.append(mobile)

Address = []
for x in range(0, 1):
    address = input("Enter your Address : ")
    Address.append(address)

Salary = int(input("Enter your Salary : "))

TA = 0.02 * Salary  # TA = Travel Allowance
DA = 0.05 * Salary  # DA = Dearness Allowance
HRA = 0.2 * Salary  # HRA = House Rent Allowance
PF = 0.18 * Salary  # PF = Provident Fund
Net = Salary + TA + DA + HRA
Total = Net - PF
print("\n\t\t*******************SALARY SLIP************************")
print("\t\tCompany Name :", Company_Name)
print("\t\tName         :", Name)
print("\t\tID           :", ID)
print("\t\tPosition     :", Position)
print("\t\tEmail-id     :", Email_id)
print("\t\tMobile       :", Mobile)
print("\t\tAddress      :", Address)
print("\t\tTA           :", TA)
print("\t\tDA           :", DA)
print("\t\tHRA          :", HRA)
print("\t\tPF           :", PF)
print("\t\tSalary       :", Salary)
print("\t\tTotal Salary :", Total)
print("\n\t\t******************************************************")
