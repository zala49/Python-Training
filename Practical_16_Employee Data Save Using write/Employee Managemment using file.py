company = open("company_employee_details.txt", "w")


name = input("Enter your company name : ")
id_1 = input("Enter your id : ")
position = input("Enter your position : ")
mobile = int(input("Enter your mobile : "))
email_id = input("Enter your Email-id : ")
address = input("Enter your address : ")
salary = int(input("Enter your salary : "))
Ta = salary * 0.02
Da = salary * 0.03
Hra = salary * 0.2
Pf = salary * 0.18
Net = Ta + Da + Hra - Pf
Total = Net + salary

company.write("Employee Details".center(50))
company.write("\n**********************************************************")
company.write("\nName         : "f"{name}")
company.write("\nId           : "f"{id_1}")
company.write("\nPosition     : "f"{position}")
company.write("\nEmail_id     : "f"{email_id}")
company.write("\nMobile No    : "f"{mobile}")
company.write("\nAddress      : "f"{address}")
company.write("\nTa           : "f"{Ta}")
company.write("\nDa           : "f"{Da}")
company.write("\nHra          : "f"{Hra}")
company.write("\nPf           : "f"{Pf}")
company.write("\nSalary       : "f"{salary}")
company.write("\nTotal Salary : "f"{Total}")
company.write("\n************************************************************")


company.close()
print("Value is Added!!")
'''
name = open("name.txt", "w")
name.write(input("Enter your Name : "))
name.close()

id_ = open("ID.txt", "w")
id_.write(input("Enter your ID : "))
id_.close()

position = open("position.txt", "w")
position.write(input("Enter your Position : "))
position.close()

mobile = open("mobile.txt", "w")
mobile.write(input("Enter your Mobile Number : "))
mobile.close()

email_id = open("Email_id", "w")
email_id.write(input("Enter your Email-id : "))
email_id.close()

address = open("address.txt", "w")
address.write(input("Enter your Address : "))
address.close()

salary = open("salary.txt", "w")
salary.write(input("Enter your Salary : "))
salary.close()

ta = open("TA.txt", "w")
ta.write(input("Enter your TA : "))
ta.close()

da = open("DA.txt", "w")
da.write(input("Enter your DA : "))
da.close()

hra = open("hra.txt", "w")
hra.write(input("Enter your HRA : "))
hra.close()

pf = open("pf.txt", "w")
pf.write(input("Enter your PF : "))
pf.close()

'''

