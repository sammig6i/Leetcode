class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c in {'+', '-', '/', '*'}:
                b = stack.pop() 
                a = stack.pop()
                if c == '+':
                    result = a + b
                    stack.append(result)
                elif c == '-':
                    result = a - b
                    stack.append(result)
                elif c == '*':
                    result = a * b
                    stack.append(result)
                elif c == '/':
                    result = int(a / b)
                    stack.append(result)
            else:
                stack.append(int(c))
        return stack[0]
