class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexmap = {}

        for i in range(len(nums)):
            indexmap[nums[i]] = i 
        
        for i in range(len(nums)):
            looking_for = target - nums[i]
            if looking_for in indexmap and indexmap[looking_for] != i:
                return [i, indexmap[looking_for]]
        return []