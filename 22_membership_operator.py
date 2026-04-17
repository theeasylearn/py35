#example of membership operator

numbers = [100,500,300,1000,800]

a = 100 
b = 490
result = a in numbers
print(f"{a} in list exists = {result}") 


result = 150 in numbers
print(f"150 in list exists = {result}") 


result = b not in numbers
print(f"{b} in list exists = {result}") 


result = 100 not in numbers
print(f"100 in list exists = {result}") 


favourite_fruit = 'apple'
fruits = "banana mango pineapple apple "
result = favourite_fruit in fruits
print(result)

result = favourite_fruit not in fruits
print(result)
