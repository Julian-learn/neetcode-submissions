class MinStack:

    def __init__(self):
        self.stack = []
        self.helperstack = []
        
    def push(self, val: int) -> None:
        if not self.helperstack or self.helperstack[-1] >= val :
            self.helperstack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.helperstack[-1]:
            self.helperstack.pop()
        self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return None
        
    def getMin(self) -> int:
        return self.helperstack[-1]
