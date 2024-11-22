class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count = 0
        stack = []

        for c in s:
            if c == "(":
                stack.append(c)
                count += 1
            elif c == ")" and count > 0:
                count -= 1
                stack.append(c)
            # we do not want -> count == ) and count == 0
            elif c != ")":
                stack.append(c)
        filtered = []
        for c in stack[::-1]:
            if c == "(" and count > 0:
                count -= 1
                continue
            filtered.append(c)
        return "".join(filtered[::-1])
            
        
       
        