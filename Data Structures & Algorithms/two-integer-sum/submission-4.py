class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexmap = {}

        for i, num in enumerate(nums):
            
            looking_for = target - num
            if looking_for in indexmap:
                return [indexmap[looking_for], i]
            indexmap[num] = i
