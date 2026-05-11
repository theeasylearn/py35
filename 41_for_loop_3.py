# using for loop on string variable

line = input("Enter your name")

#print each and every letter on new line using for loop and also count no of letters 
count = 0
for letter in line:
    print(letter)
    count = count + 1

print("_"*100) 
print(count)