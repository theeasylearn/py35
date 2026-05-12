'''
        * 
      * *
    * * *
  * * * *
* * * * *
'''
row = 5
count = 2
while row>=1:
  for space in range(1,row):
    print(' ',end=' ')
  for astrik in range(1,count):
    print("* ",end='')
  count=count+1
  print("") #new line
  row = row - 1


