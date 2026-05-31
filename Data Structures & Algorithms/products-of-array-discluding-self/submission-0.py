class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i in range(len(res)):
            for j in range(len(nums)):
                if i == j:
                    continue
                res[i] *= nums[j]
        return res

                


        