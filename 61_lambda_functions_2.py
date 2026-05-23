# def getMax(num1,num2):
#     if num1>num2:
#         return num1 
#     else: 
#         return num2 
# 
getMax = lambda num1,num2:  num1 if num1>num2 else num2

print(getMax(num1=10,num2=20))
print(getMax(num1=100,num2=50))