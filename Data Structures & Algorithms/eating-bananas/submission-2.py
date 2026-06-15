class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        from math import ceil
        lowest = 1
        highest = max(piles)
        res = highest
        while lowest <= highest:
            middle_k = (lowest + highest) // 2
            hours = 0
            for p in piles:
                 hours += ceil(p / middle_k)
            if hours <= h:
                res = middle_k
                highest = middle_k - 1 
            else:
                lowest = middle_k + 1
        return res
            
        
