class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
            elif token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "-":
                stack.append(-(stack.pop() - stack.pop()))
            elif token == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
        return stack[-1]
        