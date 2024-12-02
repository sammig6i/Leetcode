class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        closeToOpen = {")": "("}
        stack = []
        for c in s:
            if stack:
                if c == "(" or stack[-1] != closeToOpen[c]:
                    stack.append(c)
                else:
                    stack.pop()
            else:
                stack.append(c)
            
        return len(stack)

            
    # (()))

    # )))

    # "()))(("
    # 4
    # 
    # [()]