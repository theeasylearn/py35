import random as rd 
def getOTP(length=6):
    digits = "0123456789"
    OTP = ""
    for i in range(length):
        OTP= OTP+digits[rd.randint(0, 9)]
    return OTP
#generate function for random password (include lowercase, uppercase, digits and special characters)
def getRandomPassword(length=12):
    #character we can use in password
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-+"
    password = "" #empty string to store password
    size = len(characters)-1 #size of characters
    for i in range(length): #loop to generate password of given length
        password += characters[rd.randint(0,size)] #add random character to password
    return password

print("Your OTP is: ", getOTP()) #6 DIGITS
print("Your OTP is: ", getOTP(10)) #10 DIGITS
print("Your OTP is: ", getOTP(12)) #12 DIGITS
print("Your Random Password is: ", getRandomPassword()) #12 characters
print("Your Random Password is: ", getRandomPassword(16)) #16 
print("Your Random Password is: ", getRandomPassword(20)) #20 characters