Employee_file = open("Employee_file.txt", "w")


class Employee:
    COMPANY_NAME = input("Enter Your Company Name : ")
    Name = input("Enter Employee Name : ")
    ID = input("Enter Employee Id : ")
    Position = input("Enter Employee Position : ")
    Mobile = int(input("Mobile Number : "))
    Address = input("Enter Employee Address : ")
    Email_id = input("Employee Email id : ")
    Salary = int(input("Enter Employee Salary : "))
    TA = (0.02 * Salary)
    DA = (0.05 * Salary)
    HRA = (0.2 * Salary)
    PF = (0.18 * Salary)
    Net = (Salary + TA + DA + HRA)
    Total = (Net - PF)


class Employee_2(Employee):
    def showdetails(self):
        Employee_file.write("\nCompany Name             : "f"{Employee.COMPANY_NAME}")
        Employee_file.write("\nName                     : "f"{Employee.Name}")
        Employee_file.write("\nID                       : "f"{Employee.ID}")
        Employee_file.write("\nPosition                 : "f"{Employee.Position}")
        Employee_file.write("\nMobile No                : "f"{Employee.Mobile}")
        Employee_file.write("\nAddress                  : "f"{Employee.Address}")
        Employee_file.write("\nEmail_Id                 : "f"{Employee.Email_id}")
        Employee_file.write("\nTA                       : "f"{Employee.TA}")
        Employee_file.write("\nDA                       : "f"{Employee.DA}")
        Employee_file.write("\nHRA                      : "f"{Employee.HRA}")
        Employee_file.write("\nPF                       : "f"{Employee.PF}")
        Employee_file.write("\nSalary                   : "f"{Employee.Net}")
        Employee_file.write("\nSalary                   : "f"{Employee.Salary}")
        Employee_file.write("\nTotal Salary             : "f"{Employee.Total}")


obj = Employee_2()
obj.showdetails()
