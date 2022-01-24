# class Solution:
    # def search(self, nums: List[int], target: int) -> int:
def search( nums, target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right :
        mid = int((left + right) / 2)

        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1

class Solution:
    def searchInsert(self, nums, target: int) -> int:
        left = 0
        listlen = len(nums)
        right = listlen -1

        if listlen == 1:
            if target > nums[0]:
                return 1
            else:
                return 0
        else:
            while left <= right :
                mid = int((left + right) / 2)

                if target == nums[mid] :
                    return mid
                # elif target > nums[mid] and target < nums[mid + 1]:
                #     return mid + 1
                # elif target > nums[mid] and target >= nums[mid + 1]:
                #     left = mid + 1
                elif target > nums[mid] :
                    left = mid + 1
                elif target < nums[mid]:
                    right = mid -1

            if target < nums[mid]:
                return right + 1
            else:
                return left






nums1 =  [-1,0,3,5,9,12]
target = 0

# print(search(nums1,target))

nums2 = [2,6]
target = -9
ClassTest = Solution()
print(ClassTest.searchInsert(nums2 , target))