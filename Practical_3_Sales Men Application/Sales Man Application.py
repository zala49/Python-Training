# Sales Man Application

from datetime import date

NAME = input("Enter Sales Man Name : ")
ID = input("Enter Sales Man ID : ")
Route = "Mahemdavad to Maninager"
JOINING_DATE = "01/01/2022"
CURRENT_DATE = date.today()

Salary = int(input("Enter your salary : "))
Total_Sale = int(input("Enter Total Sale : "))
Commission_rate = int(input("Enter the commission rate : "))

Commission = Total_Sale * Commission_rate / 100

Total = Commission + Salary

print("-------------------------------------------------------------")
print("\t\t\t\t\tSALES MAN REPORT\t\t\t\t\t")
print("-------------------------------------------------------------")
print("\t\tNAME            : ", NAME)
print("\t\tID              : ", ID)
print("\t\tJoining_Date    : ", JOINING_DATE)
print("\t\tCurrent_Date    : ", CURRENT_DATE)
print("\t\tRoute           : ", Route)
print("-------------------------------------------------------------")
print("\t\t\t\t\tCOMMISION\t\t\t\t\t")
print("-------------------------------------------------------------")
print("\t\tSalary is       : ", Salary)
print("\t\tCommission is   : ", Commission)
print("\t\tTotal Salary is : ", Total)
print("------------------------------------------------------------")
