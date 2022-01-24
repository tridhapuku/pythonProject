
import random

NoOfIteration = 0

def MergeSort(arr):
    global NoOfIteration
    NoOfIteration += 1
    mid = len(arr) // 2
    if len(arr) > 1:
        LeftArr = arr[:mid]
        RightArr = arr[mid:]

        MergeSort(LeftArr)
        MergeSort(RightArr)

        #Merge the Sorted Arrays
        i = j = k= 0
        ResultArr = []
        while i < len(LeftArr) and j < len(RightArr):
            if LeftArr[i] <= RightArr[j]:
                ResultArr.append(LeftArr[i])
                arr[k] = LeftArr[i]
                i += 1
            else:
                ResultArr.append(RightArr[j])
                arr[k] = RightArr[j]
                j += 1
            k += 1
            NoOfIteration += 1

        while i < len(LeftArr):
            ResultArr.append(LeftArr[i])
            arr[k] = LeftArr[i]
            i += 1
            k += 1
            NoOfIteration += 1

        while j < len(RightArr):
            ResultArr.append(RightArr[j])
            arr[k] = RightArr[j]
            j += 1
            k += 1
            NoOfIteration += 1

    # return ResultArr


#Test Cases
arr = [12, 11, 13, 5, 6, 7]
print("Given array is", end="\n")
# print(arr)
# MergeSort(arr)
print("Sorted array is: ", end="\n")
# print(arr)
# print(NoOfIteration)

arr2 = random.sample(range(1,9999999999) , 9800000)
# print(arr2)
MergeSort(arr2)
# print(arr2)
print(NoOfIteration)

