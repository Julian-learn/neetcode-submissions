class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums) - 1
        lpoint = 0
        rpoint = n
        middle = (rpoint + lpoint) // 2
        while rpoint >= lpoint:
            if target > nums[middle]:
                lpoint = middle + 1
                middle = (rpoint + lpoint) // 2
            elif target < nums[middle]:
                rpoint = middle - 1
                middle = (rpoint + lpoint) // 2
            if target == nums[middle]:
                return middle

        return -1
