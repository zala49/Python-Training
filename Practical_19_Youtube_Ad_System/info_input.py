PHASE1_NORMAL = "1-4"
PHASE2_NORMAL = "4-8"
PHASE3_NORMAL = "8-12"
Phase4_NORMAL = "12-16"
PHASE5_NORMAL = "16-20"
Phase6_PRIME = "20-24"

PHASE1_NORMAL_PRICE = 500000
PHASE2_NORMAL_PRICE = 500000
PHASE3_NORMAL_PRICE = 500000
PHASE4_NORMAL_PRICE = 500000
PHASE5_NORMAL_PRICE = 500000
PHASE6_PRIME_PRICE = 1000000

Total_Ad = int(input("Enter Total Number of AD : "))
print("\nEnter your Ads Details: \n")
Title_ad = []
for x in range(0, Total_Ad):
    Product_Name = input(F"Enter the Name of Product {x} : ")
    Title_ad.append(Product_Name)
print(Title_ad)

Details_ad = []
for x in range(0, Total_Ad):
    Details = input(F"Enter the Details {Title_ad[x]} : ")
    Details_ad.append(Details)
print(Details_ad)

Price_ad = []
for x in range(0, Total_Ad):
    Price = input(F"Enter the Price of {Title_ad[x]} : ")
    Price_ad.append(Price)
print(Price_ad)

user_input = int(input("In Which Phase Do You Want to Show Your Ad (Phase 1, Phase 2, Phase 2, Phase 3, Phase 4 , Phase 5, Phase 6): "))
