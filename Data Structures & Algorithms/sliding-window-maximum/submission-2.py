class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        hashmap = {}
        cur = float("-infinity")
        r = 0

        while k > r:
            hashmap[nums[r]] = hashmap.get(nums[r], 0) + 1
            cur = max(nums[r], cur)
            r += 1 
        
        res.append(cur)
        length = len(nums)
        l = 0
        while r < length:
            if hashmap[nums[l]] <= 1:
                del hashmap[nums[l]]
            else:
                hashmap[nums[l]] -= 1
            l += 1
            hashmap[nums[r]] = hashmap.get(nums[r], 0) + 1
            
            cur = max(hashmap.keys())
            r += 1
            res.append(cur)
        return res
        








        