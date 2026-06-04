class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = ["+", "-", "*", "/"]
        for token in tokens:
            if token not in operands:
                stack.append(int(token))
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            if token == "*":
                stack.append(stack.pop() * stack.pop())
            if token == "-":
                stack.append(-(stack.pop() - stack.pop()))
            if token == "/":
                stack.append(int((1 / stack.pop()) * stack.pop()))
        return stack[-1]
        