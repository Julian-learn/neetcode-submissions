# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Solution using Dummy method to avoid defining extra ifs for edge cases
        dummy = ListNode(0, head)
        point = head
        length = 0
        while point:
            length += 1
            point = point.next
        point = dummy
        steps = length - n
        while steps != 0:
            steps -= 1
            point = point.next
        point.next = point.next.next
        return dummy.next 
            
        