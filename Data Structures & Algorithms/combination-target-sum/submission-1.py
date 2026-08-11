class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums_len = len(nums)

        def dfs(i, leftover, subset):
            if leftover == 0:
                res.append(subset.copy())
                return
            
            if i < nums_len:
                subset.append(nums[i])
            else:
                return

            if i < nums_len and leftover > 0:
                dfs(i, leftover - nums[i], subset)

            subset.pop()
            dfs(i+1, leftover, subset)

        dfs(0, target, [])
        return res

        