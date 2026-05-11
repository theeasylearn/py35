# using for loop on string variable
#count vowels in string 
# Vowels = A E I O U 

line = input("Enter your name")

vowels = 0
for letter in line:
    if letter == 'a' or letter =='e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'A' or letter =='E' or letter == 'I' or letter == 'O' or letter == 'U':
        vowels= vowels + 1

print("_"*100) 
print(vowels)