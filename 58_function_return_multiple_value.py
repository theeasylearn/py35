def getSumAverage(*numbers):
    sum = 0
    count = 0
    for num in numbers:
        # print(num,end=' ')
        sum = sum + num 
        count = count + 1
    avg = sum / count
    return sum,avg #function return multiple value 
result = getSumAverage(10,20,30,40,50,200,125,300,500)
print(result)

sum, average = getSumAverage(1000,5000,25000)
print(f"sum = {sum} average = {average}")

