#nested dictionary
book = {} #empty dictionary
print(book)

#add new key value pair
book['name'] = "The Atomic habit"
book['price'] = 500
book['author'] = "james clear"
print(book)

#add chapter as tuple 
book['chapter'] = (1,2,3,4,5)
#add topics as list 
book['topics'] = ['introduction','index','habits','thinking','practice']

print(book)

print(book['chapter'][0]) #1
print(book['topics'][2]) #habits

book['topics'][2] = "habit, the good and bad"
print(book)
# book['chapter'][0] = 10 #error
print("good bye")