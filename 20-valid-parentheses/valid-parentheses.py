class Solution:
    def isValid(self, s: str) -> bool:
        closedMap = {")": "(", "]": "[", "}": "{"}
        res = []

        for p in s:
            if p not in closedMap:
                res.append(p)
                continue
            if not res or res[-1] != closedMap[p]:
                return False
            res.pop()
        
        return not res
            

            