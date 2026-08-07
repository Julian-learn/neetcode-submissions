class ListNode:
    def __init__(self, val, next_node = None):
        self.val = val
        self.next = next_node

class LinkedList: 
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur.val

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
        if self.length == 0:
            self.tail = new_node
        self.length += 1

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = self.tail = new_node
        self.length += 1

    def remove(self, index: int) -> bool:
        if index >= self.length:
            return False
        
        if index == 0:
            self.head = self.head.next
            if self.length == 1:
                self.tail = None
        else:
            cur = self.head
            for i in range(index - 1):
                cur = cur.next
            cur.next = cur.next.next
            if index == self.length - 1:
                self.tail = cur
                
        self.length -= 1
        return True

    def getValues(self) -> List[int]:
        res = []
        cur = self.head
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res