

def TwoSum(arr,sum):
    len1 = len(arr)
    complementDict = {}

    for i in range(len1):
        num = arr[i]
        complement = sum - num

        if complement in complementDict:
            return [complementDict[complement] , i ]
        else:
            complementDict[num] = i

    return 0

# Test Cases

arr = [2,7,11,15]
sum = 9

arr1 = [3,2,4]
sum1 = 6

print(TwoSum(arr1, sum1))

