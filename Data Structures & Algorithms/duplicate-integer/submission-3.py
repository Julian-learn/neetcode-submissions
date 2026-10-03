class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        solset = set(nums)
        if len(solset) == len(nums):
            return False
        else:
            return True