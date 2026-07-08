from datetime import datetime as dt 

#create datetime type object 
dt = dt.now()

print("Date ", dt.day)
print("Month ", dt.month)
print("Year ", dt.year)
print("weekday ", dt.weekday())
week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
today = week[dt.weekday()] + " " + str(dt.day) + "/" + str(dt.month) + "/" + str(dt.year)
print(today)

print("hours ",dt.hour)
print("minutes ",dt.minute)
print("seconds ",dt.second)
current_time = str(dt.hour) + ":" + str(dt.minute) + ":" + str(dt.second)
print(current_time)