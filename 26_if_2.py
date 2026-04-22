#write a program to findout profit or loss amount using user given purchase & sale price of the product 
purchase_price = float(input("Enter product purchase price"))
sales_price = float(input("Enter product sales price"))
#process 
difference = sales_price - purchase_price
if difference>0: # == != < > <= >= 
    print("profit amount is ",difference)

if difference<0:
    print("loss amount is ",difference)

if difference==0:
    print("no profit no loss")

print("good bye.")