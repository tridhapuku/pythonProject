

class Solution:
    def twoSum(self, numbers, target: int) :
        i = 0
        listlen = len(numbers)
        ResultList = [0 , 0]
        for i in range(0, listlen):
            left = i + 1
            right = listlen - 1

            while left <= right:
                mid = int((left + right)/2)

                sum = numbers[i] + numbers[mid]

                if sum == target:
                    ResultList[0] = i + 1
                    ResultList[1] = mid + 1
                    return ResultList

                elif target > sum:
                    left = mid + 1
                else:
                    right = mid -1

#Test Class

Solun1 = Solution()
numbers = [2,7,11,15]
target = 9

numbers = [2,3,4]
target = 6

numbers = [-1, 0]
target = -1
print(Solun1.twoSum(numbers,target))
