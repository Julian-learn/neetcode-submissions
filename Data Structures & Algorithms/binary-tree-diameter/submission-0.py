# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(treenode):
            if not treenode:
                return 0

            nonlocal res
            left = dfs(treenode.left)
            right = dfs(treenode.right)
            res = max(left+right, res)
            return max(left, right) + 1
        
        dfs(root)
        return res
        