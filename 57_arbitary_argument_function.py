def printSumAverage(*numbers):
    sum = 0
    count = 0
    for num in numbers:
        # print(num,end=' ')
        sum = sum + num 
        count = count + 1

    print("sum " , sum)
    avg = sum / count
    print("average " , avg)
printSumAverage(10,20,30,40,50,200,125,300,500)
