class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        soltuple = set(nums)
        if len(soltuple) == len(nums):
            return False
        else:
            return True