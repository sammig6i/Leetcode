class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count = 0
        stack = []

        for c in s:
            if c == ")" and count == 0:
                continue
            elif c == "(":
                count += 1
            # we do not want -> count == ) and count == 0
            elif c == ")":
                count -= 1
            stack.append(c)

        filtered = []
        for c in stack[::-1]:
            if c == "(" and count > 0:
                count -= 1
                continue
            filtered.append(c)
        return "".join(filtered[::-1])
        