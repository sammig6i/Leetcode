class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        stack = []
        closedToOpen = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if stack:
                if c in closedToOpen and stack[-1] == closedToOpen[c]:
                    stack.pop()
                elif c not in closedToOpen:
                    stack.append(c)
                else:
                    return False
            else:
                stack.append(c)
            
        return not stack
        
        
