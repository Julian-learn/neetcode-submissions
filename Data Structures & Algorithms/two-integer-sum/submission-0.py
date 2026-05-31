class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for j in range(len(nums)):
            for i in range(len(nums)):
                if (nums[i] + nums[j]) == target and i != j:
                    sol = sorted([i, j])
                    return sol