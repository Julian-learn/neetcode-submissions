# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def depth(root):
            if not root:
                return 0
            ld = depth(root.left)
            rd = depth(root.right)
            #-1 means imbalance in this case, since the actual depth cannot be negative
            if ld == -1 or rd == -1:
                return -1
            
            dif = rd - ld
            if 1 < dif or dif < -1:
                return -1
            return 1 + max(ld, rd)

        if depth(root) < 0:
            return False
        else:
            return True
