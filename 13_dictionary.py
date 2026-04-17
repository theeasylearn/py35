# create dictionary 
student = {'name':'pratham','age':16,'gender':True,'weight':70.25}

print(student)
print(student['name'])
print(student['weight'])
print(student['gender'])
print(student['age'])

#update value
#update name to pratham patel
student['name'] = "Pratham Patel"

#insert new key value pair
student['city'] = 'bhavnagar'

print(student)

#remove key and value
del student['gender']
# del student['email'] we can delete non existing key 
# print(student['email']) we cant access non existing key
print(student)
print("Good bye.")