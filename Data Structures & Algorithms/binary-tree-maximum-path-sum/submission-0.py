# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #Complicated Problem, i tried to understand the given solution
        #but couldnt solve myself
        #Main Idea: every Node has a return value (without splitting) and a path value
        #The return value is without splitting to keep the path properties, while the path value
        #can be another path in itself. 
        res = [root.val]
        
        def dfs(root):
            if not root:
                return 0
            
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            res[0] = max(res[0], root.val + leftMax + rightMax)

            return root.val + max(leftMax, rightMax) 
        
        dfs(root)
        return res[0]