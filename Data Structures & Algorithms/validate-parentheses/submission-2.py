class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {"{" : "}", "[" : "]", "(" : ")"}
        for i in range(len(s)):
            if len(stack) >= 1 and brackets.get(stack[-1]) == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        return len(stack) == 0