from datetime import datetime as dt 

#create datetime type object 
dt = dt.now()

husband_date = input("Enter husband's birthdate")
wife_date = input("Enter wife's birthdate")

#convert string into date 
date1 = dt.strptime(husband_date,"%d-%m-%Y")
date2 = dt.strptime(wife_date,"%d-%m-%Y")

if date1<date2:
    print("Husband is older and wife is younger")
else:
    print("Husband is younger and wife is older")