#Hierarchical inheritance 
class Student: # level 2
    def read(self):
        print("I can read")
    def write(self):
        print("I can write")

class Commerce(Student):
    def accounting(self):
        print("I can do accounting")
    def marketing(self):
        print("I can do marketing")

class Arts(Student):
    def drawing(self):
        print("i can draw pictures")
    def acting(self):
        print("I can do acting in dramas")
    

mohan = Commerce()
mohan.accounting()
mohan.marketing()
mohan.read()
mohan.write()


rita = Arts()
rita.drawing()
rita.acting()
rita.read()
rita.write()
rita.accounting() #error
