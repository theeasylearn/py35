def getNSquare(x,y=2):
    print(f"x = {x} y = {y}")
    return (x*x + 2*x*y + y*y)

def getInterest(amount,rate=10.0,year=5):
    interest = (amount * rate * year) / 100
    return interest 

result = getNSquare(2,4)
print("N Square of 2 and 4",result)
print("N Square of 2 ",getNSquare(2))
print("Interest of 10000, rate = 11 year = 3 ",getInterest(10000,11,3))
print("Interest of 10000, rate = 11  ",getInterest(10000,11))
print("Interest of 10000 ",getInterest(10000))

