#crete class 
class MyMath:
    #define constructor 
    def __init__(self):
        #create instance variable 
        # self.variablename = value 
        self.num1 = 10
        self.num2 = 20
        print("constructor called automatically....")
    #define methods(function)
    def add(self):
        #create local variable 
        result = None 
        result = self.num1 + self.num2
        return result 
    def sub(self):
        #create local variable
        result = None 
        result = self.num1 - self.num2 
        return result
    
    def mul(self):
        result = self.num1 * self.num2 
        return result 
    def div(self):
        return self.num1 / self.num2 
    
#we must create object to call methods of the MyMath class
#object = ClassName()
m1 = MyMath() #we have to create object then we can call method using object
answer = m1.add()
print("addition = ",answer)
answer = m1.sub()
print("subtraction = ",answer)
answer = m1.mul()
print("multiplication = ",answer)
print("division = ",m1.div())



