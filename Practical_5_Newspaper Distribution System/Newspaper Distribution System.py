# NEWSPAPER DISTRIBUTE SYSTEM

# Newspaper Name
P1 = "Divyabhasker"
P2 = "Sandesh"
P3 = "Aconomics"
P4 = "Timesofindia"
P5 = "Sanj_Samachar"
P6 = "Jansata"

# Boys Name
Boy1 = "Shubham Patel"
Boy2 = "Aeron Mahida"

# Salary
Boy_1_Salary = 10000
Boy_2_Salary = 12000

# Quantity of Newspaper
P_1 = int(input("Enter the quantity of Divyabhasker : "))
P_2 = int(input("Enter the quantity of Sandesh : "))
P_3 = int(input("Enter the quantity of Aconomics : "))
P_4 = int(input("Enter the quantity of Timesofindia : "))
P_5 = int(input("Enter the quantity of Sanj_Samachar : "))
P_6 = int(input("Enter the quantity of Jansata : "))

# Quantity of Newspaper Provided to Boy 1
B1_Divyabhasker = int(input("Enter the Quantity of Divyabhasker to Boy 1 : "))
B1_Sandesh = int(input("Enter the Quantity of Sandesh to Boy 1 : "))
B1_Aconomics = int(input("Enter the Quantity of Aconomics to Boy 1 : "))
B1_Timesofindia = int(input("Enter the Quantity of Timesofindia to Boy 1 : "))
B1_Sanj_Samachar = int(input("Enter the Quantity of Sanj_Samachar to Boy 1 : "))
B1_Janasata = int(input("Enter the Quantity of Jansata Boy 1 : "))

# Quantity of Newspaper Provided to Boy 2
B2_Divyabhasker = int(input("Enter the Quantity of Divyabhasker to Boy 2 : "))
B2_Sandesh = int(input("Enter the Quantity of Sandesh to Boy 2 : "))
B2_Aconomics = int(input("Enter the Quantity of Aconomics to Boy 2 : "))
B2_Timesofindia = int(input("Enter the Quantity of Timesofindia to Boy 2 : "))
B2_Sanj_Samachar = int(input("Enter the Quantity of Sanj_Samachar to Boy 2 : "))
B2_Janasata = int(input("Enter the Quantity of Janasata to Boy 2 : "))


# Boy 1 have total quantity of newspaper
Total_newspaper_Boy1 = B1_Divyabhasker + B1_Sandesh + B1_Aconomics + B1_Timesofindia + B1_Sanj_Samachar + B1_Janasata
Total_newspaper_Boy2 = B2_Divyabhasker + B2_Sandesh + B2_Aconomics + B2_Timesofindia + B2_Sanj_Samachar + B2_Janasata

# Commision Rate on Newspaper
Commission_Rate = int(input('Commission on each newspaper :'))
Commission_of_Boy_1 = Total_newspaper_Boy1 + Commission_Rate / 100
Commission_of_Boy_2 = Total_newspaper_Boy2 + Commission_Rate / 100

Total_Newspaper = int(P_1 + P_2 + P_3 + P_4 + P_5 + P_6)
Sold_paper = Total_newspaper_Boy1 + Total_newspaper_Boy2
Remaining = Total_Newspaper - Sold_paper

# Total salary
Total_Salary_Boy_1 = Boy_1_Salary + Commission_of_Boy_1
Total_Salary_Boy_2 = Boy_2_Salary + Commission_of_Boy_2

print('\t========================================\n\t\t\t\tReport\n\t========================================')
print('\t========================================\n\t\t\tQuantity of NEWSPAPER\n\t========================================')
print("\tQuantity of Divyabhasker : ", P_1)
print("\tQuantity of Sandesh : ", P_2)
print("\tQuantity of Aconomics : ", P_3)
print("\tQuantity of Timesofindia : ", P_4)
print("\tQuantity of Sanj_Samachar : ", P_5)
print("\tQuantity of Janasata : ", P_6)
print('\t========================================\n\t\t\tName Of Delivery Boys\n\t========================================')
print('\tName of Delivery Boy-1 :', Boy1)
print('\tName Of Delivery Boy-2 :', Boy2)
print('\t========================================\n\t\t\t Total Quantity Of NEWSPAPER Each Have\n\t========================================')
print('\tTotal Quantity of NEWSPAPER Have Boy_1 :', Total_newspaper_Boy1)
print('\tTotal Quantity of NEWSPAPER Have Boy_2 :', Total_newspaper_Boy2)
print('\t========================================\n\t\t\tTotal Quantity of NEWSPAPERS\n\t========================================')
print('\tTotal Quantity Of NEWSPAPERS :', Total_Newspaper)
print('\t========================================\n\t\t\tQuantity  of NEWSPAPER Sold by BOYS\n\t========================================')
print('\tQuantity Of NEWSPAPER Sold by BOY_1   :', Total_newspaper_Boy1)
print('\tQuantity Of NEWSPAPER Sold by BOY_2   :', Total_newspaper_Boy2)
print('\tTotal Quantity of NEWSPAPER SOLD   :', Sold_paper)
print('\t========================================\n\t\t\tQuantity of NEWSPAPER REMAINING\n\t========================================')
print('\tQuantity of NEWSPAPER REMAINS   :', Remaining)
print('\t========================================\n\t\t\t\tSalary\n\t========================================')
print('\tSalary of BOY_1    :', Boy_1_Salary)
print('\tSalary Of BOY_2    :', Boy_2_Salary)
print('\t========================================\n\t\t\t\tCommission\n\t========================================')
print('\tCommission of BOY_1  :', Commission_of_Boy_1)
print('\tCommission of BOY_2  :', Commission_of_Boy_2)
print('\t========================================\n\t\t\t\tTotal Salary\n\t========================================')
print('\tTotal Salary Of BOY_1  :', Total_Salary_Boy_1)
print('\tTotal Salary Of BOY_2  :', Total_Salary_Boy_2)
print('\t========================================')
