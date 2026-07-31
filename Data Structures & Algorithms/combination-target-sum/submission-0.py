class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, leftover):
            if leftover == 0:
                res.append(cur.copy())
                return
            if i >= len(nums) or leftover < 0:
                return
            
            cur.append(nums[i])
            dfs(i, cur, leftover - nums[i])
            cur.pop()
            dfs(i + 1, cur, leftover)

        dfs(0, [], target)
        return res
