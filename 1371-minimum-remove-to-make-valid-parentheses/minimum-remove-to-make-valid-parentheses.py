class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        i_to_remove = set()
        stack = []

        for i, c in enumerate(s):
            if c not in "()":
                continue
            elif c == "(":
                stack.append(i)
            elif not stack:
                i_to_remove.add(i)
            else:
                stack.pop()
            
        i_to_remove = i_to_remove.union(set(stack))

        string = []
        for i, c in enumerate(s):
            if i not in i_to_remove:
                string.append(c)
        
        return "".join(string)