fruits = {"apple", "banana", "mango", "orange", "apple", "banana", "grapes", "kiwi", "mango", "pineapple"}

print(fruits)

#add fruits
fruits.add('jackfruit')
fruits.add('watermelon')

print(fruits)

fruits.remove('kiwi')
print(fruits)

set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}

print("Set 1:", set1)
print("Set 2:", set2)

#get unique value from both set
union = set1.union(set2)

#get common values 
intersection = set1.intersection(set1)

#get difference between set1 and set2 
difference = set1.difference(set2)

print("Union",union)
print("intersection",intersection)
print("difference",difference)

