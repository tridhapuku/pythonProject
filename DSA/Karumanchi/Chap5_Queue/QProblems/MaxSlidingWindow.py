

def MaxSlidingWindow(listA , K):
    lenA = len(listA)
    OutputWindow = []
    #Loop through each elem till
    for i in range(0 , lenA - (K -1)):
        tempMax = max(listA[i: i + K])
        # print(listA[i:i+K])
        # print(tempMax)
        OutputWindow.append(tempMax)

    return OutputWindow

def MaxSlidingWindowOptm(listA , K):
    lenA = len(listA)
    OutputWindow = []
    #Loop through each elem till
    for i in range(0 , lenA - (K -1)):
        tempMax = max(listA[i: i + K])
        # print(listA[i:i+K])
        # print(tempMax)
        OutputWindow.append(tempMax)

    return OutputWindow

listA1 = [1, 2, 3, 1, 4, 5, 2, 3, 6]
K = 3

listA2 = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
K2 = 4

# print(MaxSlidingWindow(listA1 , K))
print(MaxSlidingWindow(listA2 , K2))
