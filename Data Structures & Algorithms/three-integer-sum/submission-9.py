class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        n = len(nums)
        if n <= 2:
                return []
        for i in range(n - 2):
            if i-1 != -1 and nums[i-1] == nums[i]:
                continue
            l = i + 1 
            r = n - 1
            while l < r:
                current = [nums[i], nums[l], nums[r]]
                current_sum = sum(current)
                if current_sum == 0:
                    res.append(current)
                if current_sum >= 0:
                    r -= 1
                    while nums[r] == nums[r+1] and l < r:
                        r -= 1
                elif current_sum < 0:
                    l += 1
        return res
            



            
            
        