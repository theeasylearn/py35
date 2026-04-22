#example of if statement 
#write a program to findout and display cube of given positive number 
number = int(input("Enter number"))

#check if the number is negative, convert it into positive number 
if number<0: # == != < <= >=
    print("it is negative number, so let us convert it into positive number")
    number = 0 - number
    print("now number is ",number)
cube = number * number * number
print("cube is ",cube)
