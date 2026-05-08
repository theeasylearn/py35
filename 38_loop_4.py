#write a program to figure out whether given number  is prime number or not

number = int(input("Enter number"))
divisor = 2
if number%2==0:
    print("it is not prime number")
else:
    half = number // 2
    while divisor<=half:
        reminder = number % divisor
        # print(reminder)
        if reminder==0:
            break #loop stop 
        divisor = divisor + 1 #3

    if divisor > half:
        print("it is prime number")
    else:
        print("it is not prime number")

