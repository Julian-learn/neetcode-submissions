# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #get 2nd half of list
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reorder 2nd half of list
        first, second = head, slow.next
        slow.next = prev = None
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node
        
        #merge lists
        #second = None here from previous loop
        #prev is the start of the reversed 2nd half of the list
        first = head
        second = prev
        while second:
            next_node1 = first.next
            next_node2 = second.next
            first.next = second
            second.next = next_node1
            first = next_node1
            second = next_node2

