class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            middle = (l+r) // 2
            if nums[l] < nums[r]:
                return nums[l]
            elif nums[middle] >= nums[l]:
                l = middle + 1
            elif nums[middle] < nums[l]:
                r = middle


        return nums[middle]