
def getMerit(maths,science,english,hindi,gujarati,computer):
    total = maths + science + english 
    return total 

m = 100
s = 99
e = 98
h = 60
g = 50
c = 40

# print(getMerit(h,g,c,m,s,e)) wrong way of calling function
#keyword arguments
print(getMerit(hindi=h,gujarati=g,computer=c,maths=m,science=s,english=e))