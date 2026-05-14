#create(define) function 
def getSquare(number):
    #create local variable
    square = number * number
    return square

def getCube(number):
    #create local variable
    qube = number * getSquare(number)
    return qube 


num = int(input("Enter number "))
#call getSquare 
result = getSquare(num)
print("square  = ",result)

#call getCube()
result = getCube(num)
print("Cube = ",result)

