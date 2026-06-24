# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        point = head
        length = 0
        while point:
            length += 1
            point = point.next
        point = head
        steps = length - n - 1
        if length == 1:
            return None
        elif length == n:
            head = head.next
            return head
        while steps != 0:
            steps -= 1
            point = point.next
        point.next = point.next.next
        return head
            
        