# Slicing Using User's input
String = "     The word pollution was derived from the Latin word pollution,which means to make dirty. Pollution is the process of making the environment pollute the water and the air by adding harmful substances.      Pollution causes an imbalance in the environment.This report is produced by researchers at Yale and Columbia University in association with the World Economic Forum.Industrial development and the green revolution have had a negative impact on the environment.These changes could be in the physical, chemical or biological characteristics of air or water that are harmful to human life and other living things. Population explosion, rapid industrialization, deforestation, unplanned urbanization, scientific and technological advancement, etc. The main causes of environmental pollution."
Starting = int(input("Enter the Starting Position you want to slice : "))
Ending = int(input("Enter the Ending Position of Slice : "))
s1 = slice(Starting)
s2 = slice(Ending)
print(String)
print(String[s1])
print((String[s2]))
print("\n")

# Find the length
Len = String[s2]
print("Your Output's Length is : ", len(Len))
print("\n")

# Remove useless Space
print(String[s2].strip())
print("\n")

# Convert into LowerCase and UpperCase
Lower = input("Do You Want all character into LowerCase : ").upper()
if Lower == "YES" or Lower == "Y":
    print("Your LowerCase String is :")
    print((String[s2].strip().lower()))
    print("\n")
else:
    pass
Upper = input("Do You Want all Character into Uppercase : ").upper()
if Upper == "YES" or Upper == "Y":
    print("Your UpperCase String is :")
    print((String[s2].strip().upper()))
    print("\n")
else:
    pass

# Replacing Word
Replace = String[s2].strip()
Replace_int = input("Enter the word you want to replace : ")
Replace_int2 = input("Enter the word you want to replace with : ")
print("Your Replaced Value is : ")
print(Replace.replace(Replace_int, Replace_int2))
print("\n")

# Split Function
Split = String[s2].strip()
print("Your Value After the Spliting : ")
print(Split.split())
print(Split.split(","))
print("\n")

# Add String
Add = input("Do you want to add any string or number Yes or No : ").upper()
if Add == "YES" or "Y":
    Add2 = input("Enter the new String/Number : ")
else:
    pass

# Concat
Final_String = String[s2].strip() + ' ' + Add2
print("Your Final String is : ")
print(Final_String)
print("\n")
