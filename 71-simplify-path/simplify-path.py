class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")

        for c in path:
            if c == "..":
                if stack:
                    stack.pop()
            elif c in (".", ""):
                continue
            else:
                stack.append(c)
        return "/" + "/".join(stack)

        