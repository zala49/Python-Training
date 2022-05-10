import info_input

Youtube_file = open("Youtube_file.txt", "a")
Youtube_Normal = open("Youtube_normal.txt", "w")
Youtube_Prime = open("Youtube_Prime.txt", "w")


class Youtube:
    def youtube_ad(self):
        Youtube_file.write("Advertisement of Youtube!!\n")
        Youtube_file.write("Ad Name          : "f"{info_input.Title_ad}\n")
        Youtube_file.write("Details          : "f"{info_input.Details_ad}\n")
        Youtube_file.write("Price of Product : "f"{info_input.Price_ad}\n")

    def youtube_normal_prime(self):
        if info_input.user_input == 1:
            Youtube_Normal.write("Time = 1 AM to 4 AM(PHASE_1)\n")
            Youtube_Normal.write("Advertisement of Youtube!!\n")
            Youtube_Normal.write("Ad Name                   : "f"{info_input.Title_ad}\n")
            Youtube_Normal.write("Details                   : "f"{info_input.Details_ad}\n")
            Youtube_Normal.write("Price of Product          : "f"{info_input.Price_ad}\n")
        elif info_input.user_input == 2:
            Youtube_Normal.write("Time = 4 AM to 8 AM(PHASE_2)\n")
            Youtube_Normal.write("Advertisement of Youtube!!\n")
            Youtube_Normal.write("Ad Name                   : "f"{info_input.Title_ad}\n")
            Youtube_Normal.write("Details                   : "f"{info_input.Details_ad}\n")
            Youtube_Normal.write("Price of Product          : "f"{info_input.Price_ad}\n")
        elif info_input.user_input == 3:
            Youtube_Normal.write("Time = 8 AM to 12 AM(PHASE_3)\n")
            Youtube_Normal.write("Advertisement of Youtube!!\n")
            Youtube_Normal.write("Ad Name                   : "f"{info_input.Title_ad}\n")
            Youtube_Normal.write("Details                   : "f"{info_input.Details_ad}\n")
            Youtube_Normal.write("Price of Product          : "f"{info_input.Price_ad}\n")
        elif info_input.user_input == 4:
            Youtube_Normal.write("Time = 12 PM to 4 PM(PHASE_4)\n")
            Youtube_Normal.write("Advertisement of Youtube!!\n")
            Youtube_Normal.write("Ad Name                   : "f"{info_input.Title_ad}\n")
            Youtube_Normal.write("Details                   : "f"{info_input.Details_ad}\n")
            Youtube_Normal.write("Price of Product          : "f"{info_input.Price_ad}\n")
        elif info_input.user_input == 5:
            Youtube_Normal.write("Time = 4 PM to 8 PM(PHASE_5)\n")
            Youtube_Normal.write("Advertisement of Youtube!!\n")
            Youtube_Normal.write("Ad Name                   : "f"{info_input.Title_ad}\n")
            Youtube_Normal.write("Details                   : "f"{info_input.Details_ad}\n")
            Youtube_Normal.write("Price of Product          : "f"{info_input.Price_ad}\n")
        elif info_input.user_input == 6:
            Youtube_Normal.write("Time = 8 PM to 12 PM(PHASE_6)\n")
            Youtube_Prime.write("Advertisement of Youtube!!\n")
            Youtube_Prime.write("Ad Name                   : "f"{info_input.Title_ad}\n")
            Youtube_Prime.write("Details                   : "f"{info_input.Details_ad}\n")
            Youtube_Prime.write("Price of Product          : "f"{info_input.Price_ad}\n")
        else:
            print("Enter Valid Input!!")


obj = Youtube()
obj.youtube_normal_prime()
obj.youtube_ad()
