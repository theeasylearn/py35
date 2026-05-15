# Without return value without argument
def printLine():
    print("-"*100)
    return 
# Without return value with argument 
def printLetter(letter,times):
    print(letter*times)
    return 
#  With return value without argument
def getPi():
    #local variable 
    pi = 22/7
    return pi

#we must call/run/execute/use  function
printLine()

printLetter('*',70)
print("the easylearn academy")
printLetter('~',100)

pi = getPi()
print("value of pi ",pi)