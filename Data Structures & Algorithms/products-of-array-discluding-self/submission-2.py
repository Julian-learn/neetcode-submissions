class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = [1]
        suffix = [1]
        length = len(nums)
        for i in range(1, len(nums)):
            prefix.append(prefix[i-1] * nums[i-1])
            suffix.append(suffix[i-1] * nums[length-i])
        for j in range(len(nums)):
            res.append(prefix[j] * suffix[-j-1])
        return res

                


        