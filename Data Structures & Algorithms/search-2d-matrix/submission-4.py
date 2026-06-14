class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lowrow = 0
        highrow = len(matrix) - 1
        while lowrow <= highrow:
            middlerow = (lowrow + highrow) // 2
            if target > matrix[middlerow][0] and target > matrix[middlerow][-1]:
                lowrow = middlerow + 1
            elif target < matrix[middlerow][0] and target < matrix[middlerow][-1]:
                highrow = middlerow - 1
            else:
                l = 0
                r = len(matrix[0]) - 1
                while l <= r:
                    middle = (l + r) // 2
                    if target > matrix[middlerow][middle]:
                        l = middle + 1
                    elif target < matrix[middlerow][middle]:
                        r = middle - 1
                    else:
                        return True
                return False
        return False
 
        