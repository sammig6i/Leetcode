class Solution:
    def calculate(self, s: str) -> int:
        op = "+"
        res = 0
        curr_sum = 0
        v = 0

        for i, c in enumerate(s):
            if c.isdigit():
                v = v * 10 + int(c)
            if i == len(s) - 1 or c in ("+", "-", "/", "*"):
                if op == "+":
                    curr_sum += v
                elif op == "-":
                    curr_sum -= v
                elif op == "*":
                    curr_sum *= v
                elif op == "/":
                    curr_sum = int(curr_sum / v)
                op = c
                v = 0

                if i == len(s) - 1 or c in ("-","+"):
                    res += curr_sum
                    curr_sum = 0
            
        return res


