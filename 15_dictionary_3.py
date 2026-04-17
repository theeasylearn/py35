student = {'name':'pratham','age':16,'gender':True,'weight':70.25}

print(student)
#copy dictionary into another dictionary
student2 = student.copy()
print(student2)

#remove all key value pair 
student2.clear()
print(student2)

#print only keys 
print(student.keys())

#print values 
print(student.values())

player = ['name','match','runs','age']
print(player)

#create dictionary 
kohli = dict.fromkeys(player)
kohli['name'] = 'Virat Kohli'
kohli['match'] = 400
kohli['runs'] = 14000
kohli['age'] = 36
print(kohli)

#delete age key and value
kohli.pop('age')
print(kohli)

#remove last key value pair
kohli.popitem()
print(kohli)

kohli.update({'name':'King kohli'})
kohli.update({'team':'india'})
print(kohli.get("city"))
print(kohli.get("name"))
print(kohli)