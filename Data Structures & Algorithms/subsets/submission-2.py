class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        length = len(nums)
        
        def recursion(i, subset):
            cur = subset 
            if i >= length:
                res.append(cur.copy())
                return
            
            cur.append(nums[i])
            recursion(i+1, cur)

            cur.pop()
            recursion(i+1, cur)
        
        recursion(0, [])
        return res