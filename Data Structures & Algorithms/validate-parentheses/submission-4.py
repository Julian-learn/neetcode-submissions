class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"(": ")", "[": "]", "{": "}"}

        for bracket in s:
            if stack and bracket == pairs[stack[-1]]:
                stack.pop()
            elif bracket in pairs:
                stack.append(bracket)
            else:
                return False
        
        if not stack:
            return True
        else:
            return False
                