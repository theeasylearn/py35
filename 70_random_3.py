import random as rd 
#create list that has 10 fruits name in a to z order
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon']

#create list that has 10 nuts name in a to z order (proper nuts, not fruits that are called nuts )
nuts = ['almond', 'brazil nut', 'cashew', 'hazelnut', 'macadamia', 'pecan', 'pistachio', 'walnut', 'pine nut', 'chestnut']

print("original fruits list: ", fruits)
print("original nuts list: ", nuts)

#pick one random fruit from the fruits list
random_fruit = rd.choice(fruits)
print("random fruit: ", random_fruit)

#pick two random nuts from the nuts list
random_nuts = rd.choices(nuts, k=2)
print("random nuts: ", random_nuts)

#shuffle original list fruit 
rd.shuffle(fruits)
print("shuffled fruits list: ", fruits)

#copy shuffle list to new list
nut2 = rd.sample(nuts,k=len(nuts))
print("shuffled nuts list: ", nut2)