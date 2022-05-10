import Stock_Available

# Total item
Total_Stock = int(input("Enter total item : "))
print("\nEnter your D-Mart items below here\n")
item_list = []
for x in range(0, Total_Stock):
    item = input(F"Enter item{x} : ")
    item_list.append(item)
print(item_list)

# Stock
stock = []
print("\nEnter the stock of items \n")
for x in range(0, Total_Stock):
    list_stock = int(input(F"Enter the stock of {item_list[x]} : "))
    stock.append(list_stock)
print(stock)

# Arriving Price of Stock
Arriving_Price = []
for i in range(0, Total_Stock):
    arriving_price = int(input(F"Enter the arriving price of {item_list[x]} : "))
    Arriving_Price.append(arriving_price)
print(Arriving_Price)

# Selling Price of Stock
Selling_price = []
for x in range(0, Total_Stock):
    selling_item = int(input(F"Enter the selling price of {item_list[x]} : "))
    Selling_price.append(selling_item)
print(Selling_price)

# Sold items
Sold_items = []
print('\nEnter your sold item \n')
for x in range(0, Total_Stock):
    sold_count = int(input(F"Enter the item {item_list[x]} sold : "))
    Sold_items.append(sold_count)
print(Sold_items)

# Available Stock
Available = []
for x in range(0, Total_Stock):
    available_stock = stock[x] - Sold_items[x]
    Available.append(available_stock)
print(Available)

Commission = []
for x in range(0, Total_Stock):
    commissions = (Sold_items[x] * Selling_price[x]) / 0.1
    Commission.append(commissions)

# salesman information
Salesman = input("\nEnter salesman Name : ")

print("")
print("*"*50)
Stock_Available.available(item_list, available_stock)

print('*'*50)
for x in range(0, Total_Stock):
    Stock_Available.item_show(item_list[x], item_list[x], Selling_price[x])

print('*'*50)
for x in range(0, Total_Stock):
    Stock_Available.total_commission(item_list[x], Commission[x])
