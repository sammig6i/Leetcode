class Solution:
    def simplifyPath(self, path: str) -> str:
    #/.../a/../b/c/../d/./
        string = path.split("/")
        stack = []

        for c in string:
            if c == "..":
                if stack:
                    stack.pop()
            elif c in (".", ""):
                continue
            else:
                stack.append(c)
        return "/" + "/".join(stack)
        

            
        


