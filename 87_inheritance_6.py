class KB:
    #constructor
    def __init__(self,bytes):
        #create instance variable 
        self.bytes = bytes 
        print("KB constructor called..")
    def getKB(self):
        #create local variable 
        kilobytes = self.bytes / 1024
        return kilobytes


#inheritance 
class MB(KB):
    def __init__(self, bytes):
        #calling parent class constructor
        super().__init__(bytes)
        print("MB class constructor is called....")
 
    def getMB(self):
        kilobytes = super().getKB()
        megabytes = kilobytes / 1024
        return megabytes
    
m1 = MB(10000000) #calling MB class constructor 1st but it will parent class constructor and run it first
result = m1.getMB()
print("MEGABYTES  ",result)
