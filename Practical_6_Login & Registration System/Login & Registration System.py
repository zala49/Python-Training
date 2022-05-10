# Login And Registration
import uuid
# Registration Form
print("==================================================")
print("Enter Your Details for Registration")
print("==================================================")
while True:
    name = input("Enter your name : ")
    mobile_no = input("Enter your mobile number: ")
    Email = input("Enter your email ID: ")
    if '@gmail.com' not in Email:
        print("Invalid Email Address!")
        break
    password = input("Enter your password: ")
    Position = {'super admin', 'mid admin', 'admin'}
    print("Position = ", Position)
    position = input("Enter your position: ")
    break
print("==================================================")
print('Your Registration is successful')
uuidOne = uuid.uuid1()
print("Your Unique Id is = ", uuidOne)
print("==================================================")
#    Again = (input("Do you want to fill up form again? : "))
#    if Again == "no" or Again == "n":
#        continue
#    break
Original_Name = name
Original_Password = password
UniqueId = uuidOne
name = Original_Name or UniqueId
# Login Form
print("ENTER YOUR LOGIN DETAILS")
print("==================================================")
while True:
    name = input("Enter your name/ UniqueId : ")
    password = input("Enter your password : ")
    Department = input("Enter your department : ")
    if name == Original_Name or password == Original_Password or UniqueId == uuidOne:
        if Department == position:
            print("Your are logged in : ")
            if name == Original_Name or password == Original_Password or Department == position:
                print("Press 1 to show student details")
                print("Press 2 to show admin details")
                A = int(input("Enter a number : "))
                if A == 1:
                    Student_1 = input("Enter student_1 Name : ")
                    Student_2 = input("Enter student_2 Name : ")
                    Student_3 = input("Enter student_3 Name : ")
                    Student_4 = input("Enter student_4 Name : ")
                    Student_5 = input("Enter student_5 Name : ")

                    print("Enter Student's Fees Details")

                    Student_1_Fees = input(f"Enter {Student_1}'s fee : ")
                    Student_2_Fees = input(f"Enter {Student_2}'s fee : ")
                    Student_3_Fees = input(f"Enter {Student_3}'s fee : ")
                    Student_4_Fees = input(f"Enter {Student_4}'s fee : ")
                    Student_5_Fees = input(f"Enter {Student_5}'s fee : ")

                    print("==================================================")
                    print("NAME", "\tFEES")
                    print("==================================================")
                    print(f"{Student_1}", f"\t{Student_1_Fees}")
                    print(f"{Student_2}", f"\t{Student_2_Fees}")
                    print(f"{Student_3}", f"\t{Student_3_Fees}")
                    print(f"{Student_4}", f"\t{Student_4_Fees}")
                    print(f"{Student_5}", f"\t{Student_5_Fees}")
                    print("==================================================")
                elif A == 2:
                    password = password
                    Encrypt_password = ""
                    for i in password:
                        aes_i = ord(i)
                        enc_i = aes_i + 5
                        pas_enc = chr(enc_i)
                        Encrypt_password += pas_enc
                    print("==================================================")
                    print("ADMIN DETAILS")
                    print("Name = "f"{Original_Name}")
                    print("Mobile_No = " f"{mobile_no}",)
                    print("Email = " f"{Email}")
                    print("Department = " f"{position}")
                    print("Password = ", f"{Encrypt_password}")
                    print("==================================================")
                    B = (input("Do you want to show password : ")).upper()
                    if B == "YES" or B == "Y":
                        print("This is Encrypted Password = " f"{Encrypt_password}")
                        print("For Original Password type  : ")
                        answer = (input("Enter 'Yes' or 'Y' : ")).upper()
                        if answer == "YES" or answer == "Y":
                            Decrypted_Password = ""
                            for i in Encrypt_password:
                                AES_i = ord(i)
                                dec_i = AES_i - 5
                                pass_dec = chr(dec_i)
                                Decrypted_Password += pass_dec
                            print("Your password is = "  f"{Decrypted_Password} ")
                            break
                        else:
                            print("Enter Correct Keyword!!")
                    else:
                        print("Enter Correct Keyword!!")
                else:
                    print("Please enter correct number !!")
        else:
            print("You are not belongs to this department !!")
            break
    else:
        print("Enter correct Details!!")
