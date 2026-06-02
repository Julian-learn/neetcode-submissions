class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {"{" : "}", "[" : "]", "(" : ")"}
        for i in range(len(s)):
            stack.append(s[i])
            if len(stack) >= 2 and brackets.get(stack[-2]) == stack[-1]:
                stack.pop()
                stack.pop()
        return len(stack) == 0