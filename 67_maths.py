import math 

#accept one number from user 
num = float(input("Enter a number: "))

#generate and store ceil value 
ceil_value = math.ceil(num)
#generate and store floor value
floor_value = math.floor(num)
#generate store round value using trunc 
round = math.trunc(num)
#display the values 
print("Ceil value of", num, "is: ", ceil_value)
print("Floor value of", num, "is: ", floor_value)
print("Round value of", num, "is: ", round)
#find and print absolute value of the number
abs_value = math.fabs(num)
print("Absolute value of ", num, "is: ", abs_value)
#use modf function and display it   
modf_value = math.modf(num)
print("Fractional and integer parts of ", num, "are: ", modf_value)
#find factorial of the number and display it
num_int = int(num)
if num_int >= 0:
    factorial_value = math.factorial(num_int)
    print("Factorial of ", num_int, "is: ", factorial_value)
else:    
    print("Factorial is not defined for negative numbers.")
print(" reminder of 10 divided by 3 is: ", math.fmod(10, 3))
x = -10
y = 1
#use copysign to get the value of x with the sign of y
copysign_value = math.copysign(x, y)    
print("Value of x with the sign of y is: ", copysign_value)
#math library constants
print("Value of pi is: ", math.pi)
print("Value of e is: ", math.e)
#trigonometric functions (all example with dynamic input)   
angle = float(input("Enter an angle in degrees: "))
#convert angle to radians
radians = math.radians(angle)
print("Sine of ", angle, "degrees is: ", math.sin(radians))
print("Cosine of ", angle, "degrees is: ", math.cos(radians))
print("Tangent of ", angle, "degrees is: ", math.tan(radians))
