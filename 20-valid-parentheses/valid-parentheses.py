class Solution:
    def isValid(self, s: str) -> bool:
        closedToOpen = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if stack and c in closedToOpen:
                if closedToOpen[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack
