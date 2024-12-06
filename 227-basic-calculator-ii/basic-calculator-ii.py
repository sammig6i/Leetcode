class Solution:
    def calculate(self, s: str) -> int:
        op = "+"
        curr_res = 0
        res = 0
        v = 0

        for c in s + "+":
            if c.isdigit():
                v = v * 10 + int(c)
            if c in ("+","-","*","/"):
                if op == "+":
                    curr_res += v
                elif op == "-":
                    curr_res -= v
                elif op == "*":
                    curr_res *= v
                elif op == "/":
                    curr_res = int(curr_res / v)
                
                if c in ("+","-"):
                    res += curr_res
                    curr_res = 0

                op = c
                v = 0
        return res
    
# curr_res = 0
# v = 0
# res = 7