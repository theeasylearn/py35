'''
    write a program to findout tallest person from 3 persons height given by user 
'''
height1 = float(input("Enter 1st person height in foot and inch"))
height2 = float(input("Enter 2nd person height in foot and inch"))
height3 = float(input("Enter 3rd person height in foot and inch"))

if height1>height2: 
    #compare height1 and height 3
    if height1>height3:
        print("1st person is tallest person")
    else:
        print("3rd person is tallest person")
else:
    if height2>height3:
        print("2nd person is tallest person")
    else:
        print("3rd person is tallest person")    

print("Good bye.")