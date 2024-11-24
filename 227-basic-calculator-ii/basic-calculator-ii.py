class Solution:
    def calculate(self, s: str) -> int:
        op = "+"
        stack = []
        v = 0

        for i, c in enumerate(s):
            if c.isdigit():
                v = v * 10 + int(c)
            if i == len(s) - 1 or c in ("+", "-", "/", "*"):
                if op == "+":
                    stack.append(v)
                elif op == "-":
                    stack.append(-v)
                elif op == "*":
                    stack.append(stack.pop() * v)
                elif op == "/":
                    stack.append(int(stack.pop() / v))
                v = 0
                op = c
        return sum(stack)
