# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        q = deque()

        if root:
            q.append((root, root.val))
            count += 1
        
        while len(q):
            for i in range(len(q)):
                cur, highest = q.popleft()
                if cur.left:
                    if cur.left.val >= highest:
                        count += 1
                    new_highest = max(highest, cur.left.val)
                    q.append((cur.left, new_highest))
                if cur.right:
                    if cur.right.val >= highest:
                        count += 1
                    new_highest = max(highest, cur.right.val)
                    q.append((cur.right, new_highest))

        return count
