# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        res_head = None
        point = head
        prev = ListNode(0)

        while True:
            count = k - 1
            current_head = point
            while count > 0 and point:
                point = point.next
                count -= 1
            if not point:
                prev.next = current_head
                break
            next_list = point.next
            point.next = None
            new_head = self.reverseList(current_head)
            if not res_head: #only happens once in first reversed list
                res_head = new_head
            prev.next = new_head
            prev = current_head
            point = next_list

            if not point:
                break
        return res_head



    def reverseList(self, head:Optional[ListNode]):
        prev = None
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev
        