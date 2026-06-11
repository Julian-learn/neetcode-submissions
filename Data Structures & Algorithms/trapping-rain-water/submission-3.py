class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        right_max = [0] * len(height)
        max_area = 0
        current_tallest = 0
        for j in range(len(height) - 1, -1, -1):
            right_max[j] = current_tallest
            if height[j] > current_tallest:
                current_tallest = height[j]    
        for i, h in enumerate(height):
            if h > height[l]:
                l = i
            if i == 0:
                continue
            if min(height[l], right_max[i]) - h > 0:
                max_area += min(height[l], right_max[i]) - h    
                
                
        return max_area
                    
        