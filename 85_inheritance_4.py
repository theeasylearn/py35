#example of single level inheritance 
# parent/super/base class
class Human:
    def eat(self):
        print("I can eat vegetables")
    def sleep(self):
        print("I can sleep")

class Robot:
    def work(self):
        print("I can work")
    def speak(self):
        print("i can speak like human")


class Humanoid(Human,Robot): 
    def walk(self):
        print("I can walk")
    def watch(self):
        print("I can watch")
    def WhatICanDo(self):
        #calling parent class function 
        super().eat()
        super().sleep()
        super().work()
        super().speak()
        #calling our own function 
        self.walk()
        self.watch()
    
#create object of Humanoid class 

h1 = Humanoid()
h1.WhatICanDo()
