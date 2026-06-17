class Solution:
    def findmin_index(self, nums: List[int]):
        l, r  = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return l
    def search(self, nums: List[int], target: int) -> int:
        min_index= self.findmin_index(nums)
        if target < nums[0]:
            l = min_index
            r = len(nums) - 1
        elif min_index == 0:
            l = 0
            r = len(nums) - 1
        else:
            l = 0
            r = min_index
        while l <= r:
            mid = (l + r) // 2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid 
        return -1   
            


        