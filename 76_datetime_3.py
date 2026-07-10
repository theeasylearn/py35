from datetime import datetime as dt 
from datetime import timedelta 

#create datetime type object 
dt = dt.now()

birth_date = input("Enter birth date (%d-%m-%Y)")

#convert string into date 
date1 = dt.strptime(birth_date,"%d-%m-%Y")

today = dt.now().today() #today function return current date as date 
#calculate gap between 2 dates object
difference = today - date1  
#convert date into indian format 
print("difference in days ",difference.days)
print("difference in years ",(difference.days/365))

