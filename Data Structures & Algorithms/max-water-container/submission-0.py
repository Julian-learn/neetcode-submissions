class Solution:
    def maxArea(self, heights: List[int]) -> int:
        current_highest = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            current_area = min(heights[l], heights[r]) * (r - l)
            if current_area > current_highest:
                current_highest = min(heights[l], heights[r]) * (r - l)
            if heights[l] > heights[r]:
                r -= 1
            elif heights[l] <= heights[r]:
                l += 1
        return current_highest