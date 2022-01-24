


def IntervalScheduling(StartTime , FinishTime , NoOfTasks):
    print(FinishTime)
    FinishTime.sort()
    SortedArray = FinishTime[:]
    print(SortedArray)
    ResultList = []
    count = 0
    PrevFinishTime = SortedArray[0]
    ResultList.append(SortedArray[0])
    for i in range(NoOfTasks):
        NextItem = SortedArray[i]

        if i >= 1:
            PrevFinishTime = ResultList[-1]

        if StartTime[i] >= PrevFinishTime:
            ResultList.append(NextItem)
            count += 1
        else:
            continue

    return ResultList


def IntervalScheduling2(ListDic , NoOfTasks):

    if NoOfTasks < 1:
        return
    SortedFinishTime = sorted(ListDic , key = lambda i:i['finishTime'])
    startTime = 'startTime'
    finishTime = 'finishTime'
    #Iterate over range
    # Get NextItem
    # Check if Overlapping : Overlapping Check : PresentStartTime >= PrevFinishTime
    # if yes --> just contnue
    # Else:
    # Add it to result list

    PrevFinishTime = SortedFinishTime[0][finishTime]
    ResultLisDic = []
    ResultLisDic.append(SortedFinishTime[0])
    count = 0
    for i in range(NoOfTasks):
        NextItem = SortedFinishTime[i]

        if i > 0:
            PrevFinishTime = ResultLisDic[-1][finishTime]

        if NextItem[startTime] >= PrevFinishTime:
            ResultLisDic.append(SortedFinishTime[i])
            count += 1
        else:
            continue

    return ResultLisDic









#TestCases
StartTime = [0 , 1, 3,3,4,5,6,8]
FinishTime = [6, 4, 5, 8,7, 9, 10,11]

ListDic = [ {'startTime' : 0 , 'finishTime' : 6} , \
            {'startTime' : 1 , 'finishTime' : 4} , \
            {'startTime' : 3 , 'finishTime' : 5} , \
            {'startTime' : 3 , 'finishTime' : 8} , \
            {'startTime' : 4 , 'finishTime' : 7} , \
            {'startTime' : 5 , 'finishTime' : 9} , \
            {'startTime' : 6 , 'finishTime' : 10} , \
            {'startTime' : 8 , 'finishTime' : 11} , ]

ListDic2 = [ {'name': 'A', 'startTime' : 0 , 'finishTime' : 6} , \
            {'name': 'B', 'startTime' : 1 , 'finishTime' : 4} , \
            {'name': 'C', 'startTime' : 3 , 'finishTime' : 5} , \
            {'name': 'D', 'startTime' : 3 , 'finishTime' : 8} , \
            {'name': 'E', 'startTime' : 4 , 'finishTime' : 7} , \
            {'name': 'F', 'startTime' : 5 , 'finishTime' : 9} , \
            {'name': 'G', 'startTime' : 6 , 'finishTime' : 10} , \
            {'name': 'H', 'startTime' : 8 , 'finishTime' : 11} ,]

NoOfTasks = len(StartTime)

# print(IntervalScheduling(StartTime, FinishTime , NoOfTasks))
# print(IntervalScheduling2(ListDic , len(ListDic)))
print(IntervalScheduling2(ListDic2 , len(ListDic2)))


