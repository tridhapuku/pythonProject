

class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = i = 0
        listlen = len(nums)
        IndxForLastZero = listlen - 1
        ResultList = [ 0 ] * listlen
        while count < listlen:
            if nums[count] == 0:
                ResultList[IndxForLastZero] = 0
                IndxForLastZero -= 1
            else:
                ResultList[i] = nums[count]
                i+= 1
            count += 1
        return ResultList

    def moveZeroesWOList2(self, nums) -> None:
        i = 0
        count = 0
        listlen = len(nums)
        while count < listlen:

            if nums[count] != 0:
                nums[i] = nums[count]
                i += 1
            count += 1

        while i < listlen:
            nums[i] = 0
            i += 1

    def moveZeroesWOList3(self, nums) -> None:
        i = 0
        count = 0
        listlen = len(nums)
        while count < listlen:

            if nums[count] != 0:
                nums[i] = nums[count]
                i += 1
            count += 1

        while i < listlen:
            nums[i] = 0
            i += 1





#Test
nums = [0,1,0,3,12]

Soln1 = Solution()

print(Soln1.moveZeroes(nums))

