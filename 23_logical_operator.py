num1 = 10
num2 = 20
num3 = 30

#check num1  is less then num2 and num2 is less then num3 
result = num1<num2 and num2<num3 
print(f"{result}  {num1}<{num2} and {num2}<{num3}")

#check num1 and num2 are same and num2 and num3 are same 
result = num1==num2 and num2==num3 
print(f"{result}  {num1}=={num2} and {num2}=={num3}")

#check num3 bigger then num2 and num2 is less then num1 
result = num3 > num2 and num2<num1 
print(f"{result}  {num3}>{num2} and {num2}<{num1}")

#check num1 less then num2 or num2 greater then num3
result = num1 < num2 or num2 > num3 
print(f"{result}  {num1}<{num2} or {num2}>{num3}")

#check num1 and num2 same  or num2 and num3 are same
result = num1 == num2 or num2 == num3 
print(f"{result}  {num1}=={num2} or {num2}=={num3}")

result = not (num1 == num2) 
print(f"{result} = not {num1} == {num2} ")