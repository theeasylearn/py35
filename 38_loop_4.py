#write a program to figure out whether given number  is prime number or not

number = 5
divisor = 2

reminder = number % divisor
print(reminder)
if reminder==0:
    print("it is not prime number")
divisor = divisor + 1 #3
reminder = number % divisor
print(reminder)
if reminder==0:
    print("it is not prime number")
