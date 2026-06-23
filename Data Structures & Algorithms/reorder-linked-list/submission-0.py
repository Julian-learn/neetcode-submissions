# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        cur = head
        front = 0
        counter = 0
        while cur:
            stack.append(cur)
            cur = cur.next
            counter += 1
        if counter % 2 == 0:
            even = True
        else:
            even = False
        cur = head
        if even:
            while stack[-1] != stack[front]:
                front += 1
                if stack[-1] == stack[front]:
                    head.next = stack.pop()
                    head = head.next
                    break
                head.next = stack.pop()
                head = head.next
                head.next =  stack[front]
                head = head.next
            head.next = None
        else:
            while stack[-1] != stack[front]:
                front += 1
                head.next = stack.pop()
                head = head.next
                head.next =  stack[front]
                head = head.next
            head.next = None
        head = cur



                




        