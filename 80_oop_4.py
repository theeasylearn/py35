class Room:
    def __init__(self,length,width,depth):
        #create instance variable 
        self.length = length
        self.width = width
        self.depth = depth

    def getArea(self):
        #create local variable
        area = self.length * self.width
        return area 
    def getVolume(self):
        return self.length * self.width * self.depth

#create object
bedroom = Room(15,20,12)
print("bedroom area = ",bedroom.getArea())
print("bedroom volume  = ",bedroom.getVolume())

hall = Room(30,30,12)
print("hall area = ",hall.getArea())
print("hall volume  = ",hall.getVolume())


