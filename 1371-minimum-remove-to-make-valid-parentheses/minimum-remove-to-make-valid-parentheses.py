class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count = 0
        res = []
        for c in s:
            if c == "(":
                count += 1
                res.append(c)
            elif c == ")" and count > 0:
                count -= 1
                res.append(c)
            elif c != ")":
                res.append(c)
        
        filtered = []
        for c in res[::-1]:
            if c == "(" and count > 0:
                count -= 1
                continue
            else:
                filtered.append(c)
        
        return "".join(filtered[::-1])
            



