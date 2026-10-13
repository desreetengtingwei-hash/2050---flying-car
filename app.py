Bananaboat = int(input("Enter the quantity of Banana Boat sold in a week:"))
Profit_bananaboat= 12 
Total_profit_bananaboat= Bananaboat*Profit_bananaboat

Chocolatecake = int(input("Enter the quantity of Chocolate Cake sold in a week:"))
Profit_chocolatecake=15
Total_profit_chocolatecake= Chocolatecake*Profit_chocolatecake

Bihungoreng= int(input("Enter the quantity of Bihun Goreng sold in a week:"))
Profit_bihungoreng=18.50
Total_profit_bihungoreng= Bihungoreng*Profit_bihungoreng

Total_profit = Total_profit_bananaboat + Total_profit_chocolatecake+ Total_profit_bihungoreng
if Total_profit >= 500:
  print ("Total profit:",Total_profit) 
  print ("Profitable")
else: 
  print("Total_profit:",Total_profit) 
  print("Non-profitable") 