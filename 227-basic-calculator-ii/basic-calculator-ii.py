class Solution:
    def calculate(self, s: str) -> int:
        v = 0
        stack = []
        op = "+"
        # res = 0

        for c in s + "+":
            if c.isdigit():
                v = v * 10 + int(c)
            elif c in ("+", "*", "/", "-"):
                if op == "+":
                    stack.append(v)
                elif op == "-":
                    stack.append(-v)
                elif op == "/":
                    stack.append(int(stack.pop() / v))
                elif op == "*":
                    stack.append(stack.pop() * v)
                op = c
                v = 0

        return sum(stack)
