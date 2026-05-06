#write a program to display power of given base and exponent 
'''
    base = 2 exponent = 5 
    process = 2 x 2 x 2 x 2 x 2 
    answer = 32 
'''
base = int(input("Enter base"))
exponent = int(input("Enter exponent"))

answer = 1

while exponent>=1:
    answer = base * answer #2
    exponent=exponent-1

print(answer)

