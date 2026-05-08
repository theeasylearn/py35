# write a program how odd and even value in list 
list = [24, 93, 46, 93, 76, 55, 99, 50, 92, 42, 64, 48, 68, 18, 99, 60, 97, 76, 94, 18, 15, 55, 57, 91, 76, 72, 18, 92, 28, 14, 37, 77, 50, 65, 18, 63, 95, 38, 20, 90, 51, 50, 30, 10, 91, 14, 67, 17, 64, 70]

#chain assignment
odd = even = 0 
for number in list:
    print(number)
    reminder = number % 2
    if reminder == 0:
        even = even + 1 
    else:
        odd = odd + 1

print("odd count = ",odd)
print("even count = ",even)

