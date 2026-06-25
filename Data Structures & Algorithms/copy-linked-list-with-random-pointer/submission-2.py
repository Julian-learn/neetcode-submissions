"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        dummy = Node(0, None, None)
        cur = head
        cur_copy = Node(cur.val, None, None)
        dummy.next = cur_copy

        hashmap = {}
        while cur:
            hashmap[cur] = cur_copy
            cur = cur.next
            if cur:
                cur_copy.next = Node(cur.val, None, None)
            cur_copy = cur_copy.next
        
        for original, copy in hashmap.items():
            copy.random = hashmap.get(original.random)
        
        return dummy.next