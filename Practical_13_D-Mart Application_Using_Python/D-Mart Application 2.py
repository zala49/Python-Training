import Stock_Available

Stock = ['Shampoo', 'Brush', 'Oil', 'Pen', 'Paper', 'Books', 'Shirt', 'T-Shit', 'Pent', 'Watch']

Shampoo = int(input("Enter the Stock of " f"{Stock[0]} : "))
Brush = int(input("Enter the Stock of " f"{Stock[1]} : "))
Oil = int(input("Enter the Stock of " f"{Stock[2]} : "))
Pen = int(input("Enter the Stock of " f"{Stock[3]} : "))
Paper = int(input("Enter the Stock of " f"{Stock[4]} : "))
Books = int(input("Enter the Stock of " f"{Stock[5]} : "))
Shirt = int(input("Enter the Stock of " f"{Stock[6]} : "))
T_Shirt = int(input("Enter the Stock of " f"{Stock[7]} : "))
Pent = int(input("Enter the Stock of " f"{Stock[8]}  : "))
Watch = int(input("Enter the Stock of " f"{Stock[9]} : "))

# Arriving Price
Shampoo_Price_1 = int(input("Enter the Arriving Price of " f"{Stock[0]} : "))
Brush_Price_1 = int(input("Enter the Arriving Price of " f"{Stock[1]} : "))
Oil_Price_1 = int(input("Enter the Arriving Price of " f"{Stock[2]} : "))
Pen_Price_1 = int(input("Enter the Arriving Price of " f"{Stock[3]} : "))
Paper_Price_1 = int(input("Enter the Arriving Price of " f"{Stock[4]} : "))
Books_Price_1 = int(input("Enter the Arriving Price of " f"{Stock[5]} : "))
Shirt_Price_1 = int(input("Enter the Arriving Price of " f"{Stock[6]} : "))
T_Shirt_Price_1 = int(input("Enter the Arriving Price of " f"{Stock[7]} : "))
Pent_Price_1 = int(input("Enter the Arriving Price of " f"{Stock[8]} : "))
Watch_Price_1 = int(input("Enter the Arriving Price of " f"{Stock[9]} : "))

# Selling Price
Shampoo_Price_2 = int(input("Enter the Selling Price of " f"{Stock[0]} : "))
Brush_Price_2 = int(input("Enter the Selling Price of " f"{Stock[1]} : "))
Oil_Price_2 = int(input("Enter the Selling Price of " f"{Stock[2]} : "))
Pen_Price_2 = int(input("Enter the Selling Price of " f"{Stock[3]} : "))
Paper_Price_2 = int(input("Enter the Selling Price of " f"{Stock[4]} : "))
Books_Price_2 = int(input("Enter the Selling Price of " f"{Stock[5]} : "))
Shirt_Price_2 = int(input("Enter the Selling Price of " f"{Stock[6]} : "))
T_Shirt_Price_2 = int(input("Enter the Selling Price of " f"{Stock[7]} : "))
Pent_Price_2 = int(input("Enter the Selling Price of " f"{Stock[8]} : "))
Watch_Price_2 = int(input("Enter the Selling Price of " f"{Stock[9]} : "))

Shampoo_Sell = int(input("Enter the Sell item of " f"{Stock[0]} : "))
Brush_Sell = int(input("Enter the Sell item of " f"{Stock[1]} : "))
Oil_Sell = int(input("Enter the Sell item of " f"{Stock[2]} : "))
Pen_Sell = int(input("Enter the Sell item of " f"{Stock[3]} : "))
Paper_Sell = int(input("Enter the Sell item of " f"{Stock[4]} : "))
Books_Sell = int(input("Enter the Sell item of " f"{Stock[5]} : "))
Shirt_Sell = int(input("Enter the Sell item of " f"{Stock[6]} : "))
T_Shirt_Sell = int(input("Enter the Sell item of " f"{Stock[7]} : "))
Pent_Sell = int(input("Enter the Sell item of " f"{Stock[8]} : "))
Watch_Sell = int(input("Enter the Sell item of " f"{Stock[9]} : "))

A = Stock_Available.sell(Shampoo, Shampoo_Sell)
B = Stock_Available.sell(Brush, Brush_Sell)
C = Stock_Available.sell(Oil, Oil_Sell)
D = Stock_Available.sell(Pen, Pent_Sell)
E = Stock_Available.sell(Paper, Paper_Sell)
F = Stock_Available.sell(Books, Books_Sell)
G = Stock_Available.sell(Shirt, Shirt_Sell)
H = Stock_Available.sell(T_Shirt, T_Shirt_Sell)
i = Stock_Available.sell(Pent, Pent_Sell)
J = Stock_Available.sell(Watch, Watch_Sell)

a = Stock_Available.incentive(Shampoo_Price_2, Shampoo_Sell, 10)
b = Stock_Available.incentive(Brush_Price_2, Brush_Sell, 10)
c = Stock_Available.incentive(Oil_Price_2, Oil_Sell, 10)
d = Stock_Available.incentive(Pen_Price_2, Pen_Sell, 10)
e = Stock_Available.incentive(Paper_Price_2, Paper_Sell, 10)
f = Stock_Available.incentive(Books_Price_2, Books_Sell, 10)
g = Stock_Available.incentive(Shirt_Price_2, Shirt_Sell, 10)
h = Stock_Available.incentive(T_Shirt_Price_2, T_Shirt_Sell, 10)
ii = Stock_Available.incentive(Pent_Price_2, Pent_Sell, 10)
j = Stock_Available.incentive(Watch_Price_2, Watch_Sell, 10)


def module(shampoo, brush, oil, pen, paper, books, shirt, t_shirt, pent, watch):
    print("\t\t*******************AVAILABLE STOCK************************")
    print("\t\tShampoo  : " f"{A} ")
    print("\t\tBrush    : " f"{B} ")
    print("\t\tOil      : " f"{C}")
    print("\t\tPen      : " f"{D}")
    print("\t\tPepar    : " f"{E}")
    print("\t\tBooks    : " f"{F}")
    print("\t\tShirt    : " f"{G}")
    print("\t\tt_Shirt  : " f"{H}")
    print("\t\tPent     : " f"{i}")
    print("\t\tWatch    : " f"{J}")
    print("\t\t*******************ARRIVING PRICE WITH SELLING PRICE************************")
    print("\t\t" f"{Stock[0]}", "Arriving Price " f"{Shampoo_Price_1}", "Selling Price " f"{Shampoo_Price_2}")
    print("\t\t" f"{Stock[1]}", "Arriving Price " f"{Brush_Price_1}", "Selling Price " f"{Brush_Price_2}")
    print("\t\t" f"{Stock[2]}", "Arriving Price " f"{Oil_Price_1}", "Selling Price " f"{Oil_Price_2}")
    print("\t\t" f"{Stock[3]}", "Arriving Price" f"{Pen_Price_1}", "Selling Price " f"{Pen_Price_2}")
    print("\t\t" f"{Stock[4]}", "Arriving Price " f"{Paper_Price_1}", "Selling Price " f"{Paper_Price_2}")
    print("\t\t" f"{Stock[5]}", "Arriving Price " f"{Books_Price_1}", "Selling Price " f"{Books_Price_2}")
    print("\t\t" f"{Stock[6]}", "Arriving Price " f"{Shirt_Price_1}", "Selling Price " f"{Shirt_Price_2}")
    print("\t\t" f"{Stock[7]}", "Arriving Price " f"{T_Shirt_Price_1}", "Selling Price " f"{T_Shirt_Price_2}")
    print("\t\t" f"{Stock[8]}", "Arriving Price " f"{Pent_Price_1}", "Selling Price " f"{Pent_Price_2}")
    print("\t\t" f"{Stock[9]}", "Arriving Price " f"{Watch_Price_1}", "Selling Price " f"{Watch_Price_2}")
    print("\t\t*******************TOTAL COMMISION************************")
    print("\t\t" f"{Stock[0]}", "Commision is = " f"{a}")
    print("\t\t" f"{Stock[1]}", "Commision is = " f"{b}")
    print("\t\t" f"{Stock[2]}", "Commision is = " f"{c}")
    print("\t\t" f"{Stock[3]}", "Commision is = " f"{d}")
    print("\t\t" f"{Stock[4]}", "Commision is = " f"{e}")
    print("\t\t" f"{Stock[5]}", "Commision is = " f"{f}")
    print("\t\t" f"{Stock[6]}", "Commision is = " f"{g}")
    print("\t\t" f"{Stock[7]}", "Commision is = " f"{h}")
    print("\t\t" f"{Stock[8]}", "Commision is = " f"{ii}")
    print("\t\t" f"{Stock[9]}", "Commision is = " f"{j}")


module(Shampoo, Brush, Oil, Pen, Paper, Books, Shirt, T_Shirt, Pent, Watch)
