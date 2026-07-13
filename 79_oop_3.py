#crete class 
class MyMath:
    #define constructor 
    def __init__(self,number1,number2):
        #create instance variable 
        # self.variablename = value 
        self.num1 = number1
        self.num2 = number2
        print("num1 = ",self.num1, " num2 = ",self.num2)
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
number1 = int(input("Enter value for 1st number"))
number2 = int(input("Enter value for 2nd number"))

m1 = MyMath(number1,number2) #we have to create object then we can call method using object

answer = m1.add()
print("addition = ",answer)
answer = m1.sub()
print("subtraction = ",answer)
answer = m1.mul()
print("multiplication = ",answer)
print("division = ",m1.div())

print("let us create another object")
number1 = int(input("Enter value for 1st number"))
number2 = int(input("Enter value for 2nd number"))
m2 = MyMath(number1,number2)

print("addition = ",m2.add())
print("subtraction = ",m2.sub())
print("multiplication = ",m2.mul())
print("division = ",m2.div())






