# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashmap = {}
        index = 0
        while head:
            if head not in hashmap:
                hashmap[head] = index
                index += 1
                head = head.next
            else:
                return True
        return False