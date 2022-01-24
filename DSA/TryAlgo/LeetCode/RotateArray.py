
# class Solution:
# def rotate(self, nums: List[int], k: int) -> None:
def rotate( nums, k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # nums = nums[-k:] + nums[:-k]
    # return nums
    k = k % len(nums)
    ResultList = []
    for i in range(0,len(nums)):
        ResultList.append(nums[i-k])
    return ResultList


#Test

nums1 = [1,2,3,4,5,6]
k =1
print(rotate(nums1,k))

