#input always string
num1 = input("Enter 1st number") 
num2 = input("Enter 2nd number")

#convert input into integer 
num1 = float(num1)
num2 = float(num2)

#process (expression)
#variable-name1 = variable-name2 symbol(+-*/%//**) variable-name3
#addition 
add = num1 + num2 
#subtraction 
sub = num1 - num2
#multiplication 
mul = num1 * num2 
#division 
div = num1 / num2

#reminder 
reminder = num1 % num2 

#floor division (10//3 3)
result = num1 // num2 

#exponent 5*5*5
result2 = num1 ** num2 
print("addition = ",add)
print("subtraction = ",sub)
print("Multiplication = ",mul)
print("Division = ",div)
print("reminder = ",reminder)
print("floor division = ",result)
print("power = ",result2)
