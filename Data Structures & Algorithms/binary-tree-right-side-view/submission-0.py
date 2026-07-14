# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        res = []

        if root:
            q.append(root)
        
        while len(q):
            cur_list = []
            for i in range(len(q)):
                cur = q.popleft()
                cur_list.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                
            res.append(cur_list[-1])
        
        return res

        