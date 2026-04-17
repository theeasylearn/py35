num1 = input("Enter 1st number")
num2 = input("Enter 2nd number")

#convert input into integer 
num1 = int(num1)
num2 = int(num2)

result = num1 == num2 
# print(result," = ",num1," == ",num2)
# or
print(f"{result} = {num1} == {num2}")

result = num1 != num2 
print(f"{result} = {num1} != {num2}")

result = num1 < num2 
print(f"{result} = {num1} < {num2}")

result = num1 > num2 
print(f"{result} = {num1} > {num2}")

result = num1 <= num2 
print(f"{result} = {num1} <= {num2}")

result = num1 >= num2 
print(f"{result} = {num1} >= {num2}")