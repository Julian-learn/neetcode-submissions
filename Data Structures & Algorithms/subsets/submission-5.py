class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #my 2nd attempt, this time i found the solution myself!
        res = []
        length = len(nums)
        subset = []

        def dfs(i):
            if length == i:
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)

        dfs(0)
        return res