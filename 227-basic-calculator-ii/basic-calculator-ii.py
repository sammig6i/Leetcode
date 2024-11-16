class Solution:
    def calculate(self, s: str) -> int:
        # parse each number in the string
        # take care of order of operations according to pemdas: *, /, +, -
        # if * or / in stack, then immediately calculate the two numbers
        stack = []
        v = 0
        sign = "+"

        for i, c in enumerate(s):
            if c.isdigit():
                v= v * 10 + int(c)

            if i == len(s) - 1 or c in ('+','-','*','/'):
                if sign == "+":
                    stack.append(v)
                elif sign == "-":
                    stack.append(-v)
                elif sign == "*":
                    stack.append(stack.pop() * v)
                elif sign == "/":
                    stack.append(int(stack.pop() / v))
                
                sign = c
                v = 0
        return sum(stack)



        
            



        