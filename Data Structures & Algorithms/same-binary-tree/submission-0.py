# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.same = True
        if not p and not q:
            return self.same
        elif p and not q: #redundant
            self.same = False
            return self.same
        elif not p and q: #redundant, i keep just for overview of cases
            self.same = False
            return self.same
        elif p and q and p.val == q.val:
            self.same = self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)  
            return self.same          
        else:
            self.same = False
            return self.same