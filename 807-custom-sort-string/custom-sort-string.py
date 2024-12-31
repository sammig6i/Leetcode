class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counts = Counter(s)
        res = []

        for c in order:
            if c in counts:
                res.append(c * counts[c])
                counts[c] -= counts[c]
        
        for char, count in counts.items():
            if count > 0:
                res.append(char * counts[char])
        return "".join(res)

