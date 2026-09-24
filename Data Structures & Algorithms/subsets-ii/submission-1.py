class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        length = len(nums)
        nums.sort()
        
        def recursion(i, subset): 
            if i >= length:
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            recursion(i+1, subset)

            subset.pop()
            while i+1 < length and nums[i] == nums[i+1]:
                i += 1
            recursion(i+1, subset)
        
        recursion(0, [])
        return res
        