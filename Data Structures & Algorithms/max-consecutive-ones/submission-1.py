class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        current_highest = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                if count > current_highest:
                    current_highest = count
            if nums[i] == 0:
                if count > current_highest:
                    current_highest = count
                count = 0
        return current_highest
