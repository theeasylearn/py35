from datetime import datetime as dt 
from datetime import timedelta 
#create datetime type object 
dt = dt.now()

recharge_date = input("Enter recharge date (%d-%m-%Y)")
no_of_days = int(input("Enter days"))

#convert string into date 
date1 = dt.strptime(recharge_date,"%d-%m-%Y")

#add days into date using timedelta
expiry_date = date1 + timedelta(days=no_of_days)

#convert date into indian format 
print(expiry_date.strftime("%d-%m-%Y"))

