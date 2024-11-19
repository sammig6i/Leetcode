class Solution:
    def calculate(self, s: str) -> int:
        curr_sum = 0
        res = 0
        v = 0
        op = "+"

        for i, c in enumerate(s + "+"):
            if c.isdigit():
                v = v * 10 + int(c)
            if c in ("+", "*", "/", "-"):
                if op == "+":
                    curr_sum += v
                elif op == "-":
                    curr_sum -= v
                elif op == "/":
                    curr_sum = int(curr_sum / v)
                elif op == "*":
                    curr_sum *= v
                
                if c in ("+", "-"):
                    res += curr_sum
                    curr_sum = 0
                op = c
                v = 0
                
        return res
