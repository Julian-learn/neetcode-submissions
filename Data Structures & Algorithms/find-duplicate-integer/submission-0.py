class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        bucket = [0] * n
        for num in nums:
            bucket[num] += 1
            if bucket[num] >= 2:
                return num