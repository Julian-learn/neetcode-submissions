class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        highest_streak = 0
        current_streak = 0
        current = 0
        for x in numset:
            if x-1 in numset:
                continue
            current = x    
            while current in numset:
                current += 1
                current_streak += 1
            if current_streak > highest_streak:
                highest_streak = current_streak
            current_streak = 0
        return highest_streak

