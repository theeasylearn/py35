#Hybrid inheritance 
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
    
class BCom(Commerce):
    def Tally(self):
        print("I can use tally software")
    def Profit(self):
        print("I can use profit software")
    def WhatICanDo(self):
        #calling parent class method 
        super().accounting()
        super().marketing()
        super().read()
        super().write()
        self.Tally()
        self.Profit()
    
b1 = BCom()
b1.WhatICanDo()

