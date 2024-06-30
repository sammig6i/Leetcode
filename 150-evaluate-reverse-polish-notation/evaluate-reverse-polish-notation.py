class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for c in tokens:
            if c in {'+', '-', '*', '/'}:
                b = int(stack.pop())
                a = int(stack.pop())

                if c == '+':
                    res = (a + b)
                elif c == '-':
                    res = (a - b)
                elif c == '*':
                    res = (a * b)
                elif c == '/':
                    res = int(a / b)
                stack.append(res)
            else:
                stack.append(int(c))
        return stack[-1]
                