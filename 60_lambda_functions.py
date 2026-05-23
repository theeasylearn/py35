# def getInterest(amount,rate,year):
#     interest = (amount * rate * year) / 100
#     return interest
# or 
getInterest = lambda amount,rate,year : ((amount * rate * year ) / 100)
a = float(input("Enter amount: "))
r = float(input("Enter rate of interest: "))
y = int(input("Enter number of years: "))

toCelsius = lambda fahrenheit : (5/9) * (fahrenheit - 32)

print(getInterest(amount=a,year=y,rate=r))

f = float(input("Enter fahrenheit"))
print("Celsius = ",toCelsius(fahrenheit=f))
