class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counts = Counter(s)
        res = []

        for c in order:
            if c in counts:
                res.append(c * counts[c])
                del counts[c]
        
        for char, count in counts.items():
            res.append(char * count)

        return "".join(res)

