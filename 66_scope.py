balance = 2000 #global variable as it is declared outside function 

def updateBalance(money):
    global balance #means this function can access global variable balance 
    balance = balance + money 

print("before updating balance ",balance)
money = int(input("Enter amount to update balance"))
updateBalance(money)
print("after updating balance ",balance)
