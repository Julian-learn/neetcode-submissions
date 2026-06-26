# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #reverse
        prev1 = None
        prev2 = None
        #l1 reversal
        while l1:
            next_node1 = l1.next
            l1.next = prev1
            prev1 = l1
            l1 = next_node1 
        #l2 reversal
        while l2:
            next_node2 = l2.next
            l2.next = prev2
            prev2 = l2
            l2 = next_node2
        #prev1 and prev2 are the heads of the reversed lists
        l1 = prev1
        l2 = prev2
        #get the numbers and add them up
        first = ""
        second = ""
        while l1:
            first += str(l1.val)
            l1 = l1.next
        while l2:
            second += str(l2.val)
            l2 = l2.next
        res = str(int(first) + int(second))
        #create the new linked list
        dummy = ListNode(0, None)
        cur = dummy
        for i in range(len(res) - 1, -1, -1):
            next_node = ListNode(res[i], None)
            cur.next = next_node
            cur = cur.next
        return dummy.next
        