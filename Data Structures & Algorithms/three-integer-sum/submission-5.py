class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        if len(nums) <= 2:
                return []
        for i in range(len(nums) - 2):
            l = i + 1 
            r = len(nums) - 1
            while l < r:
                current = [nums[i], nums[l], nums[r]]
                if sum(current) == 0 and current not in res:
                    res.append(current)
                if sum(current) >= 0:
                    r -= 1
                elif sum(current) < 0:
                    l += 1
        return res
            



            
            
        