class Solution:
    def simplifyPath(self, path: str) -> str:
        s = path.split("/")
        stack = []

        for c in s:
            if c == "..":
                if stack:
                    stack.pop()
            elif c in (".", ""):
                continue
            else:
                stack.append(c)
        return "/" + "/".join(stack)