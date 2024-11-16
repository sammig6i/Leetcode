class Solution:
    def calculate(self, s: str) -> int:
        # parse each number in the string
        # take care of order of operations according to pemdas: *, /, +, -
        # if * or / in stack, then immediately calculate the two numbers
        stack = []
        v = 0
        op = "+"

        for i, c in enumerate(s):
            if c.isdigit():
                v = v * 10 + int(c)

            if i == len(s) - 1 or c in ('+','-','*','/'):
                if op == "+":
                    stack.append(v)
                elif op == "-":
                    stack.append(-v)
                elif op == "*":
                    stack.append(stack.pop() * v)
                elif op == "/":
                    stack.append(int(stack.pop() / v))
                
                op = c
                v = 0
        return sum(stack)



        
            



        