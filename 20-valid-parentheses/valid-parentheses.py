class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        stack = []
        closedToOpen = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c not in closedToOpen:
                stack.append(c)
            else:
                if not stack or closedToOpen[c] != stack.pop():
                    return False
        return not stack
        
        
