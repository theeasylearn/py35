#example of multi level inheritance 
# parent/super/base class
class Human: #level 1
    def walk(self):
        print("I can walk fast")
    def talk(self):
        print("I can talk nice")
    def eat(self):
        print("I can eat vegetables")

#derived/child/sub class
#inheritance
class Student(Human): # level 2
    def read(self):
        print("I can read")
    def write(self):
        print("I can write")
    def WhatICanDo(self):
        #calling parent class 
        super().walk()
        super().talk()
        super().eat()
        #call same class function
        self.read()
        self.write()

class Coder(Student): #level 3
    def coding(self):
        print("i can write coding")
    def debugging(self):
        print("i can debug code")
    #method Overidding
    def WhatICanDo(self):
        super().WhatICanDo()
        self.coding()
        self.debugging()
        
#create child class object
# object = className()
kabir = Coder()
kabir.WhatICanDo()
print("-"*100)
kabir.coding()
kabir.debugging()

    