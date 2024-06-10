class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closedToOpen = {")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            if c in closedToOpen:
                if stack and closedToOpen[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack