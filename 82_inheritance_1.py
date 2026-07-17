#example of single level inheritance 
# parent/super/base class
class Human:
    def walk(self):
        print("I can walk fast")
    def talk(self):
        print("I can talk nice")
    def eat(self):
        print("I can eat vegetables")

#derived/child/sub class
#inheritance
class Student(Human):
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

#create child class object
# object = className()
pratham = Student()
pratham.WhatICanDo()
print("-"*100)
pratham.read()
pratham.write()
# calling parent class method using child class object
print("-"*100)
pratham.walk()
pratham.talk()
pratham.eat()




    