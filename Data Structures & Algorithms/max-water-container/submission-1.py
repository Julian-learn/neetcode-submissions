class Solution:
    def maxArea(self, heights: List[int]) -> int:
        current_highest = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            current_area = min(heights[l], heights[r]) * (r - l)
            if current_area > current_highest:
                current_highest = current_area
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return current_highest