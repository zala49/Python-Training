# Commission Management System

from datetime import date

ID = int(input("Enter Your Id : "))
NAME = input("Enter Sales Man Name : ")
SHOP_NAME = "D A Degree Engineering"
JOINNING_DATE = "2022-01-01"
CURRENT_DATE = date.today()
SALARY = 30000

ITEM1 = "Laptop"
TOTAL_ITEM1 = int(input("Total sale laptop : "))
LAPTOP_COMMISSION = TOTAL_ITEM1 * 50000 * 0.05

ITEM2 = "Mouse"
TOTAL_ITEM2 = int(input("Total sale mouse : "))
MOUSE_COMMISSION = TOTAL_ITEM2 * 500 * 0.05

TOTAL_SALE = TOTAL_ITEM1 + TOTAL_ITEM2
TOTAL_COMMISSION = LAPTOP_COMMISSION + MOUSE_COMMISSION
TOTAL_SALARY = SALARY + TOTAL_COMMISSION

print("\n\t***************************************\n\t\t\t\t\tSALE REPORT \n\t***************************************")

print("\t\tName              : ", NAME)
print("\t\tSales man id      : ", ID)
print("\t\tShop name         : ", SHOP_NAME)
print("\t\tJoining date      : ", JOINNING_DATE)
print("\t\tCurrent date      : ", CURRENT_DATE)
print("\t\tSalary            : ", SALARY)
print("\t**************************************\n\t\t\t\t\tTOTAL SALE TODAY \n\t**************************************")
print("\t\tTotal sale        : ", TOTAL_SALE)
print("\t***************************************\n\t\t\t\t\tCOMMISION \n\t***************************************")
print("\t\tTotal commission  : ", int(TOTAL_COMMISSION))
print("\t\tTotal salary      : ", TOTAL_SALARY)
print("\t***************************************")
