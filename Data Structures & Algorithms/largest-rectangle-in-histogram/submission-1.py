class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights += [0]
        largest = 0
        for h in heights:
            width = 0
            while stack and h < stack[-1][0]:
                width += stack[-1][1]
                if largest < stack[-1][0] * width:
                    largest = stack[-1][0] * width
                stack.pop()
            stack.append([h, 1 + width])
        return largest
            
                

            