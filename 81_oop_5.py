class Institute:
    #create class variable
    name = "THE EASYLEARN ACADEMY"
    count = 0
    def __init__(self,student_name):
        Institute.count = Institute.count + 1 #1
        self.roll_no = Institute.count
        self.student_name = student_name
    def display(self):
        print("Institute Name ", Institute.name)
        print("-"*100)
        print("Roll no ",self.roll_no)
        print("Student Name",self.student_name)
        print("-"*100)
    
#create object 
p1 = Institute("pratham patel")
p1.display()

p2 = Institute("prachi parmar")
p2.display()

p3 = Institute("Partia")
p3.display()

print("Institute name",Institute.name)
#change class variable
Institute.name = "T.E.L"
print("updated name ",Institute.name)
p1.display()
p2.display()
