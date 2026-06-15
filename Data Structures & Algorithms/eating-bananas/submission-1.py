class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        from math import ceil
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            middle_k = (l + r) // 2
            hours = 0
            for p in piles:
                 hours += ceil(p / middle_k)
            if hours <= h:
                res = middle_k
                r = middle_k - 1 
            else:
                l = middle_k + 1
        return res
            
        
