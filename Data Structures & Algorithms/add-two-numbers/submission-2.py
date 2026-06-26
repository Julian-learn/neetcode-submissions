# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #solution simulating addition
        dummy = ListNode()
        cur = dummy
        overhead = 0
        while l1 or l2 or overhead:
            res = (l1.val if l1 else 0) + (l2.val if l2 else 0) + overhead
            overhead, digit = res // 10, res % 10
            cur.next = ListNode(digit)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
            

        