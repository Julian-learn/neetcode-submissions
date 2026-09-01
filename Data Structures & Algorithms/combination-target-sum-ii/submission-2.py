class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, cur, leftover):
            if leftover == 0:
                res.append(cur.copy())
                return
            if leftover < 0 or i == len(candidates):
                return
            
            cur.append(candidates[i])
            dfs(i + 1, cur, leftover - candidates[i])
            cur.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1 #skip duplicates
            dfs(i+1, cur, leftover)

        dfs(0, [], target)
        return res