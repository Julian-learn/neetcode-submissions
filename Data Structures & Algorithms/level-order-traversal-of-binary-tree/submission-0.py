# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        res = []

        if root:
            q.append(root)
        level = 0
        while len(q) > 0:
            cur_list = []
            for i in range(len(q)):
                cur = q.popleft()
                cur_list.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            
            res.append(cur_list)
        
        return res
