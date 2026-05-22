def sayHello(*names):
    count = 0
    for name in names:
        print(name,end=' ')
        count= count + 1
    print("Count = ",count)
sayHello("ghanshyam","Nilkanth","sahaj")