# create list 
fruits = ["Apple", "Banana", "Mango", "Orange", "Pineapple", "Grapes", "Strawberry", "Watermelon", "Papaya", "Kiwi", "Peach", "Cherry", "Pear", "Plum", "Guava", "Pomegranate", "Lychee", "Apricot", "Fig", "Coconut","Mango"]
print(fruits)
#insert new fruits at end
fruits.append('Dragon fruit')

#insert new fruit at begin
fruits.insert(0,'Jackfruit')

print(fruits)
#insert new fruit at 2nd position
fruits.insert(2,'Raspberry')
print(fruits)

vegetables = ["Potato", "Tomato", "Onion", "Carrot", "Cabbage", "Cauliflower", "Spinach", "Broccoli", "Peas", "Capsicum", "Brinjal", "Radish", "Beetroot", "Cucumber", "Pumpkin", "Bottle Gourd", "Bitter Gourd", "Okra", "Sweet Corn", "Turnip"]

fruits.extend(vegetables) #add vegetables list into fruits
print(fruits)

#remove 1st fruit
fruits.pop(0)

#remove fruit named as Raspberry
fruits.remove('Raspberry') 

print("fruits after deletion ",fruits)
result = fruits.count("Mango")
print("No of mangos ",result)

#find position of Watermelon
position = fruits.index("Watermelon")
print("Position of Watermelon ",position)

fruits.sort() #sorts original list fruit into ascending order 
print(fruits)

fruits.reverse()
print(fruits)

fruits.clear() #remove all items 
print(fruits)
