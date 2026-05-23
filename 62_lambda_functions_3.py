# def getMin(*values):
#     min = values[0]
#     for value in values:
#         if value<min:
#             min = value 
#     return min 

getMin = lambda *values: (
    (lambda m: [m := value for value in values if value < m] and m)(values[0])
)
print(getMin(10,5,20,100,200,2))