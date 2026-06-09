class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = len(numbers) - 1
        l = 0
        while r > l:
            k = numbers[r] + numbers[l]
            if k == target:
                return [l + 1, r + 1]
            elif k > target:
                r -= 1
            else:
                l += 1

        
        