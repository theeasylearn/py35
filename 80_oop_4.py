class Room:
    #constructor (automatically execute)
    def __init__(self,length,width,depth=15):
        #create instance variable 
        self.length = length
        self.width = width
        self.depth = depth
        print("constructor function called automatically")

    def getArea(self):
        #create local variable
        area = self.length * self.width
        return area 
    def getVolume(self):
        return self.length * self.width * self.depth

#create object
print("Enter bedroom size")
length = int(input("Enter length"))
width = int(input("Enter width"))
depth = int(input("Enter depth"))

bedroom = Room(length,width,depth)
print("bedroom area = ",bedroom.getArea())
print("bedroom volume  = ",bedroom.getVolume())

print("Enter hall size")
length = int(input("Enter length"))
width = int(input("Enter width"))

hall = Room(length,width)
print("hall area = ",hall.getArea())
print("hall volume  = ",hall.getVolume())




