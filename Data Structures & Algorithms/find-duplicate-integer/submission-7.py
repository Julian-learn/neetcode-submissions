class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        n = len(nums)
        #Floyds algorithm (find start of cycle)
        # First: Find first intersection between slow and fast pointer
        while True:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
            if slow == fast:
                break
        # Second: Find intersection between slow and second slow pointer
        # This gives me the start of the cycle
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        
        
