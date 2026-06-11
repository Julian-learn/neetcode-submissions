class Solution:
    def trap(self, height: List[int]) -> int:
        right_max = [0] * len(height)
        total_water = 0
        current_tallest = 0
        for j in range(len(height) - 1, -1, -1):
            current_tallest = max(height[j], current_tallest)
            right_max[j] = current_tallest

        left_max = 0
        for i, h in enumerate(height):
            left_max = max(left_max, h)
            total_water += min(left_max, right_max[i]) - h    
        return total_water